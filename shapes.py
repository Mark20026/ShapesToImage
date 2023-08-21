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
