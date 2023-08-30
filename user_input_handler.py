class UserInputHandler:
    """
    A utility class for handling user input validation and retrieval.
    """

    @staticmethod
    def validate_color_value(value):
        """
        Validates if a color value is within the valid range (0-255).
        """
        return 0 <= value <= 255

    @staticmethod
    def get_integer_input(prompt):
        """
        Retrieves an integer input from the user after displaying the specified prompt.
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_color_input(prompt):
        """
        Retrieves a color input (black or white) from the user after displaying the specified prompt.
        """
        while True:
            color = input(prompt).strip().lower()
            if color in ("black", "white"):
                return color
            else:
                print("Invalid input. Please enter 'black' or 'white'.")

    @staticmethod
    def get_draw_input(prompt):
        """
        Retrieves a drawing input (rectangle, square, quit) from the user after displaying the specified prompt.
        """
        while True:
            drawing = input(prompt).strip().lower()
            if drawing in ("rectangle", "square", "quit"):
                return drawing
            else:
                print("Invalid input. Please enter 'rectangle' or 'square' or 'quit'.")
