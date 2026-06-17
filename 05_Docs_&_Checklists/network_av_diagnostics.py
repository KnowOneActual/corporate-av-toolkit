import os
import subprocess
import re
import math
import sys

# Color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

TARGETS = [
    {"name": "Google DNS (Global)", "ip": "8.8.8.8"},
    {"name": "Cloudflare DNS (Global)", "ip": "1.1.1.1"}
]

def ping_target(ip, count=10):
    print(f"Pinging {ip} {count} times to measure latency, loss, and jitter...")
    # Linux ping flags: -c count, -i interval (0.2s for faster run)
    cmd = ["ping", "-c", str(count), "-i", "0.2", ip]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return res.stdout
    except subprocess.TimeoutExpired:
        print(f"{RED}Ping command timed out!{RESET}")
        return None
    except FileNotFoundError:
        print(f"{RED}Ping command not found on system!{RESET}")
        return None

def analyze_ping_output(output):
    if not output:
        return None
    
    rtts = []
    packet_loss = 100.0
    
    # Parse individual RTTs
    # Example line: 64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=14.5 ms
    for line in output.split('\n'):
        match = re.search(r'time=([\d\.]+)\s*ms', line)
        if match:
            rtts.append(float(match.group(1)))
            
    # Parse summary statistics
    # Example line: 10 packets transmitted, 10 received, 0% packet loss, time 1805ms
    loss_match = re.search(r'(\d+)%\s*packet\s*loss', output)
    if loss_match:
        packet_loss = float(loss_match.group(1))
        
    if not rtts:
        return {
            "loss": 100.0,
            "min": 0, "max": 0, "avg": 0, "jitter": 0,
            "rtts": []
        }
        
    # Calculate jitter (RFC 1889 / RFC 3550 style: mean of absolute differences between consecutive pings)
    diffs = []
    for i in range(1, len(rtts)):
        diffs.append(abs(rtts[i] - rtts[i-1]))
    jitter = sum(diffs) / len(diffs) if diffs else 0.0
    
    return {
        "loss": packet_loss,
        "min": min(rtts),
        "max": max(rtts),
        "avg": sum(rtts) / len(rtts),
        "jitter": jitter,
        "rtts": rtts
    }

def print_result_row(metric, value, unit, thresholds, value_format="{:.1f}"):
    ok_val, warn_val = thresholds
    color = GREEN
    status = "OK"
    
    if value > warn_val:
        color = RED
        status = "ALERT"
    elif value > ok_val:
        color = YELLOW
        status = "WARNING"
        
    formatted_val = value_format.format(value)
    print(f"  {BOLD}{metric:<15}{RESET}: {color}{formatted_val:<8} {unit:<4}{RESET} [{color}{status:<7}{RESET}] (Target: <{ok_val}{unit})")

def main():
    print(f"{BOLD}{CYAN}=== NETWORK PERFORMANCE DIAGNOSTICS FOR AV ==={RESET}\n")
    print("This tool measures latency, packet loss, and jitter, comparing them")
    print("against standard thresholds for Zoom, Microsoft Teams, and Webex.\n")
    
    success = False
    for target in TARGETS:
        print(f"{BOLD}Testing path to: {target['name']} ({target['ip']}){RESET}")
        raw_out = ping_target(target['ip'])
        stats = analyze_ping_output(raw_out)
        
        if stats and stats["rtts"]:
            success = True
            print(f"\n{BOLD}Results:{RESET}")
            # Latency: OK < 150ms, Warn < 300ms
            print_result_row("Avg Latency", stats["avg"], "ms", (150.0, 300.0))
            # Jitter: OK < 30ms, Warn < 50ms
            print_result_row("Jitter", stats["jitter"], "ms", (30.0, 50.0))
            # Packet Loss: OK < 1.0%, Warn < 2.0%
            print_result_row("Packet Loss", stats["loss"], "%", (1.0, 2.0))
            
            print(f"  {BOLD}Min/Max RTT{RESET}    : {stats['min']:.1f} ms / {stats['max']:.1f} ms")
            print()
            
            # Overall evaluation
            if stats["loss"] > 2.0 or stats["jitter"] > 50.0 or stats["avg"] > 300.0:
                print(f"  {BOLD}Status: {RED}POOR{RESET} - High risk of audio dropouts, frozen video, or screen share lag.")
                print(f"  {YELLOW}↳ Action: Check if client is on Wi-Fi instead of Ethernet. Verify firewall rules.{RESET}")
            elif stats["loss"] > 1.0 or stats["jitter"] > 30.0 or stats["avg"] > 150.0:
                print(f"  {BOLD}Status: {YELLOW}MARGINAL{RESET} - Call will work, but you may experience latency or minor quality drops.")
                print(f"  {YELLOW}↳ Action: Close bandwidth-heavy apps. Avoid wireless if possible.{RESET}")
            else:
                print(f"  {BOLD}Status: {GREEN}EXCELLENT{RESET} - Network path meets high-quality corporate AV streaming standards.")
            print("\n" + "="*60 + "\n")
        else:
            print(f"  {RED}Failed to reach {target['ip']}.{RESET}\n")
            
    if not success:
        print(f"{RED}Error: Could not perform network diagnostics. Check local network connection.{RESET}")

if __name__ == "__main__":
    main()
