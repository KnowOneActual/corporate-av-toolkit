# 🛠️ Corporate AV Testing & Calibration Toolkit

This repository contains the **Corporate AV Testing & Calibration Toolkit**, providing files and diagnostic tools to verify, calibrate, and troubleshoot audio-visual systems in conference rooms, boardrooms, and hybrid meeting spaces (Zoom, Microsoft Teams, Webex, etc.).

---

## 🚀 Interactive HTML5 AV Dashboard (`index.html`)

At the root of the toolkit is [index.html](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/index.html) — an offline Web Dashboard that runs directly on a laptop or room PC without installation.

Features:
1. **Audio Generators**: Plays sine, square, triangle, and sawtooth waves (20 Hz to 20 kHz), pink noise, white noise, and stereo channel sweeps.
2. **Polarity Tester**: Alternates tones between In-Phase and Out-of-Phase to check speaker wiring polarity.
3. **AV Lip-Sync Sweep**: Canvas visualizer and synchronized audio beep to calibrate display lag.
4. **Calibration Patterns**: Convergence patterns, focus grids, SMPTE color bars, pixel checks, and text legibility charts.
5. **WebRTC Diagnostics**: Previews local webcams and monitors microphone levels with a VU meter.
6. **Checklists**: Digital walkthrough checklists for Zoom/MTR setups that export run-sheet logs.

---

## 📂 Folder & File Organization

The toolkit is organized into the following subdirectories:

### 📁 `01_Audio_&_Sync/`
Audio assets and synchronization signals.
* 🔊 **`audio_01_ref_1khz_tone.wav`**: A steady 1 kHz sine wave at -20 dBFS (10s). Use it to align input and output levels across the DSP, mixer, and amplifiers.
* 🔊 **`audio_02_stereo_channel_check.wav`**: Plays audio on the left channel (0–4s), right channel (4–8s), and both channels (8–12s) to verify speaker routing.
* 🔊 **`audio_03_frequency_sweep_20hz_20khz.wav`**: A 15-second logarithmic frequency sweep (20 Hz to 20 kHz) to identify rattles or resonance in ceiling tiles, vents, and mounts.
* 🔊 **`audio_04_pink_noise_eq.wav`**: Pink noise at -18 dBFS for real-time analyzers (RTA) to measure frequency response and calibrate room EQ.
* 🔊 **`audio_05_phase_test.wav`**: Plays in-phase and out-of-phase tones to verify speaker wiring polarity.
* 🎥 **`video_01_av_sync_latency_test.mp4`**: A 30 FPS sync video with a moving bar and flash aligned with a 1 kHz tone. Use to measure audio-to-video latency.

### 📁 `02_Display_Calibration/`
Visual patterns and documents for display alignment.
* 🖼️ **`image_01_display_convergence.png`**: Convergence grid to verify aspect ratio, scaling, and corner focus.
* 🖼️ **`image_02_screen_share_legibility.png`**: Legibility chart containing text (6pt to 32pt) and line grids to test screen-share compression.
* 📊 **`ALIGN 16x9.pptx` / `16x9 SI TEST.pptx`**: Widescreen test slides.
* 🖼️ **`Black_blank_slide_1080.jpg` / `Curtis_Chart_RGB_8bit.jpg` / `PB2.png`**: Display calibration and convergence graphics.
* 📁 **`Legacy_PowerPoints/`**: Legacy calibration slides (.ppt).

### 📁 `03_Looping_Video_Backgrounds/`
Video assets for digital signage and virtual backgrounds.
* 🎥 **`CLEANROOM (loop).mp4` / `FLUFFF (loop).mp4`**: Office and textured ambient video loops.
* 🎥 **`abstract_light_waves.mp4` / `blue_shining_stream_beam.mp4` / `golden_center_light_rays.mp4` / `lines_of_green_lights_move_in_waves.mp4` / `blue_black_vertical_shining_beam.mp4`**: H.264 video loops for screen calibration and signage testing.

### 📁 `04_Presentations_&_Scripts/`
Slide decks, presenter notes, and scripts.
* 📁 **`av_funny_presentation/`**: Slides and scripts for a humorous AV-themed presentation.
* 📁 **`av_tech_run_though_PPTX/`**: Technical rehearsal slides and script.
* 📄 **`Presentation Example.pdf`**: Sample PDF presentation.

### 📁 `05_Docs_&_Checklists/`
Checklists, troubleshooting guides, and diagnostic scripts.
* 📄 **`Convention Center AV Equipment Checklist.pdf`**: Venue AV reference document.
* 📄 **`footage_eula.pdf`**: End User License Agreement for video assets.
* 📄 **`edid_hdmi_troubleshooting.md`**: Troubleshooting guide for EDID, HDCP, and display flickering.
* 📄 **`networked_av_guide.md`**: Configuration guide for Dante and AV-over-IP network switches.
* 📄 **`mtr_zoom_rooms_daily_check.md`**: Daily checklist for Microsoft Teams Rooms and Zoom Rooms.
* 📁 **`Zoom_Teams_Meet_Guides/`**: Reference manuals and platform guides for boardrooms and hybrid events:
  * 📄 [general_hybrid_meeting_room_av_guide.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/general_hybrid_meeting_room_av_guide.md): Reference manual for hybrid meeting room AV systems.
  * 📄 [hybrid_meeting_room_guide_for_zoom.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/hybrid_meeting_room_guide_for_zoom.md): Zoom Rooms hybrid setup and operation.
  * 📄 [hybrid_meeting_room_guide_for_teams.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/hybrid_meeting_room_guide_for_teams.md): Microsoft Teams Rooms operational guide.
  * 📄 [hybrid_meeting_room_guide_for_google_meet.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/hybrid_meeting_room_guide_for_google_meet.md): Google Meet hardware and room guide.
  * 📄 [zoom_hybrid_setup_guide.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/zoom_hybrid_setup_guide.md): Advanced configurations for hybrid Zoom events.
  * 📄 [zoom_foh_operator_cheat_sheet.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/05_Docs_&_Checklists/Zoom_Teams_Meet_Guides/zoom_foh_operator_cheat_sheet.md): Quick reference for front-of-house operators.
* ⚙️ **`av_hardware_diagnostics.py`**: Python script to verify local audio sample rates and hardware devices.
* ⚙️ **`display_diagnostics.py`**: Python script to query connected displays and read EDID profiles.
* ⚙️ **`network_av_diagnostics.py`**: Python script to measure network latency, packet loss, and jitter.
* ⚙️ **`generate_toolkit.py`**: Python script used to generate the test signals and patterns.
* ⚙️ **`optimize_toolkit.py`**: Automation script for toolkit compression and cleanup.

---

## 🎥 AV Sync & Lip-Sync Latency Test

### Context
In hybrid meeting environments, audio and video travel through separate signal chains:
* **Audio**: Mics ➡️ DSP (Biamp/Q-SYS) ➡️ USB Bridge ➡️ Computer ➡️ Zoom/Teams.
* **Video**: Camera ➡️ USB Grabber ➡️ Computer ➡️ Zoom/Teams.
Since DSP audio processing takes time, audio can be delayed relative to video.

### How to use `01_Audio_&_Sync/video_01_av_sync_latency_test.mp4`
1. Play the video on the room display with audio routed to the room speakers.
2. Record the display and speaker output using a phone camera (30 or 60 fps).
3. Import the recording into a video editor or open it in **VLC Media Player**.
4. In VLC, press **`E`** to step frame-by-frame:
   * **In Sync**: The audio tone plays when the screen flashes teal and the red bar is on the center **0 ms (SYNC)** line.
   * **Audio Delayed**: The tone plays when the red bar is on the **RIGHT (+)** side. If it aligns at `+100 ms`, delay the video by 100ms or reduce DSP latency.
   * **Video Delayed**: The tone plays when the red bar is on the **LEFT (-)** side. If it aligns at `-200 ms`, add 200ms of audio delay in the room DSP.

---

## 💻 Screen Share Quality Testing

Video codecs compress high-frequency details during screen sharing. Use `02_Display_Calibration/image_02_screen_share_legibility.png` to check legibility on the remote side:

1. **Start a test call** between the conference room PC and a remote client.
2. **Share the screen** displaying `02_Display_Calibration/image_02_screen_share_legibility.png`.
3. **Compare settings**:
   * **Default Share**: Optimized for static text; slides with animations or videos will drop frames.
   * **Optimize for video clip**: Increases frame rate but lowers resolution and subsamples colors (4:2:0).
4. **On the remote client, check**:
   * **Red-on-Black Text**: Verify that red text on a black background is legible. If not, avoid red-on-black or red-on-blue combinations in slide designs.
   * **Small Text**: Read down the font sizes. Blurry 6pt or 8pt text indicates downscaling.
   * **Moiré Patterns**: Moving patterns in the concentric circles indicate scaling distortion.

---

## 📋 Pre-Event Technician Checklist

Perform this walkthrough 60–90 minutes before a presentation or event.

### 1. Physical Room Check
* [ ] **Sightlines**: Check the main display and confidence monitor visibility from all seating areas.
* [ ] **Cabling**: Secure all floor cables with gaffer tape or covers to eliminate trip hazards.
* [ ] **Podium**: Clear clutter and ensure presenter water is placed away from electronics.
* [ ] **Clicker**: Install fresh batteries in the presenter remote and verify range from the stage.

### 2. Audio & Microphones
* [ ] **Reference Level**: Play `01_Audio_&_Sync/audio_01_ref_1khz_tone.wav` to verify signal flow and gain structure.
* [ ] **Wireless Mics**: Verify battery levels (minimum 2 bars) and walk the room to check for dropouts or RF interference.
* [ ] **Lapel Mics**: Clip lapel microphones at sternum level, clear of clothing or jewelry.
* [ ] **Feedback Prevention**: Test microphones in front of the room speakers. Adjust DSP feedback suppressors or reduce gain in the 1 kHz–4 kHz range if ringing occurs.
* [ ] **Vibration Check**: Play `01_Audio_&_Sync/audio_03_frequency_sweep_20hz_20khz.wav` at operating volume. Ensure ceiling grids and fixtures do not rattle.

### 3. Display & Video
* [ ] **Alignment**: Open `02_Display_Calibration/image_01_display_convergence.png` to verify full screen coverage, aspect ratio, and focus.
* [ ] **Inputs**: Test connections (HDMI, USB-C) directly from the presenter's laptop using the provided cables.
* [ ] **Confidence Monitor**: Set the floor monitor to Presenter View (notes and clock) rather than screen mirroring.

### 4. Presentation Laptop
* [ ] **Power**: Connect the laptop to AC power.
* [ ] **Notifications**: Enable Do Not Disturb / Focus Assist to silence system alerts.
* [ ] **Audio Routing**: Play a video to confirm audio routes through the room sound system, not the laptop speakers.
* [ ] **Power Settings**: Disable sleep mode and screensavers.

### 5. Remote / Hybrid Check
* [ ] **Echo Test**: Join a test call, speak from the room, and listen from the remote side to verify acoustic echo cancellation (AEC).
* [ ] **Legibility**: Share `02_Display_Calibration/image_02_screen_share_legibility.png` and verify readability on the remote receiver.
* [ ] **AV Sync**: Play `01_Audio_&_Sync/video_01_av_sync_latency_test.mp4` on the call to verify alignment.
* [ ] **Virtual Backgrounds**: If using background keying, ensure the computer has sufficient hardware capacity to render it without video stutter.

---

## 📄 License & Disclaimer

This project is licensed under the MIT License - see the [LICENSE](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/LICENSE) file for details.
For the End User License Agreement (EULA) and operational warnings, please refer to the [DISCLAIMER.md](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/DISCLAIMER.md) file.

---

*Toolkit compiled & generated on: 2026-06-13*
