# Hybrid Meeting Room Guide for Microsoft Teams

## FOH Control, Presentation Playback, and Q&A Management

This guide covers how to set up, operate, and troubleshoot a hybrid conference room that uses Microsoft Teams with in-person participants, in-room presenters, and remote attendees.

> [!info] Site-Specific Infrastructure
> Update this section with your local room details before an event.
> * **Audio DSP IP / Access:** [Insert IP address / Web interface link]
> * **USB Capture Interface:** [Insert Hardware ID / Device Name]
> * **Video Switcher IP / Access:** [Insert IP address / Web interface link]
> * **FOH Service Account:** [Insert Teams meeting host account]
> * **AV Support Hotline:** [Insert contact number]

---

## 1. Interactive Operator Checklists

Copy this checklist for each event to track completion.

### Phase 1: Pre-Flight Sequence

* [ ] Log into the FOH Host PC with the dedicated corporate service account.
* [ ] Verify the FOH PC audio settings map exactly to the hardware DSP via USB.
* [ ] Enable "High-Fidelity Music Mode" in Teams device settings if using an uncertified hardware DSP.
* [ ] Join a second operator PC to the meeting as an auditor with noise-isolating headphones.
* [ ] Join the auditor PC using the "Don't use audio" option.
* [ ] Verify the hardware DSP mix sounds clear to the remote auditor.
* [ ] Test the video switcher to ensure it pushes the correct camera angles.

### Phase 2: Show Start Sequence

* [ ] Display a corporate holding slide via PowerPoint Live to the room and broadcast feed.
* [ ] Have a Co-organizer monitor the lobby and admit approved guests.
* [ ] Verify all in-person attendees opening laptops select the "Don't use audio" option.
* [ ] Turn on live transcription.
* [ ] Start the recording.

### Phase 3: Show Run Sequence

* [ ] Use the Teams "Spotlight" feature to force presenter video feeds to the main stage.
* [ ] Switch to "Multi-spotlight" during Q&A to frame the remote speaker and physical room camera side-by-side.
* [ ] Ensure in-person attendees speak directly into a routed wireless microphone when asking questions.

---

## 2. Teams Account, Licensing, and Security

FOH host accounts must be centrally managed through the corporate directory.

### Licensing Requirements

* FOH host accounts require enterprise-grade licenses (such as Office 365 E3 or E5) to support large meetings.
* Teams Premium is required for custom corporate lobbies, end-to-end encryption, and custom watermarking.
* Assign Microsoft 365 Copilot or Teams Premium licenses to access post-meeting transcripts and the AI-generated Intelligent Recap.

### Pre-Join Security Defaults

* Set "Who can bypass the lobby?" to "People in my organization" to prevent unvetted external access.
* Set "Who can present" to "Only organizers and co-organizers" to block attendees from sharing their screens.
* Enable "Manage what attendees see" to restrict the display to shared content and spotlighted video feeds. This setting automatically disables attendee microphones and cameras.
* Turn on "Green room" to give presenters a private space to test audio before the meeting starts.

---

## 3. Teams Audio and Echo Cancellation with Hardware DSP

Microsoft Teams uses cloud-driven echo cancellation & noise suppression. These settings will clash with your hardware DSP and distort audio unless they are disabled.

> [!caution] Feedback Loop Risk
> Any laptop or phone in the room that joins with active audio will bypass the hardware DSP and trigger a feedback loop. FOH operators must confirm that all in-room devices join via the "Don't use audio" option.

### Audio Settings and Setup

* **Certified Hardware:** Teams-certified DSPs automatically negotiate with the Teams client to disable software echo cancellation.
* **Uncertified Hardware:** For uncertified DSPs, enable "High-Fidelity Music Mode" in Teams settings. This option allows you to manually turn off Teams' built-in echo cancellation and noise suppression.

### DSP Routing Rules

* Route all in-room microphones to the local amplifier and to the USB transmitter bus connected to the FOH PC.
* Route the Teams far-end audio to the room speakers and the DSP's Acoustic Echo Cancellation (AEC) reference input. Do not route the far-end feed back into the USB transmitter bus.

---

## 4. Video, Screen Layouts, and Room Routing

Visual layouts must keep remote attendees visible in the room and presentation slides visible on both feeds.

### Layout Reference Guide

| Layout Mode | Ideal Environment | Screen Setup | Operator Action |
| --- | --- | --- | --- |
| **Front Row** | Dedicated MTR Boardrooms | Requires ultra-wide 21:9 or dual displays | Default layout. Puts remote video at the bottom of the screen to simulate eye contact. Places chat and raised hands on the sides. |
| **Shared Display** | BYOD Rooms | Standard 16:9 screen | Have the user select "Room Audio" when joining. This pushes the slides to the TV while keeping private desktop controls on the laptop. |
| **PowerPoint Live** | High-Stakes FOH Events | Dual FOH monitors | Launch PPT Live. Monitor 1 shows the private Presenter View. Monitor 2 feeds the clean slides to the room projector and remote audience. |

> [!tip] Spotlight and Pin Settings
> Use Spotlight to control what the remote audience sees and what gets recorded. Use Pin on your local FOH monitor to privately watch VIP feeds or specific camera angles without changing the global layout.

---

## 5. Teams Roles

Assign these four roles to manage the event flow.

* **Organizer:** Controls the meeting lifecycle, sets lobby policies, starts the recording, and assigns Co-organizers.
* **Co-organizers:** Adjust meeting settings during the event, manage breakout rooms, and change participant roles. They must belong to the internal domain.
* **Presenters:** Share audio, video, and slides via PowerPoint Live. They cannot modify security settings.
* **Attendees:** Read-only participants who are restricted to using chat, raising hands, and viewing content.

---

## 6. Troubleshooting Diagnostics

| Symptom | Root Cause | Operator Fix |
| --- | --- | --- |
| **Severe Audio Echo** | A secondary device in the room joined with active audio. | Identify the active green mic icon in the participant list. Force-mute them. Instruct the user to rejoin using "Don't use audio". |
| **Choppy or Gated Voice** | Teams is applying its cloud AEC on top of an uncertified hardware DSP. | Enable "High-Fidelity Music Mode" in the device settings to bypass the cloud processing. |
| **Presenter Notes on Projector** | The presenter is using duplicate screen mode. | Switch to PowerPoint Live to isolate the Presenter View from the audience view. |
| **Missing Slide Animations in Recording** | Slide animations are not captured in PowerPoint Live cloud recordings. | If complex motion graphics must be preserved in the archive, revert to standard full-screen desktop sharing. |

---

## 7. Recording, Transcription, and Governance

### Storage and Access Controls

Restrict transcript access to organizers to prevent unauthorized data sharing. Set "Who can record and transcribe" to "Organizers and co-organizers" to block attendees from downloading the text or feeding it into external tools. Ad-hoc meeting recordings save to the host organizer's OneDrive, while channel-based meetings save to the SharePoint site of the associated Team.

### Intelligent Recap and Copilot

* **Teams Premium:** Generates notes, task lists, and speaker timeline markers after the meeting concludes.
* **Microsoft 365 Copilot:** Serves as a real-time query engine during the meeting. Copilot requires live transcription to be enabled to answer questions about the event afterwards.
