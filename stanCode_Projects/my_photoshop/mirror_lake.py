"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    TODO: to make a new image the creates a mirror lake.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename: SimpleImage, original image.
    :return: SimpleImage, original image with reflected new one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    blank_img = SimpleImage.blank(original_mt.width, original_mt.height*2)

    for x in range(original_mt.width):
        for y in range(original_mt.height):

            color_p = original_mt.get_pixel(x, y)
            b_p1 = blank_img.get_pixel(x, y)
            b_p2 = blank_img.get_pixel(x, blank_img.height-1-y)

            b_p1.red = color_p.red
            b_p1.green = color_p.green
            b_p1.blue = color_p.blue

            b_p2.red = color_p.red
            b_p2.green = color_p.green
            b_p2.blue = color_p.blue

    return blank_img


if __name__ == '__main__':
    main()
