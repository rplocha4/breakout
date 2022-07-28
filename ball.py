class Ball:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 5
        self.direcion_y = -1
        self.direcion_x = 1

    def move(self, game_info):
        self.x += self.speed * self.direcion_x
        self.y += self.speed * self.direcion_y

        self.detect_walls(game_info)

    def detect_walls(self, game_info):
        # hitting left wall
        if self.x <= self.radius:
            self.bounce_x()

        # hitting top wall
        if self.y <= self.radius:
            self.bounce_y()

        # hitting right wall
        if self.x >= game_info.WIDTH - self.radius:
            self.bounce_x()

        # hitting bottom wall
        if self.y >= game_info.HEIGHT - self.radius:
            self.stop_ball()

    def bounce_x(self):
        self.direcion_x *= -1

    def bounce_y(self):
        self.direcion_y *= -1

    def heading_left(self):
        return self.direcion_x == -1

    def heading_down(self):
        return self.direcion_y == 1

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
            if not self.heading_down() and int(self.y) - self.radius in range(int(brick.y) + brick.height - self.speed,
                                                                              int(brick.y) + brick.height) \
                    and int(self.x) in range(int(brick.x) - self.radius,
                                             int(brick.x) + brick.width + self.radius):
                self.bounce_y()
                return brick
            # hitting brick from top
            elif self.heading_down() and int(self.y) + self.radius in range(int(brick.y) - self.speed, int(brick.y)) \
                    and int(self.x) in range(int(brick.x) - self.radius,
                                             int(brick.x) + brick.width + self.radius):
                self.bounce_y()
                return brick

            # hitting brick from left
            elif not self.heading_left() and int(self.y) in range(int(brick.y) - self.radius,
                                                                  int(brick.y) + brick.height + self.radius) \
                    and int(self.x) + self.radius in range(int(brick.x) - self.speed, int(brick.x)):
                self.bounce_x()
                return brick

            # hitting brick from right
            elif self.heading_left() and int(self.y) in range(int(brick.y) - self.radius,
                                                              int(brick.y) + brick.height + self.radius) \
                    and int(self.x) - self.radius in range(int(brick.x) + brick.width - self.speed,
                                                           int(brick.x) + brick.width):
                self.bounce_x()
                return brick
