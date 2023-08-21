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
        canvas.data[self.y: self.y + self.height, self.x: self.x + self.width] = self.color


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


canvas_width = int(input("Canvas width: "))
canvas_height = int(input("Canvas height: "))
canvas_color = input("What color should be the canvas? (black or white)?: ")

if canvas_color == "white":
    color = (255,255,255)
elif canvas_color == "black":
    color = (0,0,0)

canvas = Canvas(canvas_width, canvas_height, color=color)

while True:
    user_draw = input("What do you want to draw (square or rectangle)? If you want to quit enter quit : ")

    if user_draw == "square":
        square_x = int(input("x coordinate: "))
        square_y = int(input("y coordinate: "))
        square_side = int(input("Side length: "))
        square_red = int(input("How many red should be in it?: (0-255)"))
        square_green = int(input("How many green should be in it?: (0-255)"))
        square_blue = int(input("How many blue should be in it?: (0-255)"))

        square = Square(square_x, square_y, square_side, color=(square_red, square_green, square_blue))
        square.draw(canvas)

    elif user_draw == "rectangle":
        rectangle_x = int(input("x coordinate: "))
        rectangle_y = int(input("y coordinate: "))
        rectangle_width = int(input("Width: "))
        rectangle_height = int(input("Height: "))
        rectangle_red = int(input("How many red should be in it?: (0-255)"))
        rectangle_green = int(input("How many green should be in it?: (0-255)"))
        rectangle_blue = int(input("How many blue should be in it?: (0-255)"))

        rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_height, rectangle_width, color=(rectangle_red,
                                                                                                  rectangle_green,
                                                                                                  rectangle_blue))
        rectangle.draw(canvas)

    elif user_draw == "quit":
        canvas.make("canvas.png")
        break

