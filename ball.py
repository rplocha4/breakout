

class Ball:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 3
        self.direcion_y = -1
        self.direcion_x = 1

    def move(self, window_width, window_height):
        self.x += self.speed * self.direcion_x
        self.y += self.speed * self.direcion_y
        if self.x <= self.radius:
            self.bounce_x()
        if self.y <= self.radius:
            self.bounce_y()

        if self.x >= window_width - self.radius:
            self.bounce_x()
        # if self.y >= window_height - self.radius:
        #     self.bounce_y()

    def bounce_x(self):
        self.direcion_x *= -1

    def bounce_y(self):
        self.direcion_y *= -1

    def direction_left(self):
        return self.direcion_x == -1


