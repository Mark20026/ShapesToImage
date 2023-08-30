from canvas import Canvas
from shapes import Rectangle, Square
from user_input_handler import UserInputHandler

user_input_handler = UserInputHandler()


def get_color_components():
    # Get and validate the red color component
    red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")
    while not user_input_handler.validate_color_value(red):
        print("Red value should be between 0 and 255.")
        red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")

    # Get and validate the green color component
    green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")
    while not user_input_handler.validate_color_value(green):
        print("Green value should be between 0 and 255.")
        green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")

    # Get and validate the blue color component
    blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")
    while not user_input_handler.validate_color_value(blue):
        print("Blue value should be between 0 and 255.")
        blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")

    return red, green, blue


canvas_width = user_input_handler.get_integer_input("Canvas width: ")
canvas_height = user_input_handler.get_integer_input("Canvas height: ")
canvas_color = user_input_handler.get_color_input("What color should be the canvas? (black or white)?: ")

color = (255, 255, 255) if canvas_color == "white" else (0, 0, 0)

canvas = Canvas(int(canvas_width), int(canvas_height), color=color)

while True:
    user_draw = user_input_handler.get_draw_input("What do you want to draw (square or rectangle)?"
                                                  "If you want to quit enter quit : ")

    if user_draw == "quit":
        # Save the canvas as an image file and exit the loop
        canvas.make("canvas.png")
        break

    x = user_input_handler.get_integer_input("x coordinate: ")
    y = user_input_handler.get_integer_input("y coordinate: ")
    red, green, blue = get_color_components()

    if user_draw == "square":
        side = user_input_handler.get_integer_input("Side length: ")
        square = Square(x, y, side, color=(red, green, blue))
        square.draw(canvas)

    elif user_draw == "rectangle":
        width = user_input_handler.get_integer_input("Width: ")
        height = user_input_handler.get_integer_input("Height: ")
        rectangle = Rectangle(x, y, height, width, color=(red, green, blue))
        rectangle.draw(canvas)

