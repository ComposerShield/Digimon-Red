import argparse
import sys
from PIL import Image

# Create an argument parser object
parser = argparse.ArgumentParser()

parser.add_argument("--width", type=int, default=48, help="width of the output image")
parser.add_argument("--height", type=int, default=48, help="height of the output image")
parser.add_argument("--image", help="input image")

# Parse the command-line arguments
args = parser.parse_args()

# Open the image file
try:
    image = Image.open(args.image).convert("RGBA")
except:
    print("Failed to open image.")
    sys.exit()

# Get the current width and height of the image
width, height = image.size

## Calculate the new size of the image
if width > height:
    new_size = (height, height)
else:
    new_size = (width, width)

# Create a new image with the new size and white background
new_image = Image.new("RGBA", new_size, (255, 255, 255, 255))

# Paste the original image into the new image
x = (new_size[0] - width) // 2
y = (new_size[1] - height) // 2
new_image.paste(image, (x, y), mask=image)

width = args.width
height = args.height

# Rescale image
new_image = new_image.resize((width,height), resample = Image.BICUBIC)

# Convert to greyscale
new_image = new_image.convert("L")

## Reduce bit depth
#new_image = new_image.point(lambda x: x // 64 * 64)
# Convert the image to a 2-bit palette image
#new_image = new_image.convert("P", palette=Image.ADAPTIVE, colors=4)
new_image = new_image.quantize(colors=4)

# Get the original filename and add _grey before the file extension
file_name = args.image.split(".")[0]
new_file_name = file_name + "_grey.png"

# Save the new image
new_image.save(new_file_name)

