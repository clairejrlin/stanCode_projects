"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is the game of breakout, users have 3 chances (life) to break all of the bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120   # 120 frames per second
NUM_LIVES = 3			  # Number of attempts


def main():

    live = NUM_LIVES
    graphics = BreakoutGraphics()
    graphics.set_speed()

    if live > 0:
        while True:
            pause(FRAME_RATE)   # Willie taught me how to set it.
            if live == 0:
                graphics.game_over()
                break

            if graphics.click:
                while True:
                    if graphics.total == 0:
                        graphics.congrats()
                        break
                    vx = graphics.get_x_speed()
                    vy = graphics.get_y_speed()
                    graphics.click = False

                    graphics.ball.move(vx, vy)
                    graphics.bouncing()   # Willie also helped me to debug it.

                    if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        live -= 1
                        graphics.life -= 1
                        graphics.left_life.text = 'Life: '+str(graphics.life)
                        graphics.get_ball()
                        break

                    # window system can't detect the ball velocity accurately, so set the functions. (by willie too XD)
                    elif graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.reverse_x()

                    elif graphics.ball.y <= 0:
                        graphics.reverse_y()

                    pause(FRAME_RATE)

    # Add animation loop here!


if __name__ == '__main__':
    main()
