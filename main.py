import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

members = [0] * 9


for i in range(0, width -1):
    for j in range(0, height - 1):
        r,g,b, = img.getpixel((i,j))
        new_img.putpixel((i,j), (254-r,254-g,254-b))

new_img.save(output_path)
