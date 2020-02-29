from PIL import ImageDraw, Image

image = Image.open('LAB1/roof.jpg')
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            q = x / width
            draw.point((x, y), (int(r * q), int(g * q), int(b * q)))

image.show()
del draw
