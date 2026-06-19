import os
import math
from PIL import Image, ImageDraw, ImageFont

# Set output directory to current folder (03_Looping_Video_Backgrounds)
LOOPS_DIR = os.path.dirname(os.path.abspath(__file__))

def load_system_font(size):
    # Try common Mac system paths, then fallback
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/System/Library/Fonts/Cache/Helvetica.ttc"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()

def draw_gradient_background(image, primary, secondary):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    # Linear vertical gradient
    for y in range(height):
        ratio = y / height
        r = int(primary[0] * (1 - ratio) + secondary[0] * ratio)
        g = int(primary[1] * (1 - ratio) + secondary[1] * ratio)
        b = int(primary[2] * (1 - ratio) + secondary[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def generate_still(filename, template_type, title, subtitle):
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height))
    
    # Elegant corporate dark gradient (Navy slate theme)
    primary_color = (15, 23, 42)    # Slate 900
    secondary_color = (30, 41, 59)  # Slate 800
    accent_color = (56, 189, 248)   # Light blue / Sky 400
    text_color = (248, 250, 252)    # Near white / Slate 50
    
    draw_gradient_background(image, primary_color, secondary_color)
    draw = ImageDraw.Draw(image)
    
    # Fonts
    font_large = load_system_font(64)
    font_medium = load_system_font(36)
    font_small = load_system_font(24)
    
    # Draw thin decorative border (Safe Area)
    draw.rectangle([96, 54, width - 96, height - 54], outline=accent_color, width=2)
    
    # Logo Placeholder Icon
    logo_y = 350
    draw.ellipse([width//2 - 60, logo_y - 60, width//2 + 60, logo_y + 60], outline=accent_color, width=4)
    draw.text((width//2, logo_y), "AV", font=font_medium, fill=text_color, anchor="mm")
    
    # Text Placement
    if template_type == "logo":
        draw.text((width//2, 630), title.upper(), font=font_large, fill=text_color, anchor="mm")
        draw.text((width//2, 710), subtitle, font=font_small, fill=accent_color, anchor="mm")
        
    elif template_type == "snafu":
        draw.text((width//2, 560), "ATTENTION", font=font_small, fill=accent_color, anchor="mm")
        draw.text((width//2, 640), "TECHNICAL DIFFICULTIES", font=font_large, fill=text_color, anchor="mm")
        draw.text((width//2, 720), "PLEASE STAND BY. WE WILL RETURN MOMENTARILY.", font=font_medium, fill=text_color, anchor="mm")
        
    elif template_type == "start":
        draw.text((width//2, 560), "WELCOME", font=font_small, fill=accent_color, anchor="mm")
        draw.text((width//2, 640), title.upper(), font=font_large, fill=text_color, anchor="mm")
        draw.text((width//2, 720), "THE SESSION WILL BEGIN SHORTLY", font=font_medium, fill=text_color, anchor="mm")
        
    elif template_type == "intermission":
        draw.text((width//2, 560), "INTERMISSION", font=font_small, fill=accent_color, anchor="mm")
        draw.text((width//2, 640), "SESSION RESUMES SHORTLY", font=font_large, fill=text_color, anchor="mm")
        draw.text((width//2, 720), subtitle, font=font_medium, fill=text_color, anchor="mm")
        
    elif template_type == "qa":
        draw.text((width//2, 560), "LIVE Q&A", font=font_small, fill=accent_color, anchor="mm")
        draw.text((width//2, 640), "QUESTION & ANSWER SESSION", font=font_large, fill=text_color, anchor="mm")
        draw.text((width//2, 720), "Please submit your questions to the moderator.", font=font_medium, fill=text_color, anchor="mm")

    # Save
    filepath = os.path.join(LOOPS_DIR, filename)
    image.save(filepath)
    print(f"Generated backup still: {filepath}")

def main():
    generate_still("still_01_logo_placeholder.png", "logo", "Acme Corporate Event", "Staging & Still Store Reference Frame")
    generate_still("still_02_technical_difficulties.png", "snafu", "", "")
    generate_still("still_03_session_starting.png", "start", "General Keynote Session", "")
    generate_still("still_04_intermission.png", "intermission", "", "Thank you for your patience.")
    generate_still("still_05_qa_session.png", "qa", "", "")

if __name__ == "__main__":
    main()
