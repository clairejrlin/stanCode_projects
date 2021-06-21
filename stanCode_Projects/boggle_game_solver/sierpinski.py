"""
File: sierpinski.py
Name: Claire Lin
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: draw Sierpinski Triangle with lines.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the layers of the images.
	:param length: int, triangle length.
	:param upper_left_x: int, the start site of x.
	:param upper_left_y: int, the start site of y.
	:return: img, Sierpinski Triangle.
	"""
	if order == 0:
		pass
	else:
		triangle_left = GLine(upper_left_x, upper_left_y, upper_left_x+(length*0.5), upper_left_y+(length*0.866))
		triangle_right = GLine(upper_left_x+length, upper_left_y, upper_left_x+(length*0.5), upper_left_y+(length*0.866))
		triangle_upper = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		window.add(triangle_right)
		window.add(triangle_left)
		window.add(triangle_upper)
		pause(50)

		# Upper left
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)
		# Upper right
		sierpinski_triangle(order-1, length*0.5, upper_left_x+(length*0.5), upper_left_y)
		# Lower
		sierpinski_triangle(order-1, length*0.5, upper_left_x+(length*0.25), upper_left_y+(length*0.433))


if __name__ == '__main__':
	main()