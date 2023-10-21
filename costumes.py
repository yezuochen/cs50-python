import sys

from PIL import Image

Images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    Images.append(image)

Images[0].save(
    "costumes.gif", save_all=True, append_images=[Images[1]], duration=200, loop=0
)