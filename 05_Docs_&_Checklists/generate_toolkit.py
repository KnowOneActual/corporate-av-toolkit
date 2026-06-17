import os
import wave
import struct
import math
import random
import subprocess
import shutil
from PIL import Image, ImageDraw, ImageFont

# Directory configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)  # This will be /home/user/Desktop/test_media_toolkit
AUDIO_DIR = os.path.join(BASE_DIR, "01_Audio_&_Sync")
DISPLAY_DIR = os.path.join(BASE_DIR, "02_Display_Calibration")
TEMP_FRAMES_DIR = os.path.join(BASE_DIR, "temp_frames")

# Fonts
FONT_REGULAR_PATH = "/usr/share/fonts/google-carlito-fonts/Carlito-Regular.ttf"
FONT_BOLD_PATH = "/usr/share/fonts/google-carlito-fonts/Carlito-Bold.ttf"

def load_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except IOError:
        try:
            return ImageFont.load_default(size=size)
        except TypeError:
            return ImageFont.load_default()

def save_wav(filename, samples, sample_rate=44100, num_channels=2):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(2) # 16-bit PCM
        wav_file.setframerate(sample_rate)
        
        packed_data = []
        for sample in samples:
            if num_channels == 2:
                if isinstance(sample, tuple) or isinstance(sample, list):
                    val_l = int(max(-32768, min(32767, sample[0])))
                    val_r = int(max(-32768, min(32767, sample[1])))
                else:
                    val = int(max(-32768, min(32767, sample)))
                    val_l, val_r = val, val
                packed_data.append(struct.pack('<hh', val_l, val_r))
            else:
                val = int(max(-32768, min(32767, sample)))
                packed_data.append(struct.pack('<h', val))
        
        wav_file.writeframes(b''.join(packed_data))

def generate_reference_tone(filename, frequency=1000, dbfs=-20, duration=10, sample_rate=44100):
    print(f"Generating reference tone: {frequency}Hz at {dbfs}dBFS...")
    amplitude = 32767 * (10 ** (dbfs / 20.0))
    num_samples = int(duration * sample_rate)
    samples = []
    for i in range(num_samples):
        t = i / sample_rate
        val = amplitude * math.sin(2 * math.pi * frequency * t)
        samples.append(val)
    save_wav(filename, samples, sample_rate, num_channels=2)

def generate_stereo_check(filename, duration=12, sample_rate=44100):
    print("Generating stereo channel check...")
    num_samples = int(duration * sample_rate)
    samples = []
    amplitude = 32767 * (10 ** (-15 / 20.0)) # -15 dBFS
    
    for i in range(num_samples):
        t = i / sample_rate
        if t < 4.0:
            # Pulsed beep on Left, silent on Right (4 beeps, 0.5s on, 0.5s off)
            if int(t * 2) % 2 == 0:
                val_l = amplitude * math.sin(2 * math.pi * 440 * t)
            else:
                val_l = 0
            val_r = 0
        elif t < 8.0:
            # Pulsed beep on Right, silent on Left (4 beeps)
            if int(t * 2) % 2 == 0:
                val_r = amplitude * math.sin(2 * math.pi * 440 * t)
            else:
                val_r = 0
            val_l = 0
        else:
            # Steady 880Hz tone on both (Center check)
            val_l = amplitude * math.sin(2 * math.pi * 880 * t)
            val_r = val_l
        samples.append((val_l, val_r))
    save_wav(filename, samples, sample_rate, num_channels=2)

def generate_frequency_sweep(filename, f_start=20, f_end=20000, dbfs=-15, duration=15, sample_rate=44100):
    print(f"Generating frequency sweep from {f_start}Hz to {f_end}Hz...")
    amplitude = 32767 * (10 ** (dbfs / 20.0))
    num_samples = int(duration * sample_rate)
    samples = []
    
    ln_f = math.log(f_end / f_start)
    for i in range(num_samples):
        t = i / sample_rate
        if t >= duration:
            samples.append(0)
            continue
        phase = 2 * math.pi * f_start * (duration / ln_f) * (math.exp(t * ln_f / duration) - 1)
        val = amplitude * math.sin(phase)
        samples.append(val)
    save_wav(filename, samples, sample_rate, num_channels=2)

def generate_pink_noise(filename, dbfs=-18, duration=10, sample_rate=44100):
    print(f"Generating pink noise at {dbfs}dBFS...")
    num_samples = int(duration * sample_rate)
    num_rows = 12
    array = [random.uniform(-1.0, 1.0) for _ in range(num_rows)]
    running_sum = sum(array)
    
    raw_samples = []
    for i in range(num_samples):
        r = 0
        if i > 0:
            temp = i
            while (temp & 1) == 0:
                temp >>= 1
                r += 1
        if r < num_rows:
            running_sum -= array[r]
            array[r] = random.uniform(-1.0, 1.0)
            running_sum += array[r]
        
        val = running_sum + random.uniform(-1.0, 1.0)
        raw_samples.append(val / (num_rows + 1))
        
    mean_square = sum(x**2 for x in raw_samples) / len(raw_samples)
    rms_raw = math.sqrt(mean_square)
    
    target_rms = 32767 * (10 ** (dbfs / 20.0))
    scale_factor = target_rms / rms_raw
    
    samples = [x * scale_factor for x in raw_samples]
    save_wav(filename, samples, sample_rate, num_channels=2)

def generate_sync_audio(filename, duration=15, sample_rate=44100):
    print("Generating AV sync click audio track...")
    num_samples = int(duration * sample_rate)
    samples = [0.0] * num_samples
    amplitude = 32767 * (10 ** (-12 / 20.0)) # -12 dBFS beep
    
    # Beeps occur every 1.0 second, centered at 0.5s, 1.5s, 2.5s...
    for cycle in range(duration):
        beep_center = cycle + 0.5
        beep_start = beep_center - 0.025 # 50 ms duration
        beep_end = beep_center + 0.025
        
        start_idx = int(beep_start * sample_rate)
        end_idx = int(beep_end * sample_rate)
        
        for idx in range(start_idx, end_idx):
            if idx < num_samples:
                t = idx / sample_rate
                samples[idx] = amplitude * math.sin(2 * math.pi * 1000 * t)
                
    save_wav(filename, samples, sample_rate, num_channels=2)

def generate_phase_polarity_test(filename, duration=12, sample_rate=44100):
    print("Generating speaker phase polarity check (tone & pink noise)...")
    num_samples = int(duration * sample_rate)
    samples = []
    
    tone_amp = 32767 * (10 ** (-15 / 20.0)) # -15 dBFS
    noise_amp = 32767 * (10 ** (-18 / 20.0)) # -18 dBFS
    
    # Pink noise generator setup (Voss-McCartney algorithm)
    num_rows = 12
    array_l = [random.uniform(-1.0, 1.0) for _ in range(num_rows)]
    running_sum_l = sum(array_l)
    array_r = [random.uniform(-1.0, 1.0) for _ in range(num_rows)]
    running_sum_r = sum(array_r)
    
    for i in range(num_samples):
        t = i / sample_rate
        
        if t < 6.0:
            # 0-6s: 500 Hz Tone (pulsed)
            # Pulse: 0.4s on, 0.2s off
            pulse_cycle = t % 0.6
            if pulse_cycle < 0.4:
                val_l = tone_amp * math.sin(2 * math.pi * 500 * t)
            else:
                val_l = 0.0
                
            if t < 3.0:
                val_r = val_l # In-Phase
            else:
                val_r = -val_l # Out-of-Phase
        else:
            # 6-12s: Pink Noise (in-phase 6-9s, out-of-phase 9-12s)
            # Generate one step of pink noise
            r = 0
            if i > 0:
                temp = i
                while (temp & 1) == 0:
                    temp >>= 1
                    r += 1
            if r < num_rows:
                running_sum_l -= array_l[r]
                array_l[r] = random.uniform(-1.0, 1.0)
                running_sum_l += array_l[r]
            
            raw_val = (running_sum_l + random.uniform(-1.0, 1.0)) / (num_rows + 1)
            val_l = raw_val * noise_amp * 2.0
            
            if t < 9.0:
                val_r = val_l # In-Phase
            else:
                val_r = -val_l # Out-of-Phase
                
        samples.append((val_l, val_r))
        
    save_wav(filename, samples, sample_rate, num_channels=2)

def draw_convergence_pattern(filename):
    print("Generating display convergence pattern...")
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    
    # 1. White border (to check cropping / overscan)
    draw.rectangle([0, 0, width - 1, height - 1], outline="white", width=2)
    
    # 2. Grid lines (spaced 120 pixels apart)
    grid_color = (120, 120, 120)
    for x in range(120, width, 120):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(120, height, 120):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
        
    # 3. Center Crosshairs (Thick red lines)
    draw.line([(width // 2, 0), (width // 2, height)], fill="red", width=3)
    draw.line([(0, height // 2), (width, height // 2)], fill="red", width=3)
    
    # 4. Aspect Ratio Circle (Red, radius 300)
    center = (width // 2, height // 2)
    draw.ellipse([center[0] - 300, center[1] - 300, center[0] + 300, center[1] + 300], outline="red", width=3)
    
    # 5. Corner focus circles (Red, radius 100)
    corners = [
        (240, 240),
        (width - 240, 240),
        (240, height - 240),
        (width - 240, height - 240)
    ]
    for c in corners:
        draw.ellipse([c[0] - 100, c[1] - 100, c[0] + 100, c[1] + 100], outline="red", width=2)
        draw.line([(c[0] - 120, c[1]), (c[0] + 120, c[1])], fill="red", width=1)
        draw.line([(c[0], c[1] - 120), (c[0], c[1] + 120)], fill="red", width=1)
        
    # 6. Adding Text labels
    font_title = load_font(FONT_BOLD_PATH, 32)
    font_info = load_font(FONT_REGULAR_PATH, 24)
    font_small = load_font(FONT_REGULAR_PATH, 14)
    
    # Draw central info box
    draw.rectangle([width//2 - 250, height//2 - 80, width//2 + 250, height//2 + 80], fill="black", outline="red", width=2)
    
    title_text = "CONVERGENCE & ALIGNMENT TEST"
    info_text = "1920 x 1080 | 16:9 ASPECT RATIO"
    hint_text = "If center circle is not perfectly round, check projector aspect scaling."
    
    # Center text
    draw.text((width // 2, height // 2 - 45), title_text, font=font_title, fill="white", anchor="mm")
    draw.text((width // 2, height // 2), info_text, font=font_info, fill="white", anchor="mm")
    draw.text((width // 2, height // 2 + 45), hint_text, font=font_small, fill="grey", anchor="mm")
    
    # Corner focus labels
    draw.text((240, 240), "FOCUS TL\n240,240", font=font_small, fill="white", anchor="mm", align="center")
    draw.text((width - 240, 240), "FOCUS TR\n1680,240", font=font_small, fill="white", anchor="mm", align="center")
    draw.text((240, height - 240), "FOCUS BL\n240,840", font=font_small, fill="white", anchor="mm", align="center")
    draw.text((width - 240, height - 240), "FOCUS BR\n1680,840", font=font_small, fill="white", anchor="mm", align="center")
    
    # Border tick markers
    for x in [120, 960, width - 120]:
        draw.text((x, 10), f"x={x}", font=font_small, fill="white", anchor="mt")
        draw.text((x, height - 25), f"x={x}", font=font_small, fill="white", anchor="mb")
    for y in [120, 540, height - 120]:
        draw.text((10, y), f"y={y}", font=font_small, fill="white", anchor="lm")
        draw.text((width - 10, y), f"y={y}", font=font_small, fill="white", anchor="rm")
        
    image.save(filename)

def draw_legibility_pattern(filename):
    print("Generating text legibility and compression pattern...")
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # 1. Dark title header
    draw.rectangle([0, 0, width, 120], fill="#0f172a") # Slate 900
    font_header = load_font(FONT_BOLD_PATH, 32)
    font_subheader = load_font(FONT_REGULAR_PATH, 18)
    draw.text((width // 2, 45), "SCREEN SHARE LEGIBILITY & COMPRESSION TEST CHART", font=font_header, fill="white", anchor="mm")
    draw.text((width // 2, 85), "Use this chart to test Zoom/Teams compression artifacts, chroma sub-sampling, and scale scaling.", font=font_subheader, fill="#cbd5e1", anchor="mm")
    
    # 2. Divide into columns
    col_y_start = 140
    col_width = (width - 80) // 3
    
    # Column 1: Typography and Sizing (White background, Black text)
    col1_x = 30
    draw.rectangle([col1_x, col_y_start, col1_x + col_width, height - 30], outline="#cbd5e1", width=1)
    draw.rectangle([col1_x, col_y_start, col1_x + col_width, col_y_start + 40], fill="#334155")
    draw.text((col1_x + col_width // 2, col_y_start + 20), "TYPOGRAPHY & FONT SIZES", font=load_font(FONT_BOLD_PATH, 16), fill="white", anchor="mm")
    
    # Write text samples of different sizes
    font_sizes = [6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 32]
    curr_y = col_y_start + 60
    for fs in font_sizes:
        font_sample = load_font(FONT_REGULAR_PATH, fs)
        text_sample = f"Font Size {fs}pt: Pack my box with five dozen liquor jugs."
        draw.text((col1_x + 15, curr_y), text_sample, font=font_sample, fill="black", anchor="lm")
        curr_y += max(fs + 14, 22)
        
    # Column 2: Color Sub-sampling & Contrast (4:2:0 Test)
    col2_x = 30 + col_width + 10
    draw.rectangle([col2_x, col_y_start, col2_x + col_width, height - 30], outline="#cbd5e1", width=1)
    draw.rectangle([col2_x, col_y_start, col2_x + col_width, col_y_start + 40], fill="#334155")
    draw.text((col2_x + col_width // 2, col_y_start + 20), "COLOR SUB-SAMPLING & CONTRAST", font=load_font(FONT_BOLD_PATH, 16), fill="white", anchor="mm")
    
    # Red text on Black box (Chroma sub-sampling test)
    box_y = col_y_start + 60
    draw.rectangle([col2_x + 15, box_y, col2_x + col_width - 15, box_y + 160], fill="black")
    draw.text((col2_x + col_width // 2, box_y + 20), "CHROMA SUB-SAMPLING (4:2:0 vs 4:4:4)", font=load_font(FONT_BOLD_PATH, 14), fill="white", anchor="mm")
    
    red_test_font_large = load_font(FONT_BOLD_PATH, 18)
    red_test_font_small = load_font(FONT_REGULAR_PATH, 12)
    draw.text((col2_x + col_width // 2, box_y + 60), "RED ON BLACK TEXT IS OFTEN SMUDGED IN ZOOM/TEAMS", font=red_test_font_large, fill="red", anchor="mm")
    draw.text((col2_x + col_width // 2, box_y + 100), "If this text is blurry or illegible, it's due to video compression sub-sampling.", font=red_test_font_small, fill="red", anchor="mm")
    draw.text((col2_x + col_width // 2, box_y + 130), "Try checking 'Optimize for video clip' or sharing a specific window rather than screen.", font=red_test_font_small, fill="#00ff00", anchor="mm")
    
    # Low Contrast test (Light grey on White)
    curr_y2 = box_y + 180
    draw.text((col2_x + 15, curr_y2), "Low Contrast Test:", font=load_font(FONT_BOLD_PATH, 14), fill="black", anchor="lm")
    curr_y2 += 25
    
    contrasts = [
        ("90% Grey Contrast (Standard)", "#1e293b", 14),
        ("70% Grey Contrast (Medium)", "#64748b", 14),
        ("50% Grey Contrast (Lower)", "#94a3b8", 12),
        ("30% Grey Contrast (Hard to see)", "#cbd5e1", 10),
        ("15% Grey Contrast (Near Limit)", "#e2e8f0", 8)
    ]
    for label, color, size in contrasts:
        draw.text((col2_x + 20, curr_y2), f"{label} - size {size}pt", font=load_font(FONT_REGULAR_PATH, size), fill=color, anchor="lm")
        curr_y2 += 25
        
    # Blue on Black box
    curr_y2 += 10
    draw.rectangle([col2_x + 15, curr_y2, col2_x + col_width - 15, curr_y2 + 100], fill="black")
    draw.text((col2_x + col_width // 2, curr_y2 + 25), "BLUE ON BLACK TEST (Chroma 4:2:0)", font=load_font(FONT_BOLD_PATH, 14), fill="white", anchor="mm")
    draw.text((col2_x + col_width // 2, curr_y2 + 65), "Blue text on black suffers similarly from sub-sampling compression.", font=load_font(FONT_REGULAR_PATH, 12), fill="blue", anchor="mm")
    
    # Column 3: Scaling, Fine Lines & Moiré
    col3_x = 30 + 2 * col_width + 20
    draw.rectangle([col3_x, col_y_start, col3_x + col_width, height - 30], outline="#cbd5e1", width=1)
    draw.rectangle([col3_x, col_y_start, col3_x + col_width, col_y_start + 40], fill="#334155")
    draw.text((col3_x + col_width // 2, col_y_start + 20), "SCALING & DETAIL PATTERNS", font=load_font(FONT_BOLD_PATH, 16), fill="white", anchor="mm")
    
    # Draw fine grid in col 3
    pattern_y = col_y_start + 60
    draw.text((col3_x + 15, pattern_y), "Fine Line & Nyquist Limit Tests:", font=load_font(FONT_BOLD_PATH, 14), fill="black", anchor="lm")
    
    # Drawing horizontal / vertical line patterns
    start_pat_y = pattern_y + 20
    # 1px lines, 1px gaps
    draw.text((col3_x + 15, start_pat_y + 10), "1px line, 1px gap (horizontal):", font=load_font(FONT_REGULAR_PATH, 11), fill="black", anchor="lm")
    for ly in range(start_pat_y + 20, start_pat_y + 50, 2):
        draw.line([(col3_x + 15, ly), (col3_x + col_width - 15, ly)], fill="black", width=1)
        
    start_pat_y += 60
    draw.text((col3_x + 15, start_pat_y + 10), "2px line, 2px gap (horizontal):", font=load_font(FONT_REGULAR_PATH, 11), fill="black", anchor="lm")
    for ly in range(start_pat_y + 20, start_pat_y + 60, 4):
        draw.line([(col3_x + 15, ly), (col3_x + col_width - 15, ly)], fill="black", width=2)
        
    start_pat_y += 70
    draw.text((col3_x + 15, start_pat_y + 10), "1px vertical lines (horizontal sweep):", font=load_font(FONT_REGULAR_PATH, 11), fill="black", anchor="lm")
    for lx in range(col3_x + 15, col3_x + col_width - 15, 4):
        draw.line([(lx, start_pat_y + 20), (lx, start_pat_y + 70)], fill="black", width=1)
        
    start_pat_y += 90
    draw.text((col3_x + 15, start_pat_y + 10), "Concentric Moiré Circle Target:", font=load_font(FONT_BOLD_PATH, 14), fill="black", anchor="lm")
    circle_center = (col3_x + col_width // 2, start_pat_y + 120)
    for r in range(10, 100, 4):
        draw.ellipse([circle_center[0] - r, circle_center[1] - r, circle_center[0] + r, circle_center[1] + r], outline="black", width=1)
        
    # Standard warning text at the bottom of the chart
    draw.text((width // 2, height - 50), "NOTE: If sharing over Zoom/Teams, look at this slide on the REMOTE client computer. Look for text blurring, missing fine lines, or scaling artifacts.", font=load_font(FONT_REGULAR_PATH, 12), fill="#64748b", anchor="mm")
    
    image.save(filename)

def generate_av_sync_video(output_mp4, duration=15):
    print("Preparing to build AV Sync Video...")
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)
    
    fps = 30
    total_frames = duration * fps
    
    temp_wav = os.path.join(AUDIO_DIR, "temp_sync_audio.wav")
    generate_sync_audio(temp_wav, duration=duration)
    
    width, height = 1920, 1080
    font_title = load_font(FONT_BOLD_PATH, 36)
    font_subtitle = load_font(FONT_REGULAR_PATH, 20)
    font_bold_mid = load_font(FONT_BOLD_PATH, 24)
    font_reg_mid = load_font(FONT_REGULAR_PATH, 18)
    font_ticks = load_font(FONT_REGULAR_PATH, 12)
    font_big_flash = load_font(FONT_BOLD_PATH, 72)
    
    print(f"Drawing {total_frames} video frames...")
    for i in range(total_frames):
        # Frame cycle math
        cycle_idx = i % fps
        t_sec = i / fps
        
        # Sync flash at frame 15 of every cycle
        is_flash_frame = (cycle_idx == 15)
        
        # Draw background: Flash teal on sync, dark grey on normal
        bg_color = (15, 23, 42) # slate-900
        if is_flash_frame:
            bg_color = (13, 148, 136) # teal-600
            
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        
        # 1. Header Information
        draw.text((width // 2, 60), "AV LATENCY & LIP-SYNC CALIBRATION TEST", font=font_title, fill="white", anchor="mm")
        draw.text((width // 2, 110), "Align audio beep with visual flash. Use frame-by-frame (VLC: 'E') to measure offsets.", font=font_subtitle, fill="#cbd5e1", anchor="mm")
        
        # 2. Sync Flash Target indicator box
        flash_box = [width // 2 - 400, 150, width // 2 + 400, 320]
        if is_flash_frame:
            draw.rectangle(flash_box, fill="white", outline="yellow", width=4)
            draw.text((width // 2, 235), "SYNC FLASH!", font=font_big_flash, fill="black", anchor="mm")
        else:
            draw.rectangle(flash_box, fill="#1e293b", outline="#475569", width=2)
            draw.text((width // 2, 235), "WAITING FOR SYNC", font=font_bold_mid, fill="#64748b", anchor="mm")
            
        # 3. Millisecond Track
        # The track ranges from -500ms to +500ms. 1 pixel = 1ms.
        track_y = 650
        track_start_x = width // 2 - 500 # 460
        track_end_x = width // 2 + 500   # 1460
        
        # Draw track container
        draw.rectangle([track_start_x - 10, track_y - 40, track_end_x + 10, track_y + 40], fill="#0f172a", outline="#475569", width=2)
        
        # Draw ticks every 50ms (50 pixels) and major labels every 100ms
        for offset in range(-500, 501, 50):
            tick_x = width // 2 + offset
            is_major = (offset % 100 == 0)
            tick_h = 25 if is_major else 12
            tick_color = "white" if is_major else "#64748b"
            
            # Center tick is green and thick
            if offset == 0:
                tick_color = "#10b981" # Emerald 500
                tick_h = 35
                
            draw.line([(tick_x, track_y - tick_h), (tick_x, track_y + tick_h)], fill=tick_color, width=2 if is_major else 1)
            
            if is_major:
                label = "SYNC (0ms)" if offset == 0 else f"{offset:+} ms"
                lbl_color = "#34d399" if offset == 0 else "white"
                # Offset label position slightly
                draw.text((tick_x, track_y + 55), label, font=font_ticks, fill=lbl_color, anchor="mm")
                
        # 4. Draw the Bouncing Sweep Marker
        # Center of marker offset in ms relative to frame 15:
        # offset_ms = (cycle_idx - 15) * (1000/30)
        marker_offset_ms = (cycle_idx - 15) * (1000.0 / 30.0)
        marker_x = int(width // 2 + marker_offset_ms)
        
        # Draw vertical sweep bar
        draw.rectangle([marker_x - 6, track_y - 35, marker_x + 6, track_y + 35], fill="#ef4444") # Red bar
        draw.line([(marker_x, track_y - 45), (marker_x, track_y + 45)], fill="white", width=2)
        
        # 5. Calibration Help instructions
        help_box_y = 800
        draw.rectangle([width // 2 - 600, help_box_y, width // 2 + 600, help_box_y + 160], fill="#1e293b", outline="#334155")
        
        draw.text((width // 2 - 580, help_box_y + 20), "CALIBRATION INSTRUCTIONS:", font=font_bold_mid, fill="#38bdf8")
        
        instructions = [
            "- Video uses 30 FPS. Each frame is exactly 33.3 milliseconds.",
            "- AUDIO LAGGING: If the beep is heard while the red bar is on the RIGHT (+) side.",
            "- VIDEO LAGGING: If the beep is heard while the red bar is on the LEFT (-) side.",
            "- To calculate system latency: subtract/add the ms value where the beep aligns with the red bar."
        ]
        
        curr_inst_y = help_box_y + 50
        for inst in instructions:
            draw.text((width // 2 - 580, curr_inst_y), inst, font=font_reg_mid, fill="white", anchor="lm")
            curr_inst_y += 24
            
        # 6. Status display (Frame number, Time code)
        status_text = f"Frame: {i:03d} / {total_frames} | Time: {t_sec:.2f}s | Speed: 30 FPS"
        draw.text((width // 2, height - 40), status_text, font=font_reg_mid, fill="#94a3b8", anchor="mm")
        
        # Save frame image
        frame_name = os.path.join(TEMP_FRAMES_DIR, f"frame_{i:03d}.png")
        image.save(frame_name)
        
    print("Ffmpeg encoding video...")
    # Ffmpeg command to assemble frames and sync audio
    # -y (overwrite)
    # -r 30 (input frame rate)
    # -i temp_frames/frame_%03d.png (input frames)
    # -i temp_wav (input audio)
    # -c:v libx264 (H.264 video codec)
    # -pix_fmt yuv420p (compatibility for corporate players/TVs)
    # -c:a aac -b:a 192k (high quality AAC audio)
    # output file path
    cmd = [
        "ffmpeg", "-y",
        "-r", "30",
        "-i", os.path.join(TEMP_FRAMES_DIR, "frame_%03d.png"),
        "-i", temp_wav,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        output_mp4
    ]
    
    # Run the command through rtk if enabled (hook will handle it, but using subprocess.run)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("FFmpeg error output:")
        print(result.stderr)
        raise RuntimeError("FFmpeg compilation failed.")
        
    print("Cleaning up temporary files...")
    # Delete temporary wav
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
    # Delete temp frames directory
    if os.path.exists(TEMP_FRAMES_DIR):
        shutil.rmtree(TEMP_FRAMES_DIR)
        
    print(f"AV Sync Video generated successfully at: {output_mp4}")

def main():
    # Make sure output directories exist
    os.makedirs(AUDIO_DIR, exist_ok=True)
    os.makedirs(DISPLAY_DIR, exist_ok=True)
    
    # 1. Generate audio files
    generate_reference_tone(os.path.join(AUDIO_DIR, "audio_01_ref_1khz_tone.wav"))
    generate_stereo_check(os.path.join(AUDIO_DIR, "audio_02_stereo_channel_check.wav"))
    generate_frequency_sweep(os.path.join(AUDIO_DIR, "audio_03_frequency_sweep_20hz_20khz.wav"))
    generate_pink_noise(os.path.join(AUDIO_DIR, "audio_04_pink_noise_eq.wav"))
    generate_phase_polarity_test(os.path.join(AUDIO_DIR, "audio_05_phase_test.wav"))
    
    # 2. Generate test images
    draw_convergence_pattern(os.path.join(DISPLAY_DIR, "image_01_display_convergence.png"))
    draw_legibility_pattern(os.path.join(DISPLAY_DIR, "image_02_screen_share_legibility.png"))
    
    # 3. Generate AV sync video
    generate_av_sync_video(os.path.join(AUDIO_DIR, "video_01_av_sync_latency_test.mp4"))
    
    print("\nAV TEST TOOLKIT COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
