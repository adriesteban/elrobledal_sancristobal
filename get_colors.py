
from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=3):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        image = image.resize((150, 150))      # Resize for faster processing
        pixels = list(image.getdata())
        counts = Counter(pixels)
        dominant = counts.most_common(num_colors)
        
        print(f"Dominant colors for {image_path}:")
        for color, count in dominant:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            print(f"- {hex_color} (RGB: {color})")
            
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_dominant_colors(sys.argv[1])
    else:
        print("Usage: python get_colors.py <image_path>")
