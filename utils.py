import math
from PIL import Image

import numpy as np


def mnist_square_grid(images):
    """
    Save images as a square grid
    :param images: Images to be used for the grid
    :param mode: The mode to use for images
    :return: Image of images in a square grid
    """
    # Get maximum size for square grid of images
    side_size = math.floor(np.sqrt(images.shape[0]))

    # Put images in a square arrangement
    stacked_rows = [np.hstack(images[i:i+side_size]) for i in np.arange(0, side_size**2, side_size)]
    square = np.vstack(stacked_rows)

    return square