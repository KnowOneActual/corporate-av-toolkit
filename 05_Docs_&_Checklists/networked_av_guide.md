# 🌐 Networked AV (Dante, Q-LAN & AV-over-IP) Configuration & Troubleshooting Guide

Modern corporate AV systems rely heavily on networked audio and video. Signals are no longer routed over dedicated analog or HDMI cabling; instead, they travel as IP packets over standard gigabit network infrastructure. 

This guide details configuration requirements and troubleshooting workflows for the two most common network protocols in corporate boardrooms: **Dante / Q-LAN (Audio)** and **Crestron NVX / AMX SVSI (AV-over-IP Video)**.

---

## 🎙️ 1. Networked Audio: Dante & Q-LAN

### What are they?
- **Dante (Audinate)**: A proprietary, low-latency, uncompressed digital audio networking technology. It uses standard Layer 3 IP packets.
- **Q-LAN (Q-SYS)**: A suite of network protocols designed by QSC to transmit uncompressed audio, video, and control data.

### Critical Network Requirements:
To prevent audio clicks, pops, dropouts, or clock sync failures, the network switch must be configured as follows:

| Setting | Requirement | Rationale |
| :--- | :--- | :--- |
| **Energy Efficient Ethernet (EEE / 802.3az)** | **MUST BE DISABLED** | EEE turns off ethernet ports when no traffic is detected. PTP (Precision Time Protocol) packets are intermittent, causing EEE to repeatedly sleep/wake the port, causing clock drift and dropouts. |
| **Multicast IGMP Snooping** | **Enabled** | Dante uses multicast to route audio flows to multiple destinations. Without IGMP snooping, the switch treats multicast as broadcast and floods *every* port, overwhelming wireless access points and control processors. |
| **IGMP Querier** | **Enabled (Exactly One)** | IGMP snooping requires a Querier on the VLAN to maintain the list of active multicast subscribers. If there is no Querier, multicast tables expire and audio cuts out after 2-5 minutes. |
| **Quality of Service (QoS)** | **Strict Priority queuing (DSCP)** | Audio clock packets (PTP) must be given absolute priority over general network traffic. |

### Dante/Q-LAN DSCP (QoS) Mappings:
Switches must prioritize the following DSCP values:
- **PTP Clock (Highest Priority)**: DSCP **CS7** (56) or **EF** (46).
- **Audio Streams (Medium-High Priority)**: DSCP **EF** (46) or **AF41** (34).
- **Control / Video Streams**: DSCP **CS3** (24) or **AF11** (10).

---

## 📺 2. AV-over-IP: Crestron NVX & Video Distribution

### What is it?
AV-over-IP (AVoIP) encodes high-resolution HDMI video (up to 4K @ 60Hz 4:4:4) into high-bandwidth multicast streams. A single 4K NVX stream can consume **350 Mbps to 850 Mbps** of network bandwidth.

### Critical Network Requirements:
1. **IGMP Snooping v2/v3**: Enabled on the AV VLAN.
2. **IGMP Querier**: Must be active on the AV VLAN to prevent the switch from flooding video traffic to all ports.
3. **Jumbo Frames**: Set MTU to **9000 bytes** (or at least 1500+). Many AVoIP encoders pack maximum data into packets to reduce processing overhead. If Jumbo Frames are disabled, packets are fragmented, causing visual artifacts, frame drops, or black screen.
4. **Fast Leave (Immediate Leave)**: Enabled on the switch. When a display switches channels, it leaves the old multicast group. Fast Leave instantly stops the old video stream from feeding that port, preventing port congestion when switching sources.
5. **Switch Interconnect Link (SIL / Trunk Bandwidth)**: If routing AVoIP streams between switches, ensure the trunk port is a **10Gbps link** or uses **Link Aggregation (LAG/LACP)**. Standard 1Gbps uplinks will choke on a single 4K video stream.

---

## 🛠️ 3. Troubleshooting Workflows & Symptoms

### Symptom A: "Audio drops out after exactly 2 to 5 minutes."
- **Diagnosis**: IGMP Snooping is enabled, but **no IGMP Querier is active** on the network.
- **Why**: When a Dante receiver starts, it sends an IGMP Join. The switch routes the audio. After a few minutes, the switch queries the network to see if anyone is still listening. Since there is no Querier to send this query, the switch assumes the receiver has left, and stops sending the multicast audio.
- **Solution**: Log into the core switch and enable **IGMP Querier** on the AV VLAN, or set a static Querier IP address.

### Symptom B: "Audio has constant clicks, pops, or digital crackling."
- **Diagnosis**: Clock Synchronization / PTP jitter.
- **Why**: Clock packets (PTP v1 for Dante v3, PTP v2 for Dante v4/Q-LAN) are being delayed by other network traffic, or Energy Efficient Ethernet (EEE) is enabled.
- **Solution**: 
  1. Open **Dante Controller** and check the **Clock Status** tab. Look for "Clock Status: Muted" or high jitter indicators.
  2. Disable **EEE (Green Ethernet / 802.3az)** on all network switch ports connected to AV devices.
  3. Ensure QoS is enabled and configured to prioritize DSCP 56 (PTP) and DSCP 46 (Audio).

### Symptom C: "Matrix switching works, but the video stream is stuttering or frozen."
- **Diagnosis**: Port saturation or packet fragmentation.
- **Why**: The AVoIP streams are exceeding the port bandwidth (e.g. trying to push 1.2 Gbps over a 1 Gbps port) or MTU mismatch.
- **Solution**:
  1. Enable **Jumbo Frames** on the switches (MTU 9000).
  2. Check switch port statistics for packet drops, CRC errors, or input/output utilization exceeding 90%.
  3. If using multiple switches, verify the link interconnect bandwidth (10G minimum recommended).
  4. Lower the bitrate or resolution profile in the NVX/AVoIP transmitter's web panel (e.g. cap peak bitrate at 450 Mbps).

---

## 🧰 4. Essential CLI Diagnostics Commands

If you have console access to the AV network switches, run these commands to verify settings:

### On Cisco Catalyst Switches:
```bash
show ip igmp snooping            # Verify IGMP Snooping status globally & per VLAN
show ip igmp snooping groups     # List active multicast groups and ports subscribed
show ip igmp snooping querier    # Verify if a Querier is detected and on which IP
show mac address-table multicast # Verify how multicast MAC addresses are mapped
show interface <port> counters   # Look for input errors, CRC errors, or drops
```

### On Netgear AV Line (M4250/M4300):
```bash
show igmp                       # Show IGMP snooping configuration
show igmp querier               # Show active IGMP querier
show port-channel summary       # Check status of switch-to-switch LAG/LACP trunks
```
