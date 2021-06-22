"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, original image.
    :return img: SimpleImage, 0.5x size of original image.
    """
    original = SimpleImage("images/poppy.png")
    blank_img = SimpleImage.blank(original.width//2, original.height//2)

    for x in range(0, original.width, 2):
        for y in range(0, original.height, 2):
            pixel = original.get_pixel(x, y)
            new_pixel = blank_img.get_pixel(x//2, y//2)

            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    return blank_img


def main():
    """
    TODO: smaller the images.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
