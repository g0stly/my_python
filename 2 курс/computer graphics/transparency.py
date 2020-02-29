import random
from PIL import Image, ImageDraw

image1 = Image.open("LAB2/winter.jpg")
image2 = Image.open("LAB2/park.jpg")

draw = ImageDraw.Draw(image1)
width  = image1.size[0]
height = image1.size[1]
pix1 = image1.load()
pix2 = image2.load()

for x in range(width):
    for y in range(height):
        q = 

image.show()
del draw
