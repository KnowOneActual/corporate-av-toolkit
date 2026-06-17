#!/usr/bin/env python3
import os
import subprocess
import re

# Color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def decode_manufacturer_id(bytes_data):
    if len(bytes_data) < 2:
        return "UNK"
    # Manufacturer ID is 3 compressed ASCII characters (5 bits each)
    val = (bytes_data[0] << 8) | bytes_data[1]
    char1 = chr(((val >> 10) & 0x1F) + 64)
    char2 = chr(((val >> 5) & 0x1F) + 64)
    char3 = chr((val & 0x1F) + 64)
    return f"{char1}{char2}{char3}"

def parse_edid_block(edid_bytes):
    if len(edid_bytes) < 128:
        return None
    
    # Check EDID header: 00 FF FF FF FF FF FF 00
    header = edid_bytes[0:8]
    if header != b'\x00\xff\xff\xff\xff\xff\xff\x00':
        return None
        
    info = {}
    
    # Manufacturer ID
    info["mfg_id"] = decode_manufacturer_id(edid_bytes[8:10])
    
    # Product Code (2 bytes, little-endian)
    product_code = edid_bytes[10] | (edid_bytes[11] << 8)
    info["product_code"] = f"{product_code:04X}"
    
    # Serial number (4 bytes, little-endian)
    serial = edid_bytes[12] | (edid_bytes[13] << 8) | (edid_bytes[14] << 16) | (edid_bytes[15] << 24)
    info["serial"] = f"{serial:08X}"
    
    # Week & Year of manufacture
    info["week"] = edid_bytes[16]
    info["year"] = edid_bytes[17] + 1990
    
    # EDID Version/Revision
    info["version"] = f"{edid_bytes[18]}.{edid_bytes[19]}"
    
    # Video input parameters (Digital/Analog)
    video_input = edid_bytes[20]
    info["is_digital"] = bool(video_input & 0x80)
    
    # Physical size in cm
    info["width_cm"] = edid_bytes[21]
    info["height_cm"] = edid_bytes[22]
    
    # Display descriptors (18-byte blocks starting at 54, 72, 90, 108)
    model_name = None
    serial_str = None
    
    for start in (54, 72, 90, 108):
        block = edid_bytes[start : start + 18]
        if len(block) < 18:
            continue
        # Descriptors start with 00 00 00
        if block[0:3] == b'\x00\x00\x00':
            descriptor_type = block[3]
            # 0xFC = Display Name
            if descriptor_type == 0xFC:
                try:
                    name_bytes = block[5:18]
                    # Terminated by 0x0A or space padded
                    end_idx = name_bytes.find(0x0A)
                    if end_idx != -1:
                        name_bytes = name_bytes[:end_idx]
                    model_name = name_bytes.decode('ascii', errors='ignore').strip()
                except Exception:
                    pass
            # 0xFF = Serial Number String
            elif descriptor_type == 0xFF:
                try:
                    sn_bytes = block[5:18]
                    end_idx = sn_bytes.find(0x0A)
                    if end_idx != -1:
                        sn_bytes = sn_bytes[:end_idx]
                    serial_str = sn_bytes.decode('ascii', errors='ignore').strip()
                except Exception:
                    pass
                    
    info["model_name"] = model_name or "Unknown Monitor"
    if serial_str:
        info["serial_string"] = serial_str
        
    return info

def get_displays_sysfs():
    displays = {}
    drm_dir = "/sys/class/drm"
    if not os.path.exists(drm_dir):
        return displays
        
    for dev in os.listdir(drm_dir):
        edid_path = os.path.join(drm_dir, dev, "edid")
        status_path = os.path.join(drm_dir, dev, "status")
        
        if os.path.exists(status_path) and os.path.exists(edid_path):
            with open(status_path, 'r') as f:
                status = f.read().strip()
                
            if status == "connected":
                try:
                    with open(edid_path, 'rb') as f:
                        edid_data = f.read()
                    if edid_data and len(edid_data) >= 128:
                        displays[dev] = edid_data
                except Exception:
                    pass
    return displays

def get_displays_xrandr():
    displays = {}
    try:
        # Run xrandr --verbose to extract hex EDID
        res = subprocess.run(["xrandr", "--verbose"], capture_output=True, text=True, check=True)
        current_output = None
        edid_hex = []
        in_edid = False
        
        for line in res.stdout.split('\n'):
            # Check for output connection start
            match_conn = re.match(r'^(\S+) connected', line)
            if match_conn:
                current_output = match_conn.group(1)
                in_edid = False
                edid_hex = []
                continue
                
            if current_output:
                if "EDID:" in line:
                    in_edid = True
                    continue
                if in_edid:
                    # EDID hex lines start with whitespace and contain hex characters
                    match_hex = re.match(r'^\s+([0-9a-fA-F]+)\s*$', line)
                    if match_hex:
                        edid_hex.append(match_hex.group(1))
                    else:
                        # End of EDID block
                        in_edid = False
                        if edid_hex:
                            try:
                                binary_data = bytes.fromhex("".join(edid_hex))
                                displays[current_output] = binary_data
                            except Exception:
                                pass
                            edid_hex = []
    except Exception:
        pass
    return displays

def main():
    print(f"{BOLD}{CYAN}=== CORPORATE AV DISPLAY & EDID DIAGNOSTICS ==={RESET}\n")
    print("Reading display metadata and EDID handshakes from the system...\n")
    
    # Try reading from sysfs first, fall back to xrandr
    displays = get_displays_sysfs()
    if not displays:
        displays = get_displays_xrandr()
        
    if not displays:
        print(f"{RED}No active connected displays with valid EDIDs could be detected.{RESET}")
        print(f"Verify your HDMI/DP cables and ensure the display is powered on.")
        return
        
    for name, edid_data in displays.items():
        info = parse_edid_block(edid_data)
        if not info:
            print(f"{BOLD}Display: {name}{RESET}")
            print(f"  {YELLOW}Status: Connected but EDID is corrupted or unreadable.{RESET}")
            print()
            continue
            
        print(f"{BOLD}Display Port: {CYAN}{name}{RESET}")
        print(f"  {BOLD}Device Name     {RESET}: {GREEN}{info['model_name']}{RESET}")
        print(f"  {BOLD}Manufacturer ID {RESET}: {info['mfg_id']} (Product Code: {info['product_code']})")
        
        serial_display = info.get('serial_string') or info['serial']
        print(f"  {BOLD}Serial Number   {RESET}: {serial_display}")
        print(f"  {BOLD}Year of Mfg     {RESET}: {info['year']} (Week {info['week']})")
        
        signal_type = "Digital (HDMI/DP/USB-C)" if info['is_digital'] else "Analog (VGA)"
        print(f"  {BOLD}Signal Interface{RESET}: {signal_type}")
        
        # Display physical dimensions and calculate diagonal in inches
        if info['width_cm'] > 0 and info['height_cm'] > 0:
            width_in = info['width_cm'] / 2.54
            height_in = info['height_cm'] / 2.54
            diagonal = (width_in**2 + height_in**2)**0.5
            print(f"  {BOLD}Physical Size   {RESET}: {info['width_cm']} x {info['height_cm']} cm ({diagonal:.1f}\" Diagonal)")
        else:
            print(f"  {BOLD}Physical Size   {RESET}: Variable / Projection Screen")
            
        print(f"  {BOLD}EDID Version    {RESET}: {info['version']}")
        print(f"  {GREEN}● EDID Handshake OK{RESET}")
        print()
        
    print("-" * 60)
    print(f"\n{BOLD}{CYAN}Diagnostic Complete!{RESET}")

if __name__ == "__main__":
    main()
