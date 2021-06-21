"""
File: Bouncing ball
Name: Claire Lin
-------------------------
TODO: Let the ball jump and stop at the third clicking time.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 25
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
COUNT = 3

window = GWindow(500, 300, title='bouncing_ball.py')

click = True
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
window.add(ball, START_X, START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)


def bouncing(event):

    global VX, ball, GRAVITY, COUNT, click

    h = 0
    if COUNT > 0:
        while click:
            while True:
                click = False
                h += GRAVITY   # mimic the gravity.
                ball.move(VX, h)

                if ball.y <= 0 or ball.y + ball.height >= window.height:
                    h *= REDUCE   # mimic the friction force.
                    h = -h
                if ball.x > window.width:
                    COUNT -= 1
                    break
                pause(DELAY)
            ball = GOval(SIZE, SIZE)
            ball.filled = True
            ball.fill_color = 'black'
            window.add(ball, START_X, START_Y)

        click = True




if __name__ == "__main__":
    main()
