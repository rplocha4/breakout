class Palette:
    def __init__(self, color, x, y, height, width):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def move(self, new_x, window_width):
        if new_x >= 0 and new_x + self.width <= window_width:
            self.x = new_x

    def detect_ball(self, ball, window_height):
        if ball.y >= window_height - self.height - ball.radius:
            if ball.x in range(int(self.x), int(self.x) + self.width//2 + 1):
                if ball.direction_left():
                    ball.bounce_y()
                else:
                    ball.bounce_y()
                    ball.bounce_x()
            elif ball.x in range(int(self.x) + self.width//2, self.width + int(self.x) + self.width//2):
                if ball.direction_left():
                    ball.bounce_y()
                    ball.bounce_x()
                else:
                    ball.bounce_y()

