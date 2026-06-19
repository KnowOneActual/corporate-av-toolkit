# Changelog

All notable changes to the Corporate AV Toolkit project are documented in this file.

## [2.2.0] - 2026-06-19

### Added
- **AV Lip-Sync Latency Tester**:
  - Re-integrated the visual/audible latency offset sweep simulator into the calibration tools.
  - Features interactive audio offset settings ranging from -300ms to +300ms.
  - Configured HTML5 canvas sweeping animations with visual flash sweeps and markers.
  - Integrated a 1kHz audio click generator synced to the sweep.
  - Bound spacebar play/pause toggling when navigating the AV Sync section.
  - Updated keyboard navigation shortcut options (1-7 layout, adding 2 for AV Sync).
  - Wired state integration for local persistence and global stop checks.

## [2.1.3] - 2026-06-19

### Added
- **Advanced Speaker Delay Calculator Settings**:
  - Introduced an expandable **Advanced** settings panel to the Distance to Delay calculator to keep the interface simple by default.
  - Added an **Air Temperature** input field that dynamically links to the distance unit selector: Celsius (°C) for Meters (m) and Fahrenheit (°F) for Feet (ft), including automatic value conversion when units are changed.
  - Upgraded the speed of sound delay logic to calculate dynamically using temperature-based dry air sound speed formulas ($c = 331.3 \sqrt{1 + T_C / 273.15}$ for Celsius and $c = 49.02 \sqrt{459.67 + T_F}$ for Fahrenheit).

## [2.1.2] - 2026-06-19

### Added
- **Standby & Still Slide Generator Logo Options**:
  - Added a **Logo Option** selector with options for *Placeholder Logo*, *Upload Custom Logo...*, and *No Logo (Clean Slide)*.
  - Hides the custom logo file input element when not in use.
  - Added vertical text centering (offsetting position by `h * 0.15`) when no logo is displayed to produce clean, well-balanced slides.

### Changed
- **High-Visibility Safe Area Lines**:
  - Upgraded safe area boundaries and crosshairs to draw dual-tone lines (a black outline under a white core) to ensure perfect contrast against the leftmost white color bar stripe and all other colors.
  - Configured safe area coordinates to calculate dynamically based on canvas dimensions to scale correctly in inline, fullscreen, and downloaded modes.

## [2.1.1] - 2026-06-19

### Changed
- **Speaker Delay Calculator Usability**:
  - Simplified the speaker delay calculator by removing the manual speed of sound input.
  - Added a unit selector to toggle between Meters (m) and Feet (ft), dynamically applying standard speed of sound constants (343 m/s for meters, 1125 ft/s for feet) tailored for climate-controlled indoor spaces.

## [2.1.0] - 2026-06-19

### Added
- **Staging & Diagnostics Loops (60 FPS & 30 FPS)**:
  - `video_02_judder_refresh_rate_test.mp4`: A 60 FPS vertical movement bar test pattern designed to detect micro-stutter, frame drops, and V-Sync tearing on displays and LED walls.
  - `video_03_smpte_color_bars_moving.mp4`: A 30 FPS reference color bar pattern with a moving horizontal block (to identify signal freeze) and a 1 kHz sine reference tone at -20 dBFS.
- **Standby & Still Slide Generator (Logo/SNAFU)**:
  - Integrated an interactive canvas still slide generator into the offline Web Dashboard (`index.html`).
  - Added slide templates for *Generic Logo*, *Technical Difficulties*, *Session Starting*, *Intermission*, and *Q&A*.
  - Supports client logo uploads, custom titles/subtitles, solid/gradient backgrounds, and custom brand theme color pickers.
  - Generates and exports high-quality 1080p and 4K still PNG images for switcher Still Stores.
- **Pre-Generated Backup Stills**:
  - Rendered five standard 1080p STILL PNG images (`still_01_logo_placeholder.png` through `still_05_qa_session.png`) in `03_Looping_Video_Backgrounds/` for immediate on-site deployment.
  - Created `generate_backup_stills.py` to allow automated recompilation of the stills with custom adjustments.

## [2.0.0] - 2026-06-17

### Added
- **Browser-Native Fullscreen Calibration**:
  - Implemented a dedicated `#fullscreen-canvas-container` that scales to the exact monitor resolution.
  - Added a **Go Fullscreen** button (`#fullscreenPatternBtn`) in the visual controls.
  - Bound a `dblclick` event listener on the inline canvas for quick access to fullscreen and a `click` listener on the fullscreen canvas to exit.
  - Added keyboard controls inside fullscreen: cycle patterns using **Arrow keys / Spacebar**, or jump directly using keys **1-7**.
- **Solid Color Inspection Washes**:
  - **Solid White**: Added for projector brightness and lens shading uniformity checks.
  - **Solid Black**: Added for projector contrast levels and light leak audits.
  - **RGB Color Cycle**: Loop Red, Green, and Blue washes every 2 seconds to inspect LED screen subpixels.
- **Audio Synthesizers (Web Audio API)**:
  - **Speaker Line Check Synthesis**: Integrated direct routing and panning checks for Left, Right, Sub (60 Hz low-freq tone), Fill 1, Fill 2, and Lobby speakers.
  - **Speech Tuning Pink Noise**: Generates band-limited pink noise filtered through highpass (125 Hz) and lowpass (8 kHz) nodes.
  - **Sub/Low-End Check**: Generates sub-band pink noise filtered between 40 Hz and 100 Hz.
  - **Feedback Hunt Sweep**: Runs a continuous exponential frequency sweep from 500 Hz to 6 kHz repeating every 10 seconds.
  - **Live Audio Controls**: Added a Vol range slider and a global **Stop Audio** kill-switch.
- **Manual Signal Generator**:
  - Added a fourth subpanel with manual waveform selection (Sine, Triangle, Sawtooth, Square, Pink Noise).
  - Integrated a manual frequency slider (20 Hz - 20,000 Hz) and quick reference preset buttons (100 Hz, 440 Hz, 1 kHz, 10 kHz).
- **Screen Wake Lock API**:
  - Intercepts fullscreen modes and requests a display wake lock to prevent screensavers or sleep mode during projection convergence checks.
- **Local Storage State Persistence**:
  - Backs up profiles,checklist progress, show incident logs, and line check outputs to `localStorage` on any change, loading them automatically on page refresh.

### Fixed
- **Motion Test Grid Constraints**:
  - Changed the static column rendering loop to calculate columns dynamically based on `activeCanvas.width`.
  - Solved the bug where the motion bar pattern only covered 3/4 of the width on displays wider than 1280px.
- **Direct Fullscreen Motion Trigger**:
  - Configured the **Animate motion** button (`#animatePatternBtn`) to immediately select the motion bar pattern and launch it in fullscreen.
