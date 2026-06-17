import os
import subprocess
import re
import math

# Color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def get_cameras():
    cameras = []
    v4l_dir = "/sys/class/video4linux"
    if os.path.exists(v4l_dir):
        for dev in sorted(os.listdir(v4l_dir)):
            name_file = os.path.join(v4l_dir, dev, "name")
            if os.path.exists(name_file):
                with open(name_file, 'r') as f:
                    name = f.read().strip()
                # Exclude metadata devices (v4l often creates a second metadata device for a single camera)
                if "metadata" not in name.lower() and name not in cameras:
                    cameras.append(name)
    return cameras

def run_pactl(cmd_type):
    # cmd_type can be "sources" or "sinks"
    env = os.environ.copy()
    env['LANG'] = 'C'
    try:
        res = subprocess.run(["pactl", "list", "short", cmd_type], capture_output=True, text=True, env=env, check=True)
        return res.stdout.strip().split('\n')
    except (subprocess.SubprocessError, FileNotFoundError):
        return []

def get_default_device(cmd_type):
    # cmd_type is "source" or "sink"
    env = os.environ.copy()
    env['LANG'] = 'C'
    try:
        res = subprocess.run(["pactl", "get-default-" + cmd_type], capture_output=True, text=True, env=env, check=True)
        return res.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        # Fallback to pactl info
        try:
            res = subprocess.run(["pactl", "info"], capture_output=True, text=True, env=env, check=True)
            for line in res.stdout.split('\n'):
                if f"Default {cmd_type.capitalize()}:" in line:
                    return line.split(":", 1)[1].strip()
        except:
            pass
    return None

def parse_audio_devices(lines, default_name):
    devices = []
    for line in lines:
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) >= 4:
            idx = parts[0]
            name = parts[1]
            fmt = parts[3] # e.g. "s32le 2ch 48000Hz"
            
            # Find sample rate
            match = re.search(r'(\d+)Hz', fmt)
            rate = int(match.group(1)) if match else None
            
            is_default = (name == default_name)
            devices.append({
                "index": idx,
                "name": name,
                "format": fmt,
                "rate": rate,
                "is_default": is_default
            })
    return devices

def main():
    print(f"{BOLD}{CYAN}=== CORPORATE AV HARDWARE DIAGNOSTICS ==={RESET}\n")
    
    # 1. Cameras
    print(f"{BOLD}📷 Video Input Devices (Cameras):{RESET}")
    cameras = get_cameras()
    if not cameras:
        print(f"  {RED}No cameras detected.{RESET}")
    else:
        for cam in cameras:
            print(f"  {GREEN}●{RESET} {cam}")
            
    print("\n" + "-" * 50)
    
    # 2. Audio Inputs (Microphones)
    print(f"\n{BOLD}🎙️ Audio Input Devices (Microphones/Sources):{RESET}")
    default_source = get_default_device("source")
    sources_raw = run_pactl("sources")
    sources = parse_audio_devices(sources_raw, default_source)
    
    if not sources:
        print(f"  {RED}No audio inputs detected.{RESET}")
    else:
        for src in sources:
            default_str = f" {BOLD}{CYAN}[DEFAULT]{RESET}" if src["is_default"] else ""
            rate_str = f"{src['rate']} Hz" if src["rate"] else "Unknown"
            
            if src["rate"] == 48000:
                rate_color = GREEN
                status_str = f"{GREEN}[OK]{RESET}"
            elif src["rate"] == 44100:
                rate_color = YELLOW
                status_str = f"{YELLOW}[WARNING]{RESET}"
            else:
                rate_color = RED
                status_str = f"{RED}[ALERT]{RESET}"
                
            print(f"  {GREEN}●{RESET} {src['name']}{default_str}")
            print(f"    Sample Rate: {rate_color}{rate_str}{RESET} {status_str}")
            if src["rate"] != 48000:
                print(f"    {YELLOW}↳ Hint: Teams/Zoom prefer 48000 Hz to prevent audio click/sync issues.{RESET}")

    print("\n" + "-" * 50)
    
    # 3. Audio Outputs (Speakers/Sinks)
    print(f"\n{BOLD}🔊 Audio Output Devices (Speakers/Sinks):{RESET}")
    default_sink = get_default_device("sink")
    sinks_raw = run_pactl("sinks")
    sinks = parse_audio_devices(sinks_raw, default_sink)
    
    if not sinks:
        print(f"  {RED}No audio outputs detected.{RESET}")
    else:
        for snk in sinks:
            default_str = f" {BOLD}{CYAN}[DEFAULT]{RESET}" if snk["is_default"] else ""
            rate_str = f"{snk['rate']} Hz" if snk["rate"] else "Unknown"
            
            if snk["rate"] == 48000:
                rate_color = GREEN
                status_str = f"{GREEN}[OK]{RESET}"
            elif snk["rate"] == 44100:
                rate_color = YELLOW
                status_str = f"{YELLOW}[WARNING]{RESET}"
            else:
                rate_color = RED
                status_str = f"{RED}[ALERT]{RESET}"
                
            print(f"  {GREEN}●{RESET} {snk['name']}{default_str}")
            print(f"    Sample Rate: {rate_color}{rate_str}{RESET} {status_str}")
            if snk["rate"] != 48000:
                print(f"    {YELLOW}↳ Hint: Teams/Zoom prefer 48000 Hz to prevent audio click/sync issues.{RESET}")

    print("\n" + "-" * 50)
    print(f"\n{BOLD}{CYAN}Diagnostic Complete!{RESET}")

if __name__ == "__main__":
    main()
