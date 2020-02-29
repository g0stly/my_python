import random
import collections
from PIL import ImageDraw, Image

image = Image.open('LAB1/roof.jpg')
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

histogram = 256*[0]

for x in range(width):
    for y in range(height):
        histogram[pix[x, y][1]] += 1

max_value = max(histogram.values())


for x in range(256):
    for y in range():
        draw.point()




image.show()
del draw
