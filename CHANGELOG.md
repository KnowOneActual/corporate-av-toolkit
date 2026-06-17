# Changelog

All notable changes to the Corporate AV Toolkit project are documented in this file.

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
