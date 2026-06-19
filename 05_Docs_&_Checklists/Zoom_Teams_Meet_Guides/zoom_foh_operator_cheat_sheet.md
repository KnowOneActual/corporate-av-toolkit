# Zoom FOH Operator Cheat Sheet
_For corporate hybrid meetings with in-room audience and Zoom participants_

## 1. Role and Equipment Setup
- **FOH PC**: Serves as the primary Zoom Host. Connect it to the audio interface and video capture card.
- **Podium PC**: Used for slide sharing. Do not connect its audio to Zoom to prevent feedback.
- **Shadow PC (Optional)**: Connects to monitor the attendee experience. Keep its microphone muted and route audio to headphones only.

## 2. Audio and Video Configuration
Configure these settings on the FOH PC before opening doors:
- **Audio Output**: Select the DSP or USB audio device for both microphone and speaker.
- **Echo Cancellation**: Set to Auto, or Low if the DSP provides echo cancellation.
- **Original Sound**: Disable "Original sound for musicians" unless bypassing Zoom processing.
- **Video Input**: Select the USB capture card or switcher output.
- **Display**: Enable "Use dual monitors" and set the operating system display mode to Extended.

## 3. Signal Routing
- **Video to Zoom**: Send the switcher output to the capture card on the FOH PC.
- **Room Screens**: Route the Podium PC HDMI output to the projector for local slides, or route the FOH PC screen to the projector for remote presenters.
- **Room Audio**: Send Zoom output to the DSP, which routes audio to room speakers. Send a mix-minus signal from the DSP back to the FOH PC microphone input.

## 4. Pre-Show Checklist
Complete these steps 15 to 20 minutes before start:
1. Power on all hardware including the DSP, video switcher, and cameras.
2. Launch the Zoom meeting on the FOH PC as the Host.
3. Admit the Podium PC, make it Co-host, and select "Leave Computer Audio" on that machine. Set its system volume to zero.
4. Admit the Shadow PC if one is used.
5. Verify the FOH camera feed and ensure the audio input meters respond to a local microphone.

## 5. Meeting Operation
- **Audio Control**: Ensure only the FOH PC is connected to the Zoom audio.
- **Video Control**: Use the Zoom Spotlight feature to focus the projector on the active presenter. Pin speakers on the local FOH monitor to check their feed without changing the broadcast view.
- **Slide Sharing**: Start the presentation on the Podium PC, then choose "Share Screen" and select the presentation window in Zoom.

## 6. Q&A Routing
- **Remote Questions**: Spotlight both the remote speaker and the local room camera to show both parties.
- **In-Room Questions**: Point the camera at the speaker with the microphone. Unmute the Q&A channel on the DSP, then mute it immediately when they finish speaking.

## 7. Recording Management
Select the recording type based on distribution needs:
- **Local Recording (FOH PC Disk)**: Best when you need to edit the video file afterward. Set the destination folder to a fast internal SSD.
- **Cloud Recording**: Best when other team members need quick access to the file via a URL.
- **Settings**: Turn on "Record video during screen sharing" and "Place video next to shared screen".
- **Post-Show**: Wait for local file conversion to complete. Rename the file using the format `YYYY-MM-DD_Event-Name` and move it to the shared archive.

## 8. Diagnostics and Troubleshooting
### System Monitoring
On the FOH PC, press `Cmd/Ctrl + Option/Alt + Shift + D` to open the statistics panel:
- **Processor Load**: Zoom usage should remain under 40% and host system usage under 80%.
- **Audio Quality**: Maintain packet loss below 2% and watch for jitter spikes.
- **Video Quality**: Confirm resolution is HD and frame rate is at least 24 frames per second.

On the Shadow PC, verify:
- The video feed displays the correct layout and slides.
- The audio feed is clear and does not echo.
- Report any feed discrepancies to the FOH operator.

### Issue Resolution
- **Echo or Feedback**: Identify in-room laptops connected to audio. Ensure they select "Leave Computer Audio" or use headphones. Confirm the DSP mix-minus is routing correctly.
- **Remote Attendees Cannot Hear**: Confirm the FOH microphone setting is set to the USB or DSP interface. Verify that the DSP is sending signals to the Zoom input.
- **In-Room Audience Cannot Hear Remotes**: Verify the FOH speaker setting. Ensure the DSP is routing the Zoom input to the room amplifier.
- **Slides Do Not Show**: Verify the Podium PC is sharing the application window rather than a desktop. Check screen recording permissions on macOS.