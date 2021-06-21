"""
File: blur.py
Name: Claire Lin
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original image.
    :return: SimpleImage, blurred image.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            x_start, x_end, y_start, y_end = -1, 1, -1, 1   # set the variable.

            if x == 0:      # set the variable when pixel reach the sides.
                x_start = 0
            if x == img.width-1:
                x_end = 0
            if y == 0:
                y_start = 0
            if y == img.height-1:
                y_end = 0

            count = 0
            new_red, new_blue, new_green = 0, 0, 0

            for org_x in range(x_start, x_end+1, 1):
                for org_y in range(y_start, y_end+1, 1):
                    org_pixel = img.get_pixel(x + org_x, y + org_y)
                    count += 1
                    new_red += org_pixel.red
                    new_green += org_pixel.green
                    new_blue += org_pixel.blue

            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = new_red/count
            new_pixel.green = new_green/count
            new_pixel.blue = new_blue/count
    return new_img


def main():
    """
    TODO: blur the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
