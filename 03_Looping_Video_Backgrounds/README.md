# 🎥 Looping Video Backgrounds & Staging Diagnostics

This directory contains video assets for live events, digital signage, and virtual backgrounds, alongside diagnostic video loops for calibrating projection systems, LED walls, and conference displays.

---

## 📂 File Directory

### 🎨 Background & Ambient Loops
* 🎬 **`CLEANROOM (loop).mp4`**: Subtle office backdrop for corporate virtual meetings.
* 🎬 **`FLUFFF (loop).mp4`**: Textured ambient abstract animation.
* 🎬 **`abstract_light_waves.mp4`**: H.264 smooth abstract wave loop.
* 🎬 **`blue_black_vertical_shining_beam.mp4`**: H.264 slow-moving vertical blue beam loop.
* 🎬 **`blue_shining_stream_beam.mp4`**: H.264 blue stream backdrop.
* 🎬 **`golden_center_light_rays.mp4`**: H.264 slow center light burst loop.
* 🎬 **`lines_of_green_lights_move_in_waves.mp4`**: H.264 green grid motion loop.
* 🎬 **`test_loop.webm`**: Lightweight WebM format check file.

### 🛠️ Diagnostic Calibration Loops
* 🎥 **`video_02_judder_refresh_rate_test.mp4`**: 60 FPS vertical movement test to analyze panel judder, refresh rates, and screen tearing.
* 🎥 **`video_03_smpte_color_bars_moving.mp4`**: 30 FPS color bar pattern with a moving reference block and a synchronized 1 kHz tone at -20 dBFS.

### 🖼️ Event Still / Standby Slides (1080p PNGs)
* 🖼️ **`still_01_logo_placeholder.png`**: Neutral client logo still slide for walk-in / walk-out.
* 🖼️ **`still_02_technical_difficulties.png`**: The classic SNAFU / "Technical Difficulties - Please Stand By" slide.
* 🖼️ **`still_03_session_starting.png`**: "Welcome - The Session Will Begin Shortly" slide.
* 🖼️ **`still_04_intermission.png`**: Intermission still slide to indicate ongoing breaks.
* 🖼️ **`still_05_qa_session.png`**: Q&A session slide to overlay or display during question periods.

---

## 📖 Staging & Calibration Instructions

### 1. Brightness & Contrast Calibration (PLUGE)
Use the bottom left of **`video_03_smpte_color_bars_moving.mp4`** to calibrate black levels on projectors or LED walls.
1. Open the video on the target display in full-screen.
2. Locate the three dark blocks on the bottom left:
   * **`-4% (BLOCKED)`** (RGB 4,4,4)
   * **`0% (REF BLACK)`** (RGB 16,16,16)
   * **`+4% (VISIBLE)`** (RGB 28,28,28)
3. Adjust the display's **Brightness** setting until the **`-4%`** block is completely invisible (blends into the 0% black background) and the **`+4%`** block is barely visible.
4. Adjust the display's **Contrast** setting using the white bars to maximize dynamic range without clipping bright details.

### 2. Video Freeze Verification
Video extenders (HDBaseT, AV-over-IP) and media servers can occasionally freeze on a single frame, making a technician think the signal is fine when the feed is actually dead.
* **Instruction**: The moving red block labeled with frame numbers in **`video_03_smpte_color_bars_moving.mp4`** bounces horizontally across the center. If this block stops moving, the video stream has frozen or crashed.

### 3. Display Refresh Rate & Judder Check
Use **`video_02_judder_refresh_rate_test.mp4`** to test rendering performance and V-Sync.
1. Play the video at native 60 FPS in full-screen.
2. Observe the red vertical bar as it slides across the grid.
3. **Troubleshooting**:
   * **Micro-Stutter / Hitching**: If the bar regularly stops or skips, the playback PC's CPU/GPU is bottlenecked or dropping frames.
   * **Screen Tearing**: If a horizontal line splits the red bar, V-Sync is disabled or the display's buffer is out of sync.
   * **Ghosting / Trails**: Excessive ghosting behind the bar on LED walls indicates slow pixel response times.

---

## ⚠️ Licensing & EULA

Usage of the pre-packaged video footage is subject to the End User License Agreement. Please review the [footage_eula.pdf](file:///Users/userx/github_repo/01_ACTIVE/corporate-av-toolkit/03_Looping_Video_Backgrounds/footage_eula.pdf) file in this directory for detailed constraints on corporate distribution and reuse.

---
