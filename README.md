# 🛠️ Corporate AV Testing & Calibration Toolkit

An offline diagnostics suite for AV technicians, IT support teams, and event crews to verify, calibrate, and troubleshoot hardware systems in conference rooms, boardrooms, and hybrid meeting spaces.

---

## 🚀 Interactive Offline Dashboard (`index.html`)

The root `index.html` file launches a **self-contained web dashboard** that runs completely offline on any technician's laptop or in-room PC without installation.

### Included Utilities:
1. **Audio Waveform Generator**: Direct playback of sine, square, triangle, and sawtooth waves (20 Hz to 20 kHz), pink noise, white noise, and stereo channel routing checks.
2. **Speaker Phase Auditor**: Dynamic alternation between In-Phase and Out-of-Phase tones to verify physical speaker wiring polarity.
3. **AV Sync & Lip-Sync Sweep**: Canvas-based visualizer and synchronized audio beep to calibrate latency offsets.
4. **Calibration Patterns**: Fullscreen grids for aspect ratio alignment, SMPTE color bars, focus grids, pixel checks, and screen-share legibility charts.
5. **Hardware Input Monitor**: Live webcam feed checks and microphone decibel tracking via an animated VU meter.
6. **Compliance Checklists**: Offline MTR/Zoom Room and pre-event tech checklists that auto-save progress and export text logs.

---

## 📂 Folder Structure & Assets

### 📁 `01_Audio_&_Sync/`
Reference audio assets and synchronization checks.
* 🔊 **`audio_01_ref_1khz_tone.wav`**: Steady **1 kHz sine wave at -20 dBFS** (10s) to align input/output levels across DSPs, mixers, and amplifiers.
* 🔊 **`audio_02_stereo_channel_check.wav`**: Alternates pulses on the Left channel (0-4s), Right channel (4-8s), and both channels (8-12s) to verify speaker routing.
* 🔊 **`audio_03_frequency_sweep_20hz_20khz.wav`**: Logarithmic frequency sweep (15s) to detect ceiling grid rattles, acoustic drops, or hardware cabinet resonance.
* 🔊 **`audio_04_pink_noise_eq.wav`**: Voss-McCartney Pink Noise at -18 dBFS for Real-Time Analyzers (RTA) to measure frequency response and EQ room acoustics.
* 🔊 **`audio_05_phase_test.wav`**: Alternates pulsed tones between In-Phase and Out-of-Phase (180° inverted Right channel) to check physical speaker wiring.
* 🎥 **`video_01_av_sync_latency_test.mp4`**: 30 FPS sync video with a moving indicator and audio beep. Step frame-by-frame (VLC: `E`) to measure exact offset.

### 📁 `02_Display_Calibration/`
Visual reference patterns and slide decks.
* 🖼️ **`image_01_display_convergence.png`**: Grid pattern with central circle and corner crosshairs to audit aspect ratios and focus convergence.
* 🖼️ **`image_02_screen_share_legibility.png`**: Text sizes (6pt to 32pt), contrast boxes, and 1px/2px line grids to audit compression artifacts.
* 📊 **`ALIGN 16x9.pptx` / `16x9 SI TEST.pptx`**: Widescreen test slides.
* 🖼️ **`Black_blank_slide_1080.jpg` / `Curtis_Chart_RGB_8bit.jpg` / `PB2.png`**: Display calibration and convergence graphics.
* 📁 **`Legacy_PowerPoints/`**: Legacy calibration slides in `.ppt` format.

### 📁 `03_Looping_Video_Backgrounds/`
Video assets for projection mapping, signage, and virtual backgrounds.
* 🎥 **`CLEANROOM (loop).mp4` / `FLUFFF (loop).mp4`**: Ambient loops.
* 🎥 **`abstract_light_waves.mp4` / `blue_shining_stream_beam.mp4` / `golden_center_light_rays.mp4` / `lines_of_green_lights_move_in_waves.mp4` / `blue_black_vertical_shining_beam.mp4`**: Optimized H.264 video loops for screen testing and digital signage.

### 📁 `04_Presentations_&_Scripts/`
Corporate slide decks and teleprompter templates.
* 📁 **`av_funny_presentation/`**: PPTX slides, speaker notes, and scripts for an AV-themed humorous run-through.
* 📁 **`av_tech_run_though_PPTX/`**: Technical rehearsal slide deck.
* 📄 **`Presentation Example.pdf`**: Sample PDF presentation.

### 📁 `05_Docs_&_Checklists/`
Guides, checklists, and automated diagnostics.
* 📄 **`Convention Center AV Equipment Checklist.pdf`**: Venue AV reference document.
* 📄 **`footage_eula.pdf`**: License terms for video assets.
* 📄 **`edid_hdmi_troubleshooting.md`**: Step-by-step resolution guide for EDID mismatches, HDCP blocks, and screen flickering.
* 📄 **`networked_av_guide.md`**: Switch configuration and troubleshooting guide for Dante audio and AV-over-IP.
* 📄 **`mtr_zoom_rooms_daily_check.md`**: Operational walkthrough checklist for MTR and Zoom Rooms.
* ⚙️ **`av_hardware_diagnostics.py`**: Python script querying local audio inputs/outputs to verify 48 kHz sample rates.
* ⚙️ **`display_diagnostics.py`**: Python script parsing EDID profiles (manufacturer, screen size, serials) of connected displays.
* ⚙️ **`network_av_diagnostics.py`**: Python script measuring ping latency, packet loss, and jitter against conferencing thresholds.
* ⚙️ **`generate_toolkit.py`**: Script used to compile the audio and image calibration files.
* ⚙️ **`optimize_toolkit.py`**: Compression and cleanup utility.

---

## 🎥 AV Sync & Lip-Sync Latency Test

### Latency Context
Audio and video travel through separate hardware paths:
* **Audio**: Mic ➡️ DSP (Biamp/Q-SYS) ➡️ USB Bridge ➡️ PC.
* **Video**: Camera ➡️ USB Grabber ➡️ PC.
DSP processing (Acoustic Echo Cancellation, noise suppression) adds latency, often causing audio to lag behind video on calls.

### How to use `video_01_av_sync_latency_test.mp4`
1. Play the file on the in-room display and route audio to the room speakers.
2. Record the display and speaker output using a smartphone camera (at 30 or 60 FPS).
3. Import the recording to a video editor or open it in VLC Media Player.
4. Step frame-by-frame (VLC: `E`) to verify alignment:
   * **0 ms (SYNC)**: Beep aligns exactly with the teal flash and the center vertical line.
   * **Audio Lagging (Right / +)**: Beep occurs when the red indicator is on the right side of the track. Add video delay or reduce DSP buffer sizes.
   * **Video Lagging (Left / -)**: Beep occurs when the red indicator is on the left side of the track. Add audio delay in the DSP to match the display latency.

---

## 💻 Zoom / Microsoft Teams Screen Share Testing

Video conferencing codecs apply heavy compression to screen shares. Use `02_Display_Calibration/image_02_screen_share_legibility.png` to audit legibility on the far end:

1. Establish a test call between the room PC and a remote client.
2. Share the legibility image using standard screen sharing.
3. Verify the following on the remote client:
   * **Red-on-Black Contrast**: 4:2:0 chroma subsampling smudges red text on black. If unreadable, adjust presentation slide design.
   * **Small Font Legibility**: Read down to 6pt/8pt lines to verify scaling quality.
   * **Moiré Patterns**: Check concentric circle patterns for scaling artifacts and interpolation distortion.

---

## 📋 Pre-Event Technician Checklist

### 1. Physical Room Check
* [ ] **Sightlines**: Verify main display and confidence monitor visibility from corner and back seats.
* [ ] **Safety**: Secure all floor cables under gaffer tape or rubber cord protectors.
* [ ] **Podium**: Clear trash, clutter, and ensure water glasses are placed away from mics and laptops.
* [ ] **Clicker**: Install fresh batteries and test range from the stage corners.

### 2. Audio & Microphones
* [ ] **Gain Check**: Play `audio_01_ref_1khz_tone.wav` to establish reference DSP levels.
* [ ] **RF Mics**: Verify battery levels (replace if below 2 bars) and walk test room for dropouts or RF interference.
* [ ] **Lapel Mics**: Clip at sternum level, clear of loose collars, ties, or jewelry.
* [ ] **Feedback**: Step in front of speaker arrays with live mics to test DSP feedback suppressors.
* [ ] **Rattles**: Run `audio_03_frequency_sweep_20hz_20khz.wav` at house volume to identify ceiling grid vibrations.

### 3. Display & Video
* [ ] **Overscan**: Verify `image_01_display_convergence.png` fills the display boundaries without cropping.
* [ ] **Focus**: Confirm text legibility in all four display corners.
* [ ] **Dongles**: Test physical connections (HDMI, USB-C) from the presenter's laptop.
* [ ] **Presenter View**: Configure confidence monitors to show presenter view (slides + notes + timer) instead of mirroring.

### 4. Presentation PC Configuration
* [ ] **AC Power**: Verify presentation computers are connected to AC power (never battery).
* [ ] **Do Not Disturb**: Enable Focus Assist/DND to block system, email, and chat notifications.
* [ ] **Audio Routing**: Confirm slides with embedded videos route audio through the room system, not laptop speakers.
* [ ] **timeouts**: Disable sleep mode, screen locks, and screensavers.

### 5. Hybrid Call Verification (Far-End)
* [ ] **AEC Check**: Speak from various points in the room to confirm the DSP echo canceller is functioning without loopback.
* [ ] **Legibility**: Share `image_02_screen_share_legibility.png` and verify remote readability.
* [ ] **AV Sync**: Run `video_01_av_sync_latency_test.mp4` on the call to verify far-end lip-sync.

---

## ⚖️ Disclaimer & EULA

This toolkit is provided in good faith for testing, educational, and calibration purposes. 

**No Warranty or Guarantee:**
This software, including all audio generators, calibration images, video loops, scripts, and checklists, is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

*Always test audio sweeps and levels at low volumes first to prevent hearing damage or equipment overload.*

---

*Toolkit compiled & generated on: 2026-06-13*
