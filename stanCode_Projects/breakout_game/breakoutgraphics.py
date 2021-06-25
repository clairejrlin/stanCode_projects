"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

The setting of the Breakout.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).

BALL_RADIUS = 10  # Radius of the ball (in pixels).

PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.total = BRICK_ROWS * BRICK_COLS

        # Create a graphical window, with some extra space------------------------------------------
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle---------------------------------------------------------------------------
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=(window_height - paddle_offset))
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window----------------------------------------------
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(window_width - (ball_radius * 2)) / 2,
                          y=(window_height - (ball_radius * 2)) / 2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball-----------------------------------------------------
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners------------------------------------------------------------
        self.click = False
        onmouseclicked(self.ball_start_run)
        onmousemoved(self.paddle_move)

        # Draw bricks ------------------------------------------------------------------------------
        self.draw_bricks()

        # Score broad ------------------------------------------------------------------------------
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-10'
        self.window.add(self.score_label, self.window.width - self.score_label.width*1.5,
                        self.window.height-self.score_label.height)

        # Life broad --------------------------------------------------------------------------------
        self.life = 3
        self.left_life = GLabel('Life: '+str(self.life))
        self.left_life.font = '-10'
        self.window.add(self.left_life, self.left_life.width/2,
                        self.window.height - self.left_life.height)

    # Instance Methods ------------------------------------
    def paddle_move(self, mouse):

        self.paddle.x = mouse.x - self.paddle.width / 2
        if mouse.x >= self.window.width - (self.paddle.width / 2):
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x < self.paddle.width / 2:
            self.paddle.x = 0

        self.paddle.y = self.window.height - PADDLE_OFFSET

    def ball_start_run(self, run):
        if self.ball.x == ((self.window.width - self.ball.height) / 2) and self.ball.y == (
                (self.window.height - self.ball.height) / 2):
            self.click = True

    def set_speed(self):  # Setter
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_x_speed(self):  # Getter of __dx
        return self.__dx

    def get_y_speed(self):  # Getter of __dy
        return self.__dy

    def reverse_x(self):   # Getter of -__dx
        self.__dx = -self.__dx

    def reverse_y(self):   # Getter of -__dy
        self.__dy = -self.__dy

    def get_ball(self):
        # self.ball = GOval(self.ball.width, self.ball.width, x=(self.window.width - self.ball.width) / 2,
        #                   y=(self.window.height - self.ball.height) / 2)
        # self.ball.filled = True
        # self.ball.color = 'black'
        # self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def bouncing(self):

        top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        top_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        bottom_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        bottom_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if bottom_left is not None:
            if bottom_left is self.paddle:
                self.__dy = -self.__dy
                self.ball.y = self.paddle.y-self.ball.height
            elif bottom_left is self.score_label:
                pass
            elif bottom_left is self.left_life:
                pass
            else:
                self.__dy = -self.__dy
                self.window.remove(bottom_left)
                self.total -= 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)

        elif bottom_right is not None:
            if bottom_right is self.paddle:
                self.__dy = -self.__dy
            elif bottom_right is self.score_label:
                pass
            elif bottom_right is self.left_life:
                pass
            else:
                self.__dy = -self.__dy
                self.window.remove(bottom_right)
                self.total -= 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)

        elif top_right is not None:
            if top_right is self.paddle:
                self.__dy = -self.__dy
            elif top_right is self.score_label:
                pass
            elif top_right is self.left_life:
                pass
            else:
                self.__dy = -self.__dy
                self.window.remove(top_right)
                self.total -= 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)

        elif top_left is not None:
            if top_left is self.paddle:
                self.__dy = -self.__dy
            elif top_left is self.score_label:
                pass
            elif top_left is self.left_life:
                pass
            else:
                self.__dy = -self.__dy
                self.window.remove(top_left)
                self.total -= 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)

    def game_over(self):
        self.over = GLabel('Game Over QAQ')
        self.over.font = '-20'
        self.window.add(self.over, (self.window.width - self.over.width)/2,
                        (self.window.height - self.over.height)/2)

    def congrats(self):
        self.finish = GLabel('Congrats!')
        self.finish.font = '-20'
        self.window.add(self.finish, (self.window.width - self.finish.width) / 2,
                        (self.window.height - self.finish.height) / 2)

    def draw_bricks(self):
        for x in range(self.brick_rows):
            for y in range(self.brick_cols):

                if x // 2 == 0:
                    self.brick = GRect(self.brick_width, self.brick_height)
                    self.brick.filled = True
                    self.brick.color = 'wheat'
                    self.brick.fill_color = 'wheat'
                    self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                                    (self.brick_height + self.brick_spacing) * x)

                elif x // 2 == 1:
                    self.brick = GRect(self.brick_width, self.brick_height)
                    self.brick.filled = True
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                    self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                                    (self.brick_height + self.brick_spacing) * x)

                elif x // 2 == 2:
                    self.brick = GRect(self.brick_width, self.brick_height)
                    self.brick.filled = True
                    self.brick.color = 'darkorange'
                    self.brick.fill_color = 'darkorange'
                    self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                                    (self.brick_height + self.brick_spacing) * x)

                elif x // 2 == 3:
                    self.brick = GRect(self.brick_width, self.brick_height)
                    self.brick.filled = True
                    self.brick.color = 'coral'
                    self.brick.fill_color = 'coral'
                    self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                                    (self.brick_height + self.brick_spacing) * x)

                else:
                    self.brick = GRect(self.brick_width, self.brick_height)
                    self.brick.filled = True
                    self.brick.color = 'salmon'
                    self.brick.fill_color = 'salmon'
                    self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                                    (self.brick_height + self.brick_spacing) * x)

                # else:
                #     self.brick = GRect(self.brick_width, self.brick_height)
                #     self.brick.filled = True
                #     self.brick.color = 'black'
                #     self.brick.fill_color = 'black'
                #     self.window.add(self.brick, (self.brick_width + self.brick_spacing) * y,
                #                     (self.brick_height + self.brick_spacing) * x)
