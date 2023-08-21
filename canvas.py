import os

import numpy as np
from PIL import Image


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
        os.chdir("files")
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)
