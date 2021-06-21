"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: To output the images without passengers.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    sum_red, sum_green, sum_blue = 0, 0, 0
    for pixel in pixels:
        sum_red += pixel.red
        sum_green += pixel.green
        sum_blue += pixel.blue
    red = sum_red // len(pixels)
    green = sum_green // len(pixels)
    blue = sum_blue // len(pixels)
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """

    avg = get_average(pixels)
    b_pixel_dist = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])   # Willie taught me XD
    best_pixel = pixels[0]   # set the first image's color distance and pixel.

    for pixel in pixels:
        dist_value = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist_value < b_pixel_dist:
            b_pixel_dist = dist_value
            best_pixel = pixel
    return best_pixel

    # I tried to use list before... -----------------------------
    # d = []
    # for pixel in pixels:
    #   dist_value = get_pixel_dist(pixel, red, green, blue)
    #   d.append(dist_value)
    # best_value = min(d, key=lambda p: p[1])
    # return best_value


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for x in range(width):
        for y in range(height):
            img_list = []
            for image in images:
                pixel = image.get_pixel(x, y)
                img_list.append(pixel)
            best = get_best_pixel(img_list)

            blank = result.get_pixel(x, y)   # fill the blank with best pixel.
            blank.red = best.red
            blank.green = best.green
            blank.blue = best.blue

    print("Displaying image!")
    result.show()

    # ####### YOUR CODE STARTS HERE ######## #
    # Write code to populate image and create the 'ghost' effect

    # checkpoint 1: color_distance -----------------------------------------------------------
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # checkpoint 2: get_average --------------------------------------------------------------
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # checkpoint 3: get_best_pixel -----------------------------------------------------------
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # ####### YOUR CODE ENDS HERE ########## #


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):  # listdir: Return a list containing the names of the files in the directory.
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames
    # somehow .jpg 'name' had been read.


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)  # print the filenames
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
