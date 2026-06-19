# Hybrid Meeting Room AV Guide  
## FOH Control, Presentation Playback, and Q&A Management

This guide explains how to set up, operate, and troubleshoot a professional hybrid meeting or event in a room with local audience, in‑room presenters, and remote participants on a video conferencing platform (Zoom, Microsoft Teams, Google Meet, etc.).

It assumes:

- A hardware **DSP** for audio (e.g., Extron DMP, Q‑Sys, Biamp).
- A **video switcher/matrix** for routing HDMI/SDI signals to screens and capture (e.g., Extron IN/INX/DXP, Kramer, Blackmagic ATEM).
- A **Front of House (FOH) computer** acting as the platform host and primary audio/video send/receive.
- A **Podium computer** for slide playback and screen sharing.
- One or more **handheld/wireless mics** for Q&A.

Brand names in this guide (Extron, Zoom, etc.) are examples; the concepts are the same for other vendors and platforms.

---

## 0. Quick Start Overview

### Roles

- **FOH Operator**
  Runs the conferencing platform host, controls the switcher and DSP, monitors audio/video, manages spotlighting/pinning, and records the session.

- **Podium Presenter**
  Runs the slide deck, shares screen to the meeting, and presents locally in the room.

- **Remote Presenter(s)**
  Join via the conferencing platform, are spotlighted for the room and remote audience, and interact with Q&A.

- **Shadow/Auditor PC (optional but recommended)**
  A separate device joined to the meeting solely to monitor what remote attendees see and hear.

### Typical Architectures

- **Single‑PC Setup**
  One computer in the room handles everything (host, slides, capture). Easier but higher risk and less flexible.

- **Dual‑PC Setup**
  FOH computer is host/AV hub; podium computer is just a participant for slides. Much safer and more controllable in corporate/event environments.

This guide assumes the **dual‑PC setup** as the default and calls out when a single‑PC setup behaves differently.

---

## 1. System Architecture and Signal Flow

Hybrid meeting rooms combine three main planes:

1. **Room plane** – Podium mic, handheld mics, speakers, projector/LED wall, confidence monitor.
2. **Platform plane** – The conferencing platform (Zoom/Teams/Meet) running on the FOH computer and optionally the podium computer.
3. **Bridge plane** – Hardware that glues them together: DSP, video switcher, USB bridge or capture card.

### Generic AV Signal Flow Diagram (Mermaid)

```mermaid
graph TD
    subgraph Stage_Area ["Stage & Audience Q&A"]
        PodiumPC["Podium PC<br/>(Slides & Screen Share)"]
        PodiumMic["Podium Mic<br/>(Local Presenter)"]
        HandheldMic["Handheld Q&A Mics<br/>(Audience Questions)"]
        ConfMonitor["Confidence Monitor<br/>(Switcher Output)"]
    end

    subgraph AV_Rack ["AV Processing Rack"]
        DSP["Audio DSP<br/>(Mix-Minus + AEC)"]
        Switcher["Video Switcher / Matrix"]
        PTZ_Cam["Room PTZ Camera"]
        RoomAmp["Amplifier & Room Speakers"]
        Projector["Main Room Screen<br/>(Projector / LED Wall)"]
    end

    subgraph FOH_Position ["FOH Control Position"]
        FOH_PC["FOH Control PC<br/>(Platform Host, Record, Mix)"]
        USB_Bridge["USB AV Interface<br/>(MediaPort / Capture Card)"]
        FOH_Monitor["FOH Monitor<br/>(Gallery / Stats / Tools)"]
    end

    subgraph Cloud ["Remote Participants"]
        PlatformCloud["Video Conferencing Platform"]
        RemotePresenter["Remote Presenter"]
    end

    PodiumPC -->|HDMI Out| Switcher
    PTZ_Cam -->|HDMI/SDI| Switcher
    FOH_PC -->|HDMI Out| Switcher

    Switcher -->|Output 1| Projector
    Switcher -->|Output 2| ConfMonitor
    Switcher -->|Output 3| USB_Bridge
    USB_Bridge -->|USB Video| FOH_PC

    PodiumMic -->|Mic In 1| DSP
    HandheldMic -->|Mic In 2| DSP

    USB_Bridge ---|USB Audio (Send/Return)| FOH_PC
    DSP -->|"Output to Platform (Mix-Minus)"| USB_Bridge
    USB_Bridge -->|"Platform Return Audio"| DSP

    DSP -->|"Output to Amp"| RoomAmp

    FOH_PC ---|Network| PlatformCloud
    PodiumPC -->|Network| PlatformCloud
    RemotePresenter ---|Internet| PlatformCloud
```

---

## 2. Audio DSP Routing: Mix‑Minus and Echo Control

The number one failure in hybrid rooms is **echo**: remote voices come out of the room speakers, go back into room mics, and are sent back to remote participants.

To avoid this, the DSP must provide:

- A **mix‑minus** feed to the platform (send all local mics, but not the platform's own return audio).
- **Acoustic Echo Cancellation (AEC)** on local mic inputs, referencing the platform return.

### Example DSP Matrix Configuration

| DSP Input Channel | Source                          | To Room Speakers? | To Platform Send? | AEC Configuration                                     |
| :---------------- | :------------------------------ | :---------------- | :---------------- | :---------------------------------------------------- |
| Input 1           | Podium Mic                      | YES               | YES               | AEC enabled; AEC reference = platform return input   |
| Input 2           | Handheld Q&A Mic(s)             | YES               | YES               | AEC enabled; AEC reference = platform return input   |
| Input 3           | Platform RX (remote participants) | YES               | NO (mix‑minus)    | AEC disabled; set as AEC reference source            |

### AEC and Mix‑Minus Checklist

1. **Set AEC reference** in the DSP software to the platform return input for all mic inputs.
2. **Enforce mix‑minus**: platform return mustn't be routed to the platform send.
3. Avoid double echo cancellation in the conferencing client if the DSP is doing AEC.
4. Use **gates and duckers** to keep handheld mics from opening on room noise.

---

## 3. Video Switcher Configuration and Presets

Your video switcher controls **what the room sees** and **what the platform sees**.

### Typical Inputs

1. **Podium PC HDMI** – slide deck output.
2. **FOH PC HDMI** – full screen view of spotlighted remote presenter or gallery.
3. **PTZ Camera** – camera on the room/audience.

### Typical Outputs

1. **Main Room Display / Projector** – what the local audience sees.
2. **Confidence Monitor (on stage)** – what the presenter sees (remote faces, notes, preview).
3. **USB/Capture Output** – what is sent to the platform as "camera" via the USB bridge.

### Core Switcher Presets

#### Preset 1 – Local Presenter Mode

- Room screen: Podium PC (slides full screen).
- Confidence monitor: FOH PC platform output (remote participants).
- Capture/USB to platform: PTZ camera on presenter.

The podium PC also shares its slides directly into the meeting.

#### Preset 2 – Remote Presenter Mode

- Room screen: FOH platform output (remote presenter full screen).
- Confidence monitor: PTZ camera or podium screen.
- Capture/USB to platform: PTZ camera on room, so remotes see the audience.

#### Preset 3 – Active Q&A Mode

- Room screen: FOH platform output (remote presenter responding).
- Confidence monitor: PTZ camera focused on audience member asking a question.
- Capture/USB to platform: PTZ camera on that audience member.

---

## 4. Conferencing Platform Settings (Generic)

These examples apply to Zoom, Teams, Meet, etc.: choose the **USB bridge** as your mic/speaker/camera and lock down sleep and network behavior.

### FOH Computer (Host)

- **Audio**
  - Mic: USB audio interface / DSP send.
  - Speaker: USB audio interface / DSP return.

- **Video**
  - Camera: USB capture device / switcher output.

- **Meeting**
  - Host the meeting from FOH.
  - Enable local or cloud recording per policy.
  - Mute participants on entry.
  - Assign co‑host rights to podium computer and remote presenters.

### Podium Computer (Slides)

- Keep on AC power; disable sleep, screen savers, and display timeouts.
- Use hard‑wired Ethernet; disable Wi‑Fi.
- Set display mode to **Extend**, not Duplicate.
- Join meeting as a participant but **Leave Computer Audio** in dual‑PC setups.
- Only screen‑share slides; never send or receive audio.

---

## 5. Single‑PC vs Dual‑PC Behavior

- **Dual‑PC (recommended)**
  - FOH PC is audio host; podium PC is slides‑only.

- **Single‑PC**
  - One PC joins audio and sends both program audio and room mics through DSP and switcher; HDMI audio routing must be checked carefully.

Always identify the **actual audio host** before troubleshooting audio issues.

---

## 6. FOH Operations and Q&A Playbook

### Microphone and Camera Discipline

- Keep handheld Q&A mics muted until the person is framed on camera.
- Coach participants to speak close to the mic and avoid pointing it at speakers.
- Coordinate PTZ shots and mic opens so remotes always see who is talking.

### Spotlighting vs Pinning (Conceptual)

- **Pinning** changes only the local FOH view.
- **Spotlighting** changes what everyone sees and what is recorded/sent to the projector.

Usage pattern:

- Spotlight the **remote presenter** while they speak.
- During interactive Q&A, spotlight **remote presenter + room camera** for side‑by‑side view where supported.

---

## 7. Monitoring Quality: Audio, Video, and System Health

Use three monitoring layers: **hardware**, **software**, and **shadow PC**.

### Hardware‑Level Audio Monitoring

- Plug closed‑back headphones into DSP or USB audio interface.
- Route the platform send bus (mix‑minus) to this monitor to hear exactly what is being sent upstream.

### Software‑Level Monitoring

Use the platform's statistics/diagnostics (Zoom Statistics, Teams call health, etc.) to monitor:

- CPU load.
- Audio jitter and packet loss (keep loss below 1–2%).
- Video resolution and frame rate.

### Shadow PC Monitoring

- Shadow machine joins the meeting with muted mic and headphones.
- Confirms remote experience and reports issues back to FOH.

---

## 8. Troubleshooting: Common Symptoms and Fixes

### Echo, Feedback, and Audio Loops

**Symptom:** Remote presenter hears themselves.
**Causes:** Platform return routed into platform send, or extra devices joined to audio.

**Fixes:**

- In DSP, ensure platform return isn't routed to platform send.
- Ensure all in‑room devices except the audio host have **left audio**.

---

**Symptom:** Loud squeal when handheld mic is unmuted.
**Causes:** Gain too high or mic too close to speakers.

**Fixes:**

- Mute the channel.
- Reduce gain; adjust gate.
- Move person out of loud speaker zones.

---

### No Audio from Remote in Room

**Symptom:** Remote video shows but room hears nothing.

**Fixes:**

- On host PC, check speaker device and OS volume.
- In DSP, check platform return input meter and routing to room speakers.

---

### Remote Cannot Hear the Room

**Symptom:** Remote sees room camera but hears nothing.

**Fixes:**

- Ensure host PC mic device is USB/DSP send.
- Check DSP routing of podium and handheld mics to platform send.

---

### Display / Signal Issues

**Symptom:** Laptop shows image; projector is black or "No Signal".

**Fixes:**

- Reseat HDMI/dongles; force EDID renegotiation.
- Set display mode to Extend and resolution to 1920×1080 @ 60Hz.
- Avoid DRM‑protected content that can trigger HDCP blackouts.

---

## 9. Podium Slide Presentation Gotchas

**Symptom:** Presenter View on projector; wrong view to remotes.

**Fixes:**

- In PowerPoint/Keynote, set slide show to external monitor.
- Adjust Presenter View setting.
- Start slide show, then share **slide show window** in conferencing app.

---

## 10. Pre‑Event Checklist

- **DSP**
  - Mix‑minus verified; platform return not in send path.
  - AEC reference set; mics have AEC enabled.

- **Switcher**
  - Presets for local presenter, remote presenter, Q&A.
  - Inputs labeled.

- **FOH PC**
  - Wired Ethernet; Wi‑Fi off.
  - USB bridge selected as mic/speaker/camera.
  - Dual monitors extended; full‑screen output routed to switcher input.

- **Podium PC**
  - Wired Ethernet; Wi‑Fi off.
  - Extend desktop; external at 1080p/60.
  - Joined to meeting; **Left Computer Audio** in dual‑PC setups.

- **Shadow PC**
  - Joins early; monitors with headphones; feeds back issues to FOH.

- **Room**
  - Mic walk test and full flow rehearsal with at least one remote participant.