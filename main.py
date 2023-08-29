from canvas import Canvas
from shapes import Rectangle, Square
import re


def wrong_input():
    return "Wrong input"


# Creating patterns for the canvas
canvas_width_pattern = re.compile(r'^\d{3,4}$')
canvas_height_pattern = re.compile(r'^\d{3,4}$')
canvas_color_pattern = re.compile(r'^black|white$', re.IGNORECASE)

# Get canvas dimensions and color from user input
while True:
    canvas_width = input("Canvas width: ")
    if canvas_width_pattern.match(canvas_width):
        break
    else:
        print("Give a number which has 3 or 4 numbers in it!")


while True:
    canvas_height = input("Canvas height: ")
    if canvas_height_pattern.match(canvas_height):
        break
    else:
        print("Give a number which has 3 or 4 numbers in it!")

while True:
    canvas_color = input("What color should be the canvas? (black or white)?: ")
    if canvas_color_pattern.match(canvas_color):
        break
    else:
        print("The input should be 'black' or 'white'!")

# Determine canvas color based on user input
if canvas_color == "white":
    color = (255,255,255)
elif canvas_color == "black":
    color = (0,0,0)

# Create a canvas object with the specified dimensions and color
canvas = Canvas(int(canvas_width), int(canvas_height), color=color)

# Creating pattern for the drawing
draw_pattern = re.compile(r'^square|rectangle|quit$', re.IGNORECASE)

# Loop to allow drawing shapes on the canvas
while True:
    while True:
        user_draw = input("What do you want to draw (square or rectangle)? If you want to quit enter quit : ")
        if draw_pattern.match(user_draw):
            break
        else:
            print("The input should be 'rectangle' or 'square'!")

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



