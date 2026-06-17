# 📺 EDID, HDMI & Display Troubleshooting Guide

In corporate environments, video signals travel through complex paths: laptops connect to USB-C hubs, which convert to HDMI, which goes to wall plates, through HDBaseT/AV-over-IP transmitters, into matrix switchers, and finally to displays or projectors. 

This guide details the most common failure points—**EDID**, **HDCP**, and **cabling**—and how to troubleshoot them.

---

## 🧩 1. EDID (Extended Display Identification Data) Issues

### What is EDID?
EDID is a metadata profile that a display (monitor/projector) sends to a source (laptop) to declare its capabilities: supported resolutions (e.g., 1080p, 4K), aspect ratios (16:9, 16:10), refresh rates (60Hz, 30Hz), and audio formats.

### The Symptom:
* Laptop is connected, but the screen says "No Signal" or "Format Not Supported."
* The image on the screen is stretched, squashed, or blurry.
* The laptop screen flickers repeatedly as if trying to connect, but never succeeds.

### The Root Cause:
Boardroom matrix switchers, distribution amplifiers, or HDBaseT extenders sit between the laptop and the display. If these middle devices fail to pass the display’s EDID back to the laptop, the laptop default to a resolution or refresh rate the display cannot show.

### How to Fix It:
1. **Force Laptop Resolution**: Manually change the laptop display output to standard **1920x1080 at 60Hz**. This is the most universally supported resolution.
2. **EDID Copy/Emulation on Switchers**: On professional matrix switchers (Crestron, Extron, Atlona, Lightware), access the web interface or physical switches and configure the input port to use a **"Static EDID" (1080p 60Hz with 2ch audio)** instead of dynamic EDID.
3. **Power Cycle the Signal Chain**: Turn off the display, unplug the switcher, wait 10 seconds, plug it back in, and turn on the display. This forces a fresh EDID handshake.

---

## 🔒 2. HDCP (High-bandwidth Digital Content Protection) Blocks

### What is HDCP?
HDCP is digital copy protection designed to prevent interception of audio and video content. HDMI links must authenticate each other. If any device in the signal chain does not support HDCP (or if the handshake fails), the content is blocked.

### The Symptom:
* You can see the laptop desktop, but as soon as you open a browser with **Netflix, YouTube, or a corporate training video**, the video screen goes completely black, or displays a green screen/snow, while audio continues to play.
* The screen displays an explicit "HDCP Error" or "Content Protection Error."

### The Root Cause:
* The laptop is trying to output HDCP-protected content, but one of the extenders, capture cards (e.g., USB grabber), or older displays in the boardroom is not HDCP-compliant.
* **Handshake Timeout**: The HDCP encryption keys failed to negotiate within the required time window due to cable length or signal degradation.

### How to Fix It:
1. **Disable HDCP on Input Switcher**: Many professional switcher inputs allow you to disable HDCP support. This tells the laptop that the display chain is not HDCP compliant, forcing the browser to scale down the stream to non-HDCP resolutions instead of blocking the image entirely.
2. **Bypass Capturing Devices**: If routing through a USB capture card (for Zoom/Teams rooms), ensure the video content is not copyright-protected, or bypass the capture card and plug directly into the display.
3. **Use an HDMI Splitter**: In emergencies, inserting a cheap, basic HDMI splitter between the laptop and the extender chain can sometimes strip HDCP or handle the handshake locally, letting the video pass.

---

## ⚡ 3. Screen Flickering & Intermittent Blackouts

### The Symptom:
* The image displays fine, but randomly drops to black for 2-3 seconds, then comes back. This repeats every few minutes.
* You see "white sparkles" or "snow" (digital noise) flickering across the screen.

### The Root Cause:
* **HDMI Cable Integrity**: HDMI is a high-speed digital bus. If a cable is damaged, too long, or poorly shielded, packets are dropped.
* **USB-C Dongle Bloat**: The presenter is using a cheap, unpowered USB-C multi-port adapter. The HDMI output chip inside the dongle is overheating or starved of current.

### How to Fix It:
1. **Shorten/Upgrade Cable**: Replace passive HDMI cables longer than 15 feet (5 meters) with **Active HDMI cables** or HDBaseT extenders.
2. **Verify Dongle Quality**: Swap the user's multi-port adapter for a high-quality, dedicated USB-C to HDMI adapter (e.g., Apple, Anker, StarTech).
3. **Lower Refresh Rate**: If outputting 4K, change the laptop display settings from **4K @ 60Hz to 4K @ 30Hz** (or drop down to 1080p @ 60Hz). This reduces the required bandwidth by half, allowing degraded cables to pass the signal.

---

## 🔊 4. Audio Over HDMI Failure

### The Symptom:
* Video is perfect on the display, but sound is coming out of the laptop's tiny speakers instead of the room's sound system.

### How to Fix It:
1. **Select Correct Output Device**: Click the speaker icon in the laptop OS system tray and verify that the HDMI display device (e.g., "Extron HDMI", "Crestron", or the TV model) is selected as the default playback device.
2. **Check App Output settings**: In Zoom/Teams/Webex, check the application settings and ensure the **Speaker** output is explicitly set to the HDMI device, not the default audio jack.
3. **EDID Audio Support**: If the laptop doesn't even show the HDMI device in its audio list, it means the switcher or display EDID profile is set to "Video Only". You must update the switcher input EDID setting to include **LPCM 2-Channel Audio**.
