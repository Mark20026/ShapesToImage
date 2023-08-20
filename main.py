import numpy as np
from PIL import Image


class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)

        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


canvas = Canvas(200, 300, color=(255, 255, 255))

rectangle = Rectangle(10, 20, 20, 30, color=(255, 0, 0))
rectangle.draw(canvas)

square = Square(10, 30, 50, (56, 25, 194))
square.draw(canvas)

canvas.make("asd.png")
