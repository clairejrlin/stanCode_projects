"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    TODO: to highlight the fires which were detected.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: SimpleImage, original image.
    :return: SimpleImage, the fire part were replaced in red pixel, others replaced into gray-scaled.
    """
    original_fire = SimpleImage('images/greenland-fire.png')

    for x in range(original_fire.width):
        for y in range(original_fire.height):

            pixel = original_fire.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue)//3

            if pixel.red > avg*HURDLE_FACTOR:   # fill the fire place with red pixel.
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = avg   # grayscale
                pixel.green = avg
                pixel.blue = avg
    return original_fire


if __name__ == '__main__':
    main()
