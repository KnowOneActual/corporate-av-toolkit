# 🛠️ Corporate AV Testing & Calibration Toolkit

Welcome to your custom **Corporate AV Testing & Calibration Toolkit**. This toolkit has been programmatically generated to provide AV technicians, IT support, and event production crews with high-precision assets to verify, tune, and troubleshoot audio-visual systems in conference rooms, boardrooms, and hybrid meeting spaces (Zoom, Microsoft Teams, Webex, etc.).

---

## 🚀 NEW: Interactive HTML5 AV Dashboard (`index.html`)

At the root of the toolkit is [index.html](file:///home/user/Desktop/test_media_toolkit/index.html) — a **self-contained, high-fidelity Web Dashboard** designed to be run directly on any technician's laptop or the local room PC. It runs offline and requires no installation.

Features include:
1. **Interactive Audio Generators**: Play precise sine, square, triangle, or sawtooth waves with custom frequencies (20 Hz to 20 kHz), pink noise, white noise, and live stereo channel routing checks.
2. **Speaker Polarity Phase Tester**: Alternates tones dynamically between In-Phase and Out-of-Phase to audit wiring polarity.
3. **AV Lip-Sync Latency Sweep**: A canvas visualizer and synchronized audio beep with adjustable offsets to calibrate display lag.
4. **Fullscreen Calibration Patterns**: Launch high-end vectors for display alignment, focus grids, SMPTE color bars, pixel checks, and screen share text legibility charts.
5. **Real-time WebRTC Mics & Cameras**: Preview webcams and monitor physical room microphones with an animated VU level meter.
6. **Digital Compliance Checklists**: Carry out MTR/Zoom Room walkthroughs and Pre-Event tech checks, auto-saving progress locally and exporting clean run-sheet logs.

---

## 📂 Folder & File Organization

The AV test media folder has been organized into the following logical subdirectories:

### 📁 `01_Audio_&_Sync/`
High-precision audio assets and synchronization checks.
* 🔊 **`audio_01_ref_1khz_tone.wav`**: A steady **1 kHz sine wave at -20 dBFS** (10s). Use this to align input/output levels across your DSP, mixer, and amplifiers. It should register exactly at the reference mark on your meters.
* 🔊 **`audio_02_stereo_channel_check.wav`**: Alternates pulses on the **Left channel only** (0-4s), **Right channel only** (4-8s), and a **Steady tone on both** (8-12s) to verify speaker routing.
* 🔊 **`audio_03_frequency_sweep_20hz_20khz.wav`**: A logarithmic frequency sweep spanning **20 Hz to 20 kHz** (15s). Listen for volume drops or **buzzes/rattles** in ceiling tiles, vents, or mounts.
* 🔊 **`audio_04_pink_noise_eq.wav`**: Standard **Voss-McCartney Pink Noise** at -18 dBFS. Useful for real-time analyzers (RTA) to measure frequency response and EQ room acoustics.
* 🔊 **`audio_05_phase_test.wav`**: Alternates pulsed tone and pink noise between In-Phase and Out-of-Phase (180° inverted Right channel) to check physical speaker wiring polarity.
* 🎥 **`video_01_av_sync_latency_test.mp4`**: A 30 FPS video featuring a moving red bar and a visual flash synchronized with a 1 kHz audio beep. **Measure latency** by stepping frame-by-frame (VLC: `E`) to see where the beep lines up relative to center.

### 📁 `02_Display_Calibration/`
Visual reference patterns and projector/display alignment documents.
* 🖼️ **`image_01_display_convergence.png`**: Grid pattern with a central circle and corner crosshairs. **Check aspect ratios** (if the center circle is an ellipse, the screen scaling is wrong) and **corner focus**.
* 🖼️ **`image_02_screen_share_legibility.png`**: Chart containing text from 6pt to 32pt, color contrast tests, and fine 1px/2px line grids. Use this to test screen sharing compression over Zoom/Teams.
* 📊 **`ALIGN 16x9.pptx` / `16x9 SI TEST.pptx`**: Widescreen test slides.
* 🖼️ **`Black_blank_slide_1080.jpg` / `Curtis_Chart_RGB_8bit.jpg` / `PB2.png`**: Display calibration and convergence graphics.
* 📁 **`Legacy_PowerPoints/`**: Contains old calibration slides (`.ppt` format).

### 📁 `03_Looping_Video_Backgrounds/`
Video assets for projection mapping, digital signage, and virtual backgrounds.
* 🎥 **`CLEANROOM (loop).mp4` / `FLUFFF (loop).mp4`**: Office and textured ambient video loops.
* 🎥 **`abstract_light_waves.mp4` / `blue_shining_stream_beam.mp4` / `golden_center_light_rays.mp4` / `lines_of_green_lights_move_in_waves.mp4` / `blue_black_vertical_shining_beam.mp4`**: Highly optimized H.264 video loops for screen calibration and lobby signage testing.

### 📁 `04_Presentations_&_Scripts/`
Corporate slide decks, presenter notes, and scripts.
* 📁 **`av_funny_presentation/`**: PPTX slides, speaker notes, and teleprompter scripts for a humorous AV-themed presentation.
* 📁 **`av_tech_run_though_PPTX/`**: Technical rehearsal deck and script.
* 📄 **`Presentation Example.pdf`**: Sample PDF presentation.

### 📁 `05_Docs_&_Checklists/`
Operational checklists, troubleshooting guides, and hardware/network diagnostics.
* 📄 **`Convention Center AV Equipment Checklist.pdf`**: Venue AV reference document.
* 📄 **`footage_eula.pdf`**: End User License Agreement for video assets.
* 📄 **`edid_hdmi_troubleshooting.md`**: Guide for resolving EDID mismatches, HDCP blocks, and screen flickering.
* 📄 **`networked_av_guide.md`**: Detailed network switch configuration and troubleshooting guide for Dante audio and AV-over-IP.
* 📄 **`mtr_zoom_rooms_daily_check.md`**: Daily walkthrough checklist for Microsoft Teams Rooms and Zoom Rooms setups.
* ⚙️ **`av_hardware_diagnostics.py`**: Python script to query local microphones, speakers, and cameras, verifying 48 kHz sample rates.
* ⚙️ **`display_diagnostics.py`**: Python script to query connected video displays and decode detailed EDID profiles (manufacturer, size, serials).
* ⚙️ **`network_av_diagnostics.py`**: Python script to measure latency, loss, and jitter against conferencing thresholds.
* ⚙️ **`generate_toolkit.py`**: The script used to generate the audio and image calibration files.
* ⚙️ **`optimize_toolkit.py`**: The cleanup and compression automation utility.

---

## 🎥 AV Sync & Lip-Sync Latency Test

### The Problem
In corporate hybrid environments, audio and video travel through separate paths:
* **Audio**: Mics ➡️ Room DSP (Biamp/Q-SYS) ➡️ USB Bridge ➡️ Computer ➡️ Teams/Zoom.
* **Video**: Camera ➡️ USB Grabber ➡️ Computer ➡️ Teams/Zoom (or Laptop screen share).
Because DSPs apply intensive processing (Acoustic Echo Cancellation, noise reduction), audio is often delayed relative to video, causing jarring "lip-sync" issues on calls.

### How to use `01_Audio_&_Sync/video_01_av_sync_latency_test.mp4`
1. Play the video in the room on the main display, routing audio to the room speakers.
2. Record the display and speaker output using a smartphone camera (at 30fps or 60fps) or look closely at the sync bar.
3. If analyzing a recording, import the clip into a video editor or open it in **VLC Media Player**.
4. In VLC, press **`E`** to step through the video frame-by-frame:
   * **Perfect Sync**: The 1 kHz audio beep is heard *exactly* when the screen flashes teal and the red bar is matched the center **0 ms (SYNC)** line.
   * **Audio Lagging**: The beep is heard when the red bar is on the **RIGHT (+)** side of the track. If it aligns at `+100 ms`, you need to delay the video by 100ms or reduce audio DSP processing.
   * **Video Lagging**: The beep is heard when the red bar is on the **LEFT (-)** side of the track. If it aligns at `-200 ms`, you need to add 200ms of audio delay in your DSP.

---

## 💻 Zoom / Microsoft Teams Screen Share Testing

When sharing presentations in hybrid meetings, video codecs will compress high-frequency details. Use `02_Display_Calibration/image_02_screen_share_legibility.png` to verify what remote participants actually see:

1. **Start a test call** between the conference room PC and a remote laptop (simulate a home worker).
2. **Share your screen** containing `02_Display_Calibration/image_02_screen_share_legibility.png`.
3. **Compare settings**:
   * **Default Share**: Great for text, but slides with animations or videos will stutter.
   * **"Optimize for video clip" (Zoom/Teams)**: Forces the codec into a higher frame rate but significantly drops resolution, converting colors to 4:2:0 subsampling.
4. **On the remote laptop, verify**:
   * **Red-on-Black Text Box**: In 4:2:0 compression, red text on black often smudges and becomes unreadable. If this text is illegible, presentation designers should avoid red-on-black or red-on-blue color combos.
   * **Small Text**: Read down the font sizes. If 6pt or 8pt text is blurry, the screen sharing resolution is scaling down.
   * **Moiré Circles**: If concentric circles show weird moving waves (moiré patterns), it indicates scaling distortion between the host and client screens.

---

## 📋 Pre-Event Technician Checklist (AV Walkthrough)

Use this checklist 60-90 minutes before any high-profile corporate presentation or meeting.

### 1. Physical Room Check
* [ ] **Sightlines**: Sit in the back row and corner seats. Can you see the main display and confidence monitor without obstruction?
* [ ] **Cabling**: All floor cables taped down (gaffer tape) or under cord protectors to prevent tripping.
* [ ] **Podium / Table**: Clear of clutter. Presenter water glass placed away from laptop and mics.
* [ ] **Clicker**: Fresh batteries in the slide clicker/advancer. Test it from the furthest corner of the stage.

### 2. Audio & Microphones (The most critical element)
* [ ] **Gain Check**: Play `01_Audio_&_Sync/audio_01_ref_1khz_tone.wav` to set master levels.
* [ ] **Wireless Mics**: Check battery levels (replace if below 2 bars). Perform a physical walk test:
  * Walk to the back, corners, and right under speaker lobbies.
  * Listen for dropouts, RF interference, or static.
* [ ] **Lapel Mics**: Clip lapel mics high on the chest (sternum level), avoiding loose collars or heavy jewelry that might clatter against the capsule.
* [ ] **Feedback Prevention**: Step in front of the house speakers with a live mic. Ensure the DSP feedback suppressor catches any ring, or slightly pull down the 1kHz-4kHz range in the EQ if ringing occurs.
* [ ] **Ceiling / Boundary Mics**: Run `01_Audio_&_Sync/audio_03_frequency_sweep_20hz_20khz.wav` at typical house volume. Verify nothing in the ceiling grid rattles.

### 3. Display & Video
* [ ] **Display Alignment**: Open `02_Display_Calibration/image_01_display_convergence.png`.
  * Ensure the image fills the screen exactly (no overscan cropping).
  * Verify the aspect ratio is correct (center circle must be perfectly round).
  * Check focus in all four corners.
* [ ] **Dongle / Adapter Roulette**: Test the physical connection from the presenter's laptop (HDMI, USB-C) using the stage cables.
* [ ] **Confidence Monitor**: Confirm the floor monitor is configured in "Presenter View" (slides + notes + timer) rather than mirroring the main display.

### 4. Presentation & Laptop Check
* [ ] **Power**: Presentation laptop plugged into AC power (don't run on battery!).
* [ ] **Notifications**: Enable "Do Not Disturb" / "Focus Assist" on the presentation computer to suppress emails, Slack, or system update alerts.
* [ ] **Embedded Media**: Verify slides with embedded videos play smoothly and route audio through HDMI/USB to the room speakers, NOT the tiny laptop speakers.
* [ ] **Screensaver**: Disable screen-lock and screensaver timeouts on the presentation computer.

### 5. Far-End / Hybrid Check (Zoom / Teams)
* [ ] **Audio Loopback**: Start a call, speak into the room mics, and record/listen from the remote side. Ensure no echo is heard (AEC calibration).
* [ ] **Legibility**: Share `02_Display_Calibration/image_02_screen_share_legibility.png` and verify remote readability.
* [ ] **AV Sync**: Play `01_Audio_&_Sync/video_01_av_sync_latency_test.mp4` on the call and verify lip-sync timing.
* [ ] **Virtual Backgrounds**: If using room backgrounds, check that the host computer has enough CPU/GPU to key out the presenter's background smoothly without glitching.

---

## 📄 License & Disclaimer

This project is licensed under the MIT License - see the [LICENSE](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/LICENSE) file for details.
For the End User License Agreement (EULA) and operational warnings, please refer to the [DISCLAIMER.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/DISCLAIMER.md) file.

---

*Toolkit compiled & generated on: 2026-06-13*
