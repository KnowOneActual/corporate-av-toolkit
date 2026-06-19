# Hybrid Meeting Room Guide for Google Meet

## FOH Control, Presentation Playback, and Q&A Management

This guide covers how to set up, operate, and troubleshoot a hybrid conference room that uses Google Meet with in-person participants, in-room presenters, and remote attendees.

> [!info] Site-Specific Infrastructure
> Update this section with your local room details before an event.
> * **Audio DSP IP / Access:** [Insert IP address / Web interface link]
> * **USB Capture Interface:** [Insert Hardware ID / Device Name]
> * **Video Switcher IP / Access:** [Insert IP address / Web interface link]
> * **FOH Service Account:** [Insert Google Workspace host account]
> * **AV Support Hotline:** [Insert contact number]

---

## 1. Interactive Operator Checklists

Copy this checklist for each event to track completion.

### Pre-Flight Checklist

* [ ] Log into the FOH Host PC with the dedicated corporate Google Workspace account.
* [ ] Verify the FOH PC audio settings map exactly to the hardware DSP via USB.
* [ ] Disable "Noise cancellation" in Google Meet settings if using a hardware DSP to prevent processing conflicts.
* [ ] Join a second operator PC to the meeting as an auditor with noise-isolating headphones.
* [ ] Join the auditor PC using Companion Mode.
* [ ] Verify the hardware DSP mix sounds clear to the remote auditor.
* [ ] Test the video switcher to ensure it pushes the correct camera angles.

### Show Start Checklist

* [ ] Display a corporate holding slide by presenting a clean Chrome tab or window to the room and broadcast feed.
* [ ] Have a Co-host monitor the knocking queue and admit approved external guests.
* [ ] Verify all in-person attendees opening laptops use Companion Mode to join the meeting.
* [ ] Turn on live transcription or captions if required.
* [ ] Start the cloud recording.

### Show Run Checklist

* [ ] Use the Google Meet "Pin" or "Co-host spotlight" controls to fix presenter video feeds for the room display.
* [ ] Monitor the raised hands queue and text chat continuously during the broadcast.
* [ ] Ensure in-person attendees speak directly into a routed wireless microphone when asking questions.

---

## 2. Google Workspace Account, Licensing, and Security

Configure security defaults at the Google Workspace Admin console level to enforce consistency.

### Licensing Requirements

* Use Google Workspace Enterprise (Standard or Plus) host accounts to support large participant caps, advanced moderation features, and extended meeting durations.
* Equip accounts with Gemini for Google Workspace licenses to use automated meeting tools like "Take notes for me."
* Assign dedicated Google Meet Hardware licenses if using native room kits (such as ASUS, Logitech, or Avocor systems).

### Host Safety Controls

* **Quick Access and Meet Safety:** Toggle "Quick Access" off for high-stakes events. This forces all external participants and non-invited users to request access before entering.
* **Co-host Delegation:** Assign co-hosts preemptively or during the live call to share management tasks like muting, admitting guests, and text moderation.
* **Shared Management Limits:** Restrict the "Share their screen" and "Send chat messages" toggles under Host Controls if you need a locked-down broadcast style.

---

## 3. Google Meet Audio and Echo Cancellation with Hardware DSP

Google Meet features built-in, cloud-based AI noise cancellation. When stacked on top of a professional hardware DSP, it can cause voices to sound cut off or heavily gated.

> [!caution] Feedback Loop Risk
> Any laptop or phone in the room that joins with active audio will bypass the hardware DSP and trigger a feedback loop. FOH operators must confirm that all in-room devices join via Companion Mode.

### Audio Settings and Setup

* **Hardware Interoperability:** Select your USB audio interface (such as Extron, Q-Sys, or Biamp) as the primary Input and Output device inside Google Meet’s Audio Settings.
* **Software DSP Bypass:** Navigate to Settings -> Audio and turn off "Noise cancellation." This allows your high-end room hardware to handle 100% of the acoustic echo cancellation (AEC) and filtering without interference.

### DSP Routing Rules

* Route all in-room microphones to the local amplifier and to the USB transmitter bus connected to the FOH PC.
* Route the Google Meet far-end audio to the room speakers and the DSP's Acoustic Echo Cancellation (AEC) reference input. Do not route the far-end feed back into the USB transmitter bus.

---

## 4. Video, Screen Layouts, and Room Routing

Visual layouts must keep remote attendees visible on local room displays and presentation slides visible on both feeds.

### Layout Reference Guide

| Layout Mode | Ideal Environment | Screen Setup | Operator Action |
| --- | --- | --- | --- |
| **Companion Mode** | BYOD & In-Room Audience | Personal Secondary Laptops | Users go to `g.co/companion`. Joins the meeting completely audio-free. Allows participation in chat, polls, and hand raises without audio loops. |
| **Tiled and Spotlight** | Multi-Participant Rooms | FOH Control & Projector | Select "Tiled" layout and scale the tile count slider up to 49. Pin active presenters to fix them onto the physical room display. |
| **Tab Presenting** | High-Stakes Slides & Media | Dual FOH Monitors | Select "Present a Chrome tab" instead of the entire screen. This prioritizes high-frame-rate video and clear audio transmission. |

> [!tip] Presenting from Google Workspace Apps
> Presenters on the Podium PC can open their Google Slides or Docs file directly in Chrome and click the built-in "Present to Meet" icon. This shares the file into the active call without requiring the presenter to manage browser windows.

---

## 5. Google Meet Roles

Assign these roles to distribute administrative controls during the meeting.

* **Host:** The account that created the Calendar event or initiated the Meet link. Holds ultimate control over safety settings, recording, and co-host assignments.
* **Co-hosts:** Staff promoted during the meeting. They share administrative powers, including the ability to mute participants, eject disruptive users, and accept lobby knocks.
* **Participants:** Standard attendees. They can speak, turn on video, and share screens unless restricted by the host's safety settings.

---

## 6. Troubleshooting Diagnostics

| Symptom | Root Cause | Operator Fix |
| --- | --- | --- |
| **Severe Audio Echo** | An in-room laptop or phone joined with active audio enabled. | Scan the participant list for active volume indicators. Mute the user or eject them. Instruct them to rejoin via `g.co/companion`. |
| **Robotic, Fading Room Audio** | Google Meet's built-in noise cancellation is fighting the hardware DSP. | Open Meet Audio Settings and turn off "Noise cancellation." |
| **FOH Control UI Visible on Projector** | The FOH Host PC is using duplicate display settings in the OS. | Switch OS display settings to "Extend." Move the clean Meet video stage window to Monitor 2 (Projector) and keep the control panels on Monitor 1. |
| **Laggy Slide Video or Audio Playback** | The operator shared their entire desktop instead of an isolated browser tab. | Stop sharing. Re-share using the "Present a Chrome tab" option to improve video performance and pass audio. |

---

## 7. Recording, Transcripts, and Governance

### Storage and Access Controls

Google Meet recordings and automated text transcripts are generated directly in the cloud. Once the meeting concludes, these files are automatically saved into the Primary Host’s Google Drive in a folder named "Meet Recordings." The host will also receive an email with direct links to the files. Access control is maintained entirely through Google Drive file permissions.

### Automated Documentation

If your workspace uses Gemini enterprise features, you can activate tools like "Take notes for me." This creates a running summary of the event in a Google Doc without requiring manual typing from your moderation team. Ensure this is initialized during the show start sequence.
