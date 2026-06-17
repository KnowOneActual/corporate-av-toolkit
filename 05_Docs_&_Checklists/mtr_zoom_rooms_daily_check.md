# 📋 Teams & Zoom Rooms Daily System Walkthrough

This checklist should be executed daily (usually 30–60 minutes before the first meeting of the day) to ensure Microsoft Teams Rooms (MTR) and Zoom Rooms hardware, tablets, and audio/video bridges are fully functional.

---

## 📱 Phase 1: Controller Tablet & Console Check

The tabletop controller (Logitech Tap, Crestron Flex, Poly TC8, Neat Pad) is the primary user interface.

- [ ] **Physical Check**: Ensure the screen is clean, free of smudges, and the cable strain relief is secure.
- [ ] **Power & Charging**: Verify the tablet is powered and charging. (If powered over PoE, check that the PoE injector indicator light is green).
- [ ] **Connection Status**:
  * **MTR**: Verify the screen shows the default room calendar with no "MTR Service Not Responding" or yellow caution banners.
  * **Zoom Rooms**: Confirm the tablet shows the "New Meeting / Join / Share" screen and is paired with the room PC.
- [ ] **Time Sync**: Verify the time displayed on the tablet matches your smartphone/local time exactly. Out-of-sync clocks will block calendar invite integration.

---

## 🎙️ Phase 2: Room Audio System Verification

Audio failure is the most common reason meetings are disrupted.

- [ ] **DSP Online Check**: Verify the room's DSP (Biamp Tesira, Q-SYS Core, Shure Intellimix) is powered on and shows normal status lights.
- [ ] **Microphone Mute Sync**: 
  * Tap the **Mute** button on the tablet controller.
  * Verify that physical microphone LEDs in the room (ceiling arrays, table pucks) turn **Red** (muted).
  * Tap **Unmute** on the tablet and verify the LEDs turn **Green/Blue** (unmuted).
  * *If they do not sync, the USB control bridge between the DSP and room PC is disconnected.*
- [ ] **Speaker Path Test**:
  * On the tablet controller, go to **Settings ➡️ Audio**.
  * Trigger the "Test Speaker" or ringtone sound.
  * Walk the room to ensure audio is clear and coming out of all speakers (no crackling, dead channels, or volume drops).

---

## 📷 Phase 3: Video & Camera Framing Check

- [ ] **Camera Feed Verification**:
  * Tap the **Camera Control** menu on the controller tablet.
  * Verify you see a live preview of the empty conference room on the console/monitor.
- [ ] **Pan-Tilt-Zoom (PTZ) Test**:
  * Manually pan the camera left, right, up, and down.
  * Verify the camera movements are smooth and silent.
- [ ] **Preset Check**:
  * Tap the preset buttons (e.g., "Podium", "Whiteboard", "Full Room").
  * Verify the camera returns to the correct coordinates and focus positions.
- [ ] **Auto-Framing/Group Tracking**:
  * If the room uses AI framing (e.g., Logitech RightSight, Neat Symmetry), step into the frame and verify the camera zooms in on you automatically.

---

## 💻 Phase 4: Host PC & Cable Harness Check

- [ ] **System Reboot (Recommended Weekly/Daily)**:
  * Perform a soft reboot of the room PC from the tablet console or via remote management. This clears RAM cache, resets USB port hubs, and updates system services.
- [ ] **Cable Tether Check**:
  * Verify the HDMI/USB-C cables on the table (for laptop screen sharing) are in good condition.
  * Verify the cable retractors (if installed) pull back smoothly without binding.
- [ ] **Display Power Sync**:
  * Confirm that turning on/rebooting the system triggers the displays to wake up via CEC or RS232 controls.

---

## 🚨 Troubleshooting Common Room Failures

| Symptom | Probable Cause | Immediate Action |
| :--- | :--- | :--- |
| **"Device Disconnected" Warning** | USB device went into power-save mode. | Unplug the camera/mic USB cable from the room PC, wait 5 seconds, and re-insert. Disable "USB Selective Suspend" in Windows Power Settings. |
| **Console out of sync with TV** | Display scaling mismatch or resolution override. | Reboot the room PC. If MTR, check that the display HDMI is plugged into the primary HDMI port, not secondary. |
| **Echo heard by remote participants** | Echo Cancellation (AEC) bypassed. | Ensure the room PC audio settings are set to **"Room DSP"** or **"Echo Cancelling Speakerphone"**, and NOT the raw motherboard outputs. |
| **Camera feed is black** | Camera lens cap on, or USB bandwidth exceeded. | Ensure no other USB devices are daisy-chained on the same hub as the camera. Cameras require dedicated USB bandwidth. |
