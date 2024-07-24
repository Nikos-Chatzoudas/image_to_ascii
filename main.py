import os
from PIL import Image, ImageDraw, ImageFont

def image_to_ascii(image_path, output_path, font_path, resolution_factor):
    # Open image and convert to grayscale
    image = Image.open(image_path).convert('L')
    
    # Resize image for better ASCII representation
    width, height = image.size
    aspect_ratio = height / float(width)
    new_width = width // resolution_factor
    new_height = int(aspect_ratio * new_width * 0.55)
    image = image.resize((new_width, new_height))
    
    # Define ASCII characters based on grayscale intensity
    ascii_chars = "@%#*+=-:. "
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // 32]
    
    # Split the ASCII string into multiple lines
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i + new_width] + "\n"
    
    # Create a new image with the same size as the ASCII art
    font = ImageFont.truetype(font_path, 10)
    draw = ImageDraw.Draw(Image.new("L", (1, 1)))
    bbox = draw.textbbox((0, 0), ascii_img, font=font)
    ascii_width = bbox[2] - bbox[0]
    ascii_height = bbox[3] - bbox[1]
    
    ascii_image = Image.new("L", (ascii_width, ascii_height), 255)
    draw = ImageDraw.Draw(ascii_image)
    draw.text((0, 0), ascii_img, font=font, fill=0)
    
    # Save the new image
    ascii_image.save(output_path)

if __name__ == "__main__":
    # Get the current directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Input paths and resolution factor
    image_path = input("Enter the path to the image: ")
    resolution_factor = int(input("Enter the resolution factor (e.g., 1 for 1 char per pixel, 2 for 4 chars per pixel, 3 for 9 chars per pixel): "))
    output_filename = "ascii_art.png"
    output_path = os.path.join(script_dir, output_filename)
    font_path = os.path.join(script_dir, "Monaco.ttf")  # Assuming Monaco font is in the same directory
    
    if not os.path.isfile(font_path):
        print(f"Font file {font_path} not found.")
    else:
        image_to_ascii(image_path, output_path, font_path, resolution_factor)
        print(f"ASCII art saved to {output_path}")
