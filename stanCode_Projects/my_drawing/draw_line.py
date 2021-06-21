"""
File: Draw line
Name: Claire Lin
-------------------------
TODO: To let the user can draw a line with their mouse.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
first_hole = True
window = GWindow()

first_x = 0   # set the point site.
first_y = 0
second_x = 0
second_y = 0
count = 0   # to check the point.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):

    global first_x, first_y, second_x, second_y, count

    count += 1

    if count % 2 == 1:   # first point
        hole = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        hole.filled = False
        window.add(hole)
        first_x = hole.x
        first_y = hole.y

    elif count % 2 == 0:   # second point

        pick = window.get_object_at(first_x+SIZE/2, first_y+SIZE/2)
        if pick is not None:
            window.remove(pick)

        line = GLine(first_x+SIZE/2, first_y+SIZE/2, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
