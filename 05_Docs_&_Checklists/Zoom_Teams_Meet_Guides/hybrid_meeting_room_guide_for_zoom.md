# Hybrid Meeting Room Guide for Zoom  
## FOH Control, Presentation Playback, and Q&A Management

This guide covers how to set up, operate, and troubleshoot a hybrid conference room that uses **Zoom Meetings** with in‑room participants, in‑room presenters, and remote participants.

It assumes:

- A hardware **audio DSP** (e.g., Extron DMP, Q‑Sys, Biamp) with mix‑minus and AEC.
- A **video switcher / matrix** feeding the projector, confidence monitor, and a USB capture path.
- A **Front of House (FOH) Zoom host PC**.
- A **Podium PC** for slide playback and screen sharing.
- One or more **handheld/wireless Q&A mics** for the audience.

---

## 1. Zoom Account, Licensing, and Security

For corporate environments, you typically want centrally managed account settings and locked defaults.

### 1.1 Licensing and Features

- Use **licensed Zoom accounts** for hosts so meetings aren't time‑limited and can support required participant counts.
- Enable **Cloud Recording** or **local recording** as appropriate to your corporate policy.
- For internal meetings, consider enabling **"Only authenticated users can join"** with SSO or corporate email domains.

### 1.2 Security Defaults (Admin / Account Level)

Recommended defaults for corporate hybrid rooms:

- Require **meeting passcodes** for all meeting types and enforce passcode complexity.
- Require at least one: **Passcode**, **Waiting Room**, or **Only authenticated users can join** for every meeting.
- Disable or strongly discourage use of **Personal Meeting ID (PMI)** for public or external events; use generated meeting IDs.
- Enable **Waiting Room** for external‑facing events so FOH can vet participants.
- Disable **Join before host** for corporate hybrid rooms to avoid unmoderated pre‑meeting chaos.
- Default **Screen Sharing** to **Host only**; allow FOH to selectively enable sharing for participants or co‑hosts.

These should be configured under **Account Settings → Meeting tab** and locked at the account or group level for rooms.

---

## 2. Zoom Audio with Hardware DSP (Mix‑Minus + AEC)

### 2.1 FOH Host PC Audio Settings

On the FOH Zoom host PC:

1. Open **Zoom → Settings → Audio**.
2. Set **Microphone** to your **USB audio interface / DSP send** (e.g., "Extron USB Audio," "USB Audio CODEC").
3. Set **Speaker** to the **same interface** so all remote audio flows through the DSP.

Click **Advanced** at the bottom:

- Set **Echo cancellation** to **Auto** (or Low) when using a well‑configured hardware DSP so Zoom's echo canceller doesn't fight the DSP.
- Avoid "**Original sound for musicians**" for room mics unless you are deliberately bypassing Zoom processing for a specific reason.

### 2.2 DSP Routing Summary

In the DSP:

- Route **Podium Mic** and **Q&A mics** to:
  - Room speakers output (amplifier).
  - Zoom TX bus (USB send).

- Route **Zoom RX input** (from FOH PC via USB) to:
  - Room speakers output.
  - AEC reference.
  - **Not** to Zoom TX (mix‑minus).

Zoom's "Auto/Low" echo cancellation plus DSP‑side AEC yields stable, echo‑free audio when configured properly.

### 2.3 Podium PC Audio Rules

For **dual‑PC architecture**:

- Podium PC joins Zoom, then immediately selects **"Leave Computer Audio"**.
- Confirm there's no mic icon; it should show **Join Audio**.
- Set OS system volume to 0% as a second safeguard.

For **single‑PC rooms** (not recommended for larger corporate events), that PC must be the audio host and you do **not** use "Leave Computer Audio"; all room audio flows through that machine and the DSP.

---

## 3. Zoom Video, Screen Layout, and Room Routing

### 3.1 FOH Dual‑Monitor Configuration

On FOH host PC:

1. In Zoom, go to **Settings → General** and enable **Use dual monitors**.
2. Configure OS displays as **Extended desktop**.
3. Use:
   - **Monitor 1** (FOH control screen): Zoom UI, chat, participants, Statistics, etc.
   - **Monitor 2**: full‑screen Zoom video (spotlighted speaker/gallery) feeding the switcher input via HDMI.

This lets FOH manage the meeting without affecting what the room sees.

### 3.2 Camera and Content Feeds

- Set **Zoom Camera** to the **USB capture device** connected to the switcher output; whatever is routed to that output becomes the Zoom camera feed.
- To send **slides**:
  - Podium PC shares its slide show via Zoom **Share Screen**.
  - Switcher routes podium HDMI to projector and confidence monitor as needed.

Zoom's full‑screen output on FOH is what you route to the projector for remote speakers and hybrid galleries.

---

## 4. Zoom Roles: Host, Co‑host, Moderator, Shadow

### 4.1 Recommended Roles

- **Host (FOH)**
  Controls security, Waiting Room, spotlighting/pinning, and recording.

- **Co‑hosts**
  - Podium PC (for frictionless screen sharing).
  - Remote presenters (for self‑control of mute/video and sharing).

- **Zoom Moderator**
  Watches chat, raised hands, and Q&A (webinar) to ensure remote participants are heard.

- **Shadow PC Auditor**
  Joins from separate machine with muted mic and headphones to verify remote experience; communicates with FOH via intercom or back‑channel chat.

Guides from Zoom and higher‑ed emphasize having a dedicated moderator to support remote attendees in hybrid meetings.

---

## 5. Zoom Meeting Workflow for Hybrid Rooms

### 5.1 Before the Meeting

- Schedule from a **corporate host account** with correct security defaults (passcode + Waiting Room or authenticated users).
- In invitations, instruct remote attendees to:
  - Prefer **wired Ethernet** over weak Wi‑Fi.
  - Use headsets or quality mics and stay muted when not speaking.
- Run a **tech rehearsal** with at least one remote participant and one in‑room participant to validate AV and screen sharing.

### 5.2 Meeting Start

1. FOH host starts the Zoom meeting and confirms recording status.
2. Shadow PC joins; verify audio/video.
3. Admit podium PC; assign **Co‑host**.
4. On podium PC:
   - Join Zoom.
   - Immediately **Leave Computer Audio**.
5. FOH may share a holding slide ("Welcome") while participants join.

### 5.3 During the Meeting

- Use **Spotlight** to control what everyone sees and what goes to the projector and recording.
- For Q&A, use multi‑spotlight (remote presenter + room PTZ camera) so remote attendees see both sides.
- Moderator monitors **chat** and **raised hands** and alternates between in‑room and remote questions.
- In‑room laptops/phones that join Zoom should stay **muted** and ideally **Leave Computer Audio** to avoid echo.

---

## 6. Zoom‑Specific Best Practices, Tips, and Tricks

### 6.1 Hybrid Experience and Meeting Culture

- Ask remote attendees to **rename** themselves with full name and role (e.g., "Alex – Remote – Sales").
- Open by **acknowledging remote participants** and confirming they can hear and see.
- Encourage use of **Reactions** and **Raise Hand**; moderator uses these to manage turns.
- Explicitly alternate between in‑room hands and Zoom raised hands during Q&A.

### 6.2 Security and “Zoom‑bombing” Protection

For external or high‑risk events:

- Don't publish Zoom links publicly; distribute by email or secure channels.
- Use generated meeting IDs (not PMI).
- Require passcodes and/or Waiting Room.
- Lock the meeting once all expected participants have joined.
- Use **Remove** and optional **Report** for disruptive attendees.

### 6.3 Echo and Feedback Tips

- Only **one Zoom device** in the physical room should have active audio (FOH host) unless you have a carefully managed second path through DSP.
- Extra devices used as secondary cameras should **Disconnect Audio** via Zoom app.
- If echo appears:
  - Check for additional in‑room devices with mic+speaker active and mute/Disconnect Audio.
  - In Audio → Advanced, you can temporarily increase echo cancellation aggressiveness for emergency mitigation if DSP is minimal.

Zoom's documentation notes most echo cases are caused by multiple devices in the same room joined to audio.

### 6.4 Layout and Pinning Tricks for FOH

- Use **Pin** locally on FOH to monitor specific feeds without changing what attendees see.
- Use **Spotlight** for what should be on projector and in recordings.
- On the projector or confidence monitor, arrange **gallery view** so remote participants are prominent and clearly visible to the room.

### 6.5 Rehearsal and Backup Plans

- Always run a **5–10 minute pre‑flight** with FOH, podium, and at least one remote participant:
  - Verify slides, room camera, remote camera, Q&A mic, and recording.
- Assign a **backup host** (co‑host) to take over if FOH PC fails.
- Have a **simple fallback** path: direct webcam and USB speaker/mic on a single PC if the bigger system fails.

---

## 7. Zoom‑Tailored Troubleshooting Snippets

### 7.1 Remote Participants Hear Echo

- Look for any in‑room laptop/phone joined with active mic and speakers; mute or **Leave Computer Audio**.
- Confirm only FOH PC is joined to audio and DSP mix‑minus is correct.

### 7.2 Presenter Cannot Share Screen from Podium

- Ensure presenter/podium PC is a **Co‑host**.
- On macOS, verify **System Settings → Privacy & Security → Screen Recording** allows Zoom.

### 7.3 Remote Participants See Black Screen Instead of Slides

- Confirm podium PC is sharing the **Slide Show window**, not just the editor or wrong monitor.
- Close any DRM‑protected content that could trigger HDCP blackouts.

---

## 8. Recording in Zoom (FOH Summary)

- Choose **local recording** for higher‑quality, operator‑controlled room recordings; choose **cloud** if you need easy sharing and multiple layouts.
- Configure Recording settings so you capture both **speaker video and shared screen** in useful layouts.
- Start recording a few seconds before content begins and let it run through the end; trim later.
- After the meeting, move local recordings to a **shared, backed‑up archive** and apply your organization's retention policy; manage cloud recordings similarly in the Zoom web portal.