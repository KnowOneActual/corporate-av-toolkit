import os
import subprocess
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)  # This will be /home/user/Desktop/test_media_toolkit
LOOPS_DIR = os.path.join(BASE_DIR, "03_Looping_Video_Backgrounds")
PRORES_422_DIR = os.path.join(LOOPS_DIR, "ProRes_422_Loops")
PRORES_4444_DIR = os.path.join(LOOPS_DIR, "ProRes_4444_&_Hap_Alpha")
ALPHA_GLITCH_DIR = os.path.join(LOOPS_DIR, "Alpha_&_Glitch_Elements")

files_to_compress = [
    {
        "input": "abstract-light-waves_ZyUlMBnlr-Apple ProRes 422.mov",
        "output": "abstract_light_waves.mp4"
    },
    {
        "input": "blue-black-vertical-shining-beam_WkOKwwUeB-Apple ProRes 422.mov",
        "output": "blue_black_vertical_shining_beam.mp4"
    },
    {
        "input": "blue-shining-stream-beam_bJ9hLPUxS-Apple ProRes 422.mov",
        "output": "blue_shining_stream_beam.mp4"
    },
    {
        "input": "golden-center-light-rays_b1nsCVhgr-Apple ProRes 422.mov",
        "output": "golden_center_light_rays.mp4"
    },
    {
        "input": "lines-of-green-lights-move-in-waves_wj3eyf_eb__D-Apple ProRes 422.mov",
        "output": "lines_of_green_lights_move_in_waves.mp4"
    }
]

def get_dir_size(path):
    total_size = 0
    if not os.path.exists(path):
        return 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip symlinks
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size_bytes):
    if size_bytes <= 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def main():
    initial_size = get_dir_size(BASE_DIR)
    print(f"Initial Toolkit Size: {format_size(initial_size)}")
    print("-" * 50)
    
    compressed_files = []
    
    # 1. Compress ProRes files if directory exists
    if os.path.exists(PRORES_422_DIR):
        print("Step 1: Compressing corporate ProRes 422 files to H.264 MP4...")
        for f in files_to_compress:
            input_path = os.path.join(PRORES_422_DIR, f["input"])
            output_path = os.path.join(LOOPS_DIR, f["output"])
            
            if not os.path.exists(input_path):
                print(f"Warning: Input file not found: {f['input']}. Skipping.")
                continue
                
            print(f"Compressing {f['input']} -> {f['output']}...")
            
            cmd = [
                "ffmpeg", "-y",
                "-i", input_path,
                "-c:v", "libx264",
                "-crf", "20",
                "-preset", "medium",
                "-pix_fmt", "yuv420p",
                "-an",
                output_path
            ]
            
            try:
                subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                print(f"Successfully created: {f['output']} ({format_size(os.path.getsize(output_path))})")
                compressed_files.append(output_path)
            except subprocess.CalledProcessError as e:
                print(f"Error compressing {f['input']}:")
                print(e.stderr)
                print("Aborting optimization. No files will be deleted.")
                return
    else:
        print("Note: ProRes 422 source directory not found. Scanning LOOPS directory for any raw .mov files...")

    # Also scan LOOPS_DIR for general heavy unoptimized .mov, .avi, or .mkv files
    if os.path.exists(LOOPS_DIR):
        for f in os.listdir(LOOPS_DIR):
            if f.lower().endswith(('.mov', '.avi', '.mkv')) and not f.startswith('.'):
                input_path = os.path.join(LOOPS_DIR, f)
                output_name = os.path.splitext(f)[0] + ".mp4"
                output_path = os.path.join(LOOPS_DIR, output_name)
                
                if os.path.exists(output_path):
                    print(f"Skipping {f} (optimized version {output_name} already exists).")
                    continue
                    
                print(f"Compressing unoptimized file: {f} -> {output_name}...")
                cmd = [
                    "ffmpeg", "-y",
                    "-i", input_path,
                    "-c:v", "libx264",
                    "-crf", "20",
                    "-preset", "medium",
                    "-pix_fmt", "yuv420p",
                    "-an",
                    output_path
                ]
                try:
                    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
                    print(f"Successfully created: {output_name} ({format_size(os.path.getsize(output_path))})")
                    compressed_files.append(output_path)
                    print(f"Removing original unoptimized file: {f}")
                    os.remove(input_path)
                except subprocess.CalledProcessError as e:
                    print(f"Error compressing {f}:")
                    print(e.stderr)

    # 2. Delete source folders if they exist
    print("\nStep 2: Cleaning up large source directories if present...")
    if os.path.exists(PRORES_422_DIR):
        print("Removing ProRes 422 folder...")
        shutil.rmtree(PRORES_422_DIR)
        print("Removed ProRes 422 folder.")
        
    if os.path.exists(PRORES_4444_DIR):
        print("Removing ProRes 4444 & Hap Alpha folder...")
        shutil.rmtree(PRORES_4444_DIR)
        print("Removed ProRes 4444 & Hap Alpha folder.")
        
    if os.path.exists(ALPHA_GLITCH_DIR):
        print("Removing Alpha & Glitch Elements folder...")
        shutil.rmtree(ALPHA_GLITCH_DIR)
        print("Removed Alpha & Glitch Elements folder.")

    final_size = get_dir_size(BASE_DIR)
    saved_space = initial_size - final_size
    
    print("-" * 50)
    print("AV TOOLKIT OPTIMIZATION COMPLETED!")
    print(f"Initial Size: {format_size(initial_size)}")
    print(f"Final Size:   {format_size(final_size)}")
    if saved_space > 0:
        print(f"Saved Space:  {format_size(saved_space)} (~{round((saved_space / initial_size) * 100, 1)}% reduction)")
    else:
        print("No space saved (already fully optimized).")

if __name__ == "__main__":
    main()
