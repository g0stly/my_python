# Используйте этот файл, если Вам нужны просто цветные линии
# Для выполнения практической работы номер 2 используйте файл "triangleCheck.py"
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("bear.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def lineC(x1, y1, x2, y2, color):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1) # направление изменения Y
            for x in range(x1, x2 + 1):
                    draw.point((x,y),color)
                    err += dErr
                    if err + err >= dX: # если ошибка накопилась
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),color)
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY
black = (0,0,0)
green = (0,200,0)
red = (200,0,0)
blue = (0,0,200)
lineC(0,0,width-1,height-1, black)
lineC(0,height-1,width-1,0, black)
lineC(width//2,0,0,height//2, red)
lineC(width//2,height-1,0,height//2, red)

lineC(width//2,height-1,0,0, green)
lineC(width//2,0,width-1,height-1, blue)
lineC(width-1,0,width//2,height-1, green)
lineC(width//2,0,0,height-1, blue)
image.show()
#image.save("result.jpg")
del draw
