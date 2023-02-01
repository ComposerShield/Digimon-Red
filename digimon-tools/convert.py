import sys
from PIL import Image

# Open the image file
try:
    image = Image.open(sys.argv[1]).convert("RGBA")
except:
    print("Failed to open image.")
    sys.exit()

# Get the current width and height of the image
width, height = image.size

# Calculate the new size of the image
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

# Rescale image to 56x56
new_image = new_image.resize((48,48), resample = Image.BICUBIC)

# Convert to greyscale
new_image = new_image.convert("L")

# Reduce bit depth
new_image = new_image.point(lambda x: x // 64 * 64)

# Get the original filename and add _grey before the file extension
file_name = sys.argv[1].split(".")[0]
new_file_name = file_name + "_grey.png"

# Save the new image
new_image.save(new_file_name)

