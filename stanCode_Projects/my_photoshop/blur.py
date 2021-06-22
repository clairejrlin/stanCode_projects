"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original image.
    :return: SimpleImage, blurred image.
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):

            if (img.width - 1) > x >= 1 and (img.height - 1) > y >= 1:   # for the pixel inside.
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_6 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)

                avg_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_start.red + pixel_6.red +
                           pixel_7.red + pixel_8.red + pixel_9.red) // 9
                avg_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_start.green +
                             pixel_6.green + pixel_7.green + pixel_8.green + pixel_9.green) // 9
                avg_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_start.blue +
                            pixel_6.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) // 9

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == 0 and (img.height - 1) > y >= 1:   # for pixel which were on the left edge.
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_6 = img.get_pixel(x + 1, y)
                pixel_8 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_2.red + pixel_3.red + pixel_start.red + pixel_6.red + pixel_8.red + pixel_9.red) // 6
                avg_green = (pixel_2.green + pixel_3.green + pixel_start.green + pixel_6.green + pixel_8.green +
                             pixel_9.green) // 6
                avg_blue = (pixel_2.blue + pixel_3.blue + pixel_start.blue + pixel_6.blue + pixel_8.blue +
                            pixel_9.blue) // 6

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif (img.width - 1) > x >= 1 and y == 0:   # for pixel which were on the top edge.
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_6 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_4.red + pixel_start.red + pixel_6.red + pixel_7.red + pixel_8.red + pixel_9.red) // 6
                avg_green = (pixel_4.green + pixel_start.green + pixel_6.green + pixel_7.green + pixel_8.green +
                             pixel_9.green) // 6
                avg_blue = (pixel_4.blue + pixel_start.blue + pixel_6.blue + pixel_7.blue + pixel_8.blue +
                            pixel_9.blue) // 6

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == img.width - 1 and (img.height - 1) > y >= 1:   # for pixel which were on the right edge.
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_1.red + pixel_2.red + pixel_4.red + pixel_start.red + pixel_7.red + pixel_8.red) // 6
                avg_green = (pixel_1.green + pixel_2.green + pixel_4.green + pixel_start.green + pixel_7.green +
                             pixel_8.green) // 6
                avg_blue = (pixel_1.blue + pixel_2.blue + pixel_4.blue + pixel_start.blue + pixel_7.blue +
                            pixel_8.blue) // 6

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif (img.width - 1) > x >= 1 and y == img.height - 1:   # for pixel which were on the bottom edge.
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_6 = img.get_pixel(x + 1, y)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_start.red + pixel_6.red) // 6
                avg_green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_start.green +
                             pixel_6.green) // 6
                avg_blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_start.blue +
                            pixel_6.blue) // 6

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == 0 and y == 0:  # for pixel in the corner (0, 0).
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_6 = img.get_pixel(x + 1, y)
                pixel_8 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_start.red + pixel_6.red + pixel_8.red + pixel_9.red) // 4
                avg_green = (pixel_start.green + pixel_6.green + pixel_8.green + pixel_9.green) // 4
                avg_blue = (pixel_start.blue + pixel_6.blue + pixel_8.blue + pixel_9.blue) // 4

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == img.width - 1 and y == 0:   # for pixel in the corner (x, 0).
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_7 = img.get_pixel(x - 1, y + 1)
                pixel_8 = img.get_pixel(x, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_4.red + pixel_start.red + pixel_7.red + pixel_8.red) // 4
                avg_green = (pixel_4.green + pixel_start.green + pixel_7.green + pixel_8.green) // 4
                avg_blue = (pixel_4.blue + pixel_start.blue + pixel_7.blue + pixel_8.blue) // 4

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == 0 and y == img.height - 1:   # for pixel in the corner (0, y).
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_6 = img.get_pixel(x + 1, y)
                new_pixel = new_img.get_pixel(x, y)
                avg_red = (pixel_2.red + pixel_3.red + pixel_start.red + pixel_6.red) // 4
                avg_green = (pixel_2.green + pixel_3.green + pixel_start.green + pixel_6.green) // 4
                avg_blue = (pixel_2.blue + pixel_3.blue + pixel_start.blue + pixel_6.blue) // 4

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

            elif x == img.width - 1 and y == img.height - 1:   # for pixel in the corner (x, y).
                pixel_start = img.get_pixel(x, y)  # pixel_5
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                new_pixel = new_img.get_pixel(x, y)

                avg_red = (pixel_1.red + pixel_2.red + pixel_4.red + pixel_start.red) // 4
                avg_green = (pixel_1.green + pixel_2.green + pixel_4.green + pixel_start.green) // 4
                avg_blue = (pixel_1.blue + pixel_2.blue + pixel_4.blue + pixel_start.blue) // 4

                new_pixel.red = avg_red
                new_pixel.green = avg_green
                new_pixel.blue = avg_blue

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
