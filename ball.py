class Ball:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 3
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

    def direction_left(self):
        return self.direcion_x == -1

    def stop_ball(self):
        self.speed = 0

    def detect_brick(self, bricks, game_info):
        # if int(self.x) - self.radius == int(brick.x):
        #     if int(self.y) in range(int(brick.y), int(brick.y) + brick.height):
        #         self.bounce_x()
        # if int(self.x) - self.radius == int(brick.x) + brick.width:
        #     if int(self.y) in range(int(brick.y), int(brick.y )+ brick.height):
        #         self.bounce_x()

        # hitting brick from bottom
        for brick in bricks:
            if int(self.y) - self.radius in range( int(brick.y) + brick.height - 5, int(brick.y) + brick.height) and \
                    int(self.x) in range(int(brick.x), int(brick.x) + brick.width):
                self.bounce_y()
