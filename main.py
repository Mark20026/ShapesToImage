from canvas import Canvas
from shapes import Rectangle, Square


class UserInputHandler:
    @staticmethod
    def validate_color_value(value):
        return 0 <= value <= 255

    @staticmethod
    def get_integer_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_color_input(prompt):
        while True:
            color = input(prompt).strip().lower()
            if color in ("black", "white"):
                return color
            else:
                print("Invalid input. Please enter 'black' or 'white'.")

    @staticmethod
    def get_draw_input(prompt):
        while True:
            drawing = input(prompt).strip().lower()
            if drawing in ("rectangle", "square", "quit"):
                return drawing
            else:
                print("Invalid input. Please enter 'rectangle' or 'square' or 'quit'.")


user_input_handler = UserInputHandler()

# Get canvas dimensions and color from user input
canvas_width = user_input_handler.get_integer_input("Canvas width: ")
canvas_height = user_input_handler.get_integer_input("Canvas height: ")
canvas_color = user_input_handler.get_color_input("What color should be the canvas? (black or white)?: ")

# Determine canvas color based on user input
if canvas_color == "white":
    color = (255, 255, 255)
elif canvas_color == "black":
    color = (0, 0, 0)

# Create a canvas object with the specified dimensions and color
canvas = Canvas(int(canvas_width), int(canvas_height), color=color)

# Loop to allow drawing shapes on the canvas
while True:
    user_draw = user_input_handler.get_draw_input("What do you want to draw (square or rectangle)?"
                                                  "If you want to quit enter quit : ")

    if user_draw == "square":
        square_x = user_input_handler.get_integer_input("x coordinate: ")
        square_y = user_input_handler.get_integer_input("y coordinate: ")
        square_side = user_input_handler.get_integer_input("Side length: ")

        square_red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(square_red):
            print("Red value should be between 0 and 255.")
            square_red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")

        square_green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(square_green):
            print("Green value should be between 0 and 255.")
            square_green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")

        square_blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(square_blue):
            print("Blue value should be between 0 and 255.")
            square_blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")

        square = Square(square_x, square_y, square_side, color=(square_red, square_green, square_blue))
        square.draw(canvas)

    elif user_draw == "rectangle":
        rectangle_x = user_input_handler.get_integer_input("x coordinate: ")
        rectangle_y = user_input_handler.get_integer_input("y coordinate: ")
        rectangle_width = user_input_handler.get_integer_input("Width: ")
        rectangle_height = user_input_handler.get_integer_input("Height: ")

        rectangle_red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(rectangle_red):
            print("Red value should be between 0 and 255.")
            square_red = user_input_handler.get_integer_input("How much red should be in it?: (0-255)")

        rectangle_green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(rectangle_green):
            print("Green value should be between 0 and 255.")
            square_green = user_input_handler.get_integer_input("How much green should be in it?: (0-255)")

        rectangle_blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")
        while not user_input_handler.validate_color_value(rectangle_blue):
            print("Blue value should be between 0 and 255.")
            square_blue = user_input_handler.get_integer_input("How much blue should be in it?: (0-255)")

        rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_height, rectangle_width, color=(rectangle_red,
                                                                                                  rectangle_green,
                                                                                                  rectangle_blue))
        rectangle.draw(canvas)

    elif user_draw == "quit":
        # Save the canvas as an image file and exit the loop
        canvas.make("canvas.png")
        break



