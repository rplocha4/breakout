class Ball:
    def __init__(self, color, x, y, radius, speed):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction_y = -1
        self.direction_x = 1
        self.hitted_wall = False
        self.hitted_palette = False

    def move(self, game_info):
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

        self.detect_walls(game_info)

    def detect_walls(self, game_info):
        if not self.hitted_wall:
            # hitting left wall
            if self.x <= self.radius:
                self.bounce_x()
                self.change_focus()

            # hitting top wall
            if self.y <= self.radius:
                self.bounce_y()
                self.change_focus()

            # hitting right wall
            if self.x >= game_info.WIDTH - self.radius:
                self.bounce_x()
                self.change_focus()

            # hitting bottom wall
            if self.y >= game_info.HEIGHT - self.radius:
                self.stop_ball()
                self.change_focus()

    def bounce_x(self):
        self.direction_x *= -1

    def bounce_y(self):
        self.direction_y *= -1

    def heading_left(self):
        return self.direction_x == -1

    def heading_down(self):
        return self.direction_y == 1

    def stop_ball(self):
        self.speed = 0

    def detect_brick(self, bricks):
        # if int(self.x) - self.radius == int(brick.x):
        #     if int(self.y) in range(int(brick.y), int(brick.y) + brick.height):
        #         self.bounce_x()
        # if int(self.x) - self.radius == int(brick.x) + brick.width:
        #     if int(self.y) in range(int(brick.y), int(brick.y )+ brick.height):
        #         self.bounce_x()

        for brick in bricks:
            # hitting brick from bottom
            if not self.heading_down() and int(self.y) - self.radius in range(int(brick.y) + brick.height - self.radius,
                                                                              int(brick.y) + brick.height) \
                    and int(self.x) in range(int(brick.x) - self.radius,
                                             int(brick.x) + brick.width + self.radius):
                self.bounce_y()
                self.remove_focus()
                return brick
            # hitting brick from top
            if self.heading_down() and int(self.y) + self.radius in range(int(brick.y) - self.radius, int(brick.y)) \
                    and int(self.x) in range(int(brick.x) - self.radius,
                                             int(brick.x) + brick.width + self.radius):
                self.bounce_y()
                self.remove_focus()
                return brick

            # hitting brick from left
            if not self.heading_left() and int(self.y) in range(int(brick.y) - self.radius,
                                                                  int(brick.y) + brick.height + self.radius) \
                    and int(self.x) + self.radius in range(int(brick.x) - self.radius, int(brick.x)):
                self.bounce_x()
                self.remove_focus()
                return brick

            # hitting brick from right
            if self.heading_left() and int(self.y) in range(int(brick.y) - self.radius,
                                                              int(brick.y) + brick.height + self.radius) \
                    and int(self.x) - self.radius in range(int(brick.x) + brick.width - self.radius,
                                                           int(brick.x) + brick.width):
                self.bounce_x()
                self.remove_focus()
                return brick

    def detect_palette(self, paddle, game_info):
        if not self.hitted_wall and self.y >= game_info.HEIGHT - paddle.height - self.radius - 5:

            # ball in first half of paddle
            if int(self.x) in range(int(paddle.x), int(paddle.x) + paddle.width // 2 + 1):

                if self.heading_left():
                    self.bounce_y()
                else:
                    self.bounce_y()
                    self.bounce_x()
                self.change_focus()

            # ball in second half of paddle
            elif int(self.x) in range(int(paddle.x) + paddle.width // 2, paddle.width + int(paddle.x)):
                if self.heading_left():
                    self.bounce_y()
                    self.bounce_x()
                else:
                    self.bounce_y()

                self.change_focus()

    def change_focus(self):
        if self.hitted_wall:
            self.hitted_palette = False
        if self.hitted_palette:
            self.hitted_wall = False

    def remove_focus(self):
        self.hitted_wall = False
        self.hitted_palette = False

