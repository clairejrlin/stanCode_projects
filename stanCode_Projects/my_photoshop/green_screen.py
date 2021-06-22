"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image.
    :param figure_img: SimpleImage, green screen figure image.
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image.
    """

    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_fig = figure_img.get_pixel(x, y)

            bigger = max(pixel_fig.red, pixel_fig.blue)
            if pixel_fig.green > bigger*2:   # remove green background
                new = background_img.get_pixel(x, y)
                pixel_fig.red = new.red
                pixel_fig.blue = new.blue
                pixel_fig.green = new.green
    return figure_img


def main():
    """
    TODO: to let the figure combine with the space ship image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
