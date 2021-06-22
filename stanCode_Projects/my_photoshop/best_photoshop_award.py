"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.25

# Controls black pixel
BLACK_PIXEL = 0


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """

    for x in range(0, me.width, 6):   # to smaller my figure.
        for y in range(0, me.height, 6):
            pixel = me.get_pixel(x, y)
            bg_pixel = bg.get_pixel((x+3500) // 6, (y+450) // 6)   # to put claire at the other site .

            avg = (pixel.red + pixel.blue + pixel.green) // 3
            total = pixel.red + pixel.blue + pixel.green
            if pixel.green < avg * THRESHOLD and total > BLACK_PIXEL:   # remove the green background.
                bg_pixel.red = pixel.red
                bg_pixel.green = pixel.green
                bg_pixel.blue = pixel.blue
    return bg


def main():
    """
    TODO: Claire wants to go machu picchu so much.
    """
    me = SimpleImage('image_contest/claire.jpg')
    bg = SimpleImage('image_contest/machu.jpg')

    combined_img = combine(bg, me)
    combined_img.show()


if __name__ == '__main__':
    main()
