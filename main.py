import numpy as np
from PIL import Image


class Rectangle:
    """
    A class representing a rectangle shape.

    Attributes:
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        height (int): The height of the rectangle.
        width (int): The width of the rectangle.
        color (tuple): The color of the rectangle in RGB format.
    """

    def __init__(self, x, y, height, width, color):
        """
        Initialize a rectangle.

        Args:
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            height (int): The height of the rectangle.
            width (int): The width of the rectangle.
            color (tuple): The color of the rectangle in RGB format.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """
        Draw the rectangle on the canvas.

        Args:
            canvas (Canvas): The canvas on which to draw the rectangle.
        """
        x_start = int(self.x)
        y_start = int(self.y)
        x_end = int(self.x + self.width)
        y_end = int(self.y + self.height)
        canvas.data[y_start: y_end, x_start: x_end] = self.color


class Square:
    """
    A class representing a square shape.

    Attributes:
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        side (int): The length of each side of the square.
        color (tuple): The color of the square in RGB format.
    """

    def __init__(self, x, y, side, color):
        """
        Initialize a square.

        Args:
            x (int): The x-coordinate of the top-left corner of the square.
            y (int): The y-coordinate of the top-left corner of the square.
            side (int): The length of each side of the square.
            color (tuple): The color of the square in RGB format.
        """
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
        Draw the square on the canvas.

        Args:
            canvas (Canvas): The canvas on which to draw the square.
        """
        x_start = int(self.x)
        y_start = int(self.y)
        x_end = int(self.x + self.side)
        y_end = int(self.y + self.side)
        canvas.data[y_start: y_end, x_start: x_end] = self.color



class Canvas:
    """
    A class representing a canvas for drawing shapes.

    Attributes:
        width (int): The width of the canvas.
        height (int): The height of the canvas.
        color (tuple): The background color of the canvas in RGB format.
        data (numpy.ndarray): The pixel data of the canvas.
    """

    def __init__(self, width, height, color):
        """
        Initialize a canvas.

        Args:
            width (int): The width of the canvas.
            height (int): The height of the canvas.
            color (tuple): The background color of the canvas in RGB format.
        """
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Save the canvas as an image file.

        Args:
            imagepath (str): The path where the image will be saved.
        """
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


# Get canvas dimensions and color from user input
canvas_width = int(input("Canvas width: "))
canvas_height = int(input("Canvas height: "))
canvas_color = input("What color should be the canvas? (black or white)?: ")

# Determine canvas color based on user input
if canvas_color == "white":
    color = (255,255,255)
elif canvas_color == "black":
    color = (0,0,0)

# Create a canvas object with the specified dimensions and color
canvas = Canvas(canvas_width, canvas_height, color=color)

# Loop to allow drawing shapes on the canvas
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
        # Save the canvas as an image file and exit the loop
        canvas.make("canvas.png")
        break

