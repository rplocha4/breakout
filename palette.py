class Palette:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def move(self, new_x, game_info):
        if new_x >= 0 and new_x + self.width <= game_info.WIDTH:
            self.x = new_x

    def detect_ball(self, ball, game_info):
        if ball.y >= game_info.HEIGHT - self.height - ball.radius - 5:

            # ball in first half of paddle
            if int(ball.x) in range(int(self.x), int(self.x) + self.width // 2 + 1):

                if ball.heading_left():
                    ball.bounce_y()
                else:
                    ball.bounce_y()
                    ball.bounce_x()

            # ball in second half of paddle
            elif int(ball.x) in range(int(self.x) + self.width // 2, self.width + int(self.x)):
                if ball.heading_left():
                    ball.bounce_y()
                    ball.bounce_x()
                else:
                    ball.bounce_y()

    def calculate_new_x(self, mouse_x, game_info):
        if mouse_x < self.width / 2:
            new_x = 0
        elif mouse_x >= game_info.WIDTH - self.width / 2:
            new_x = game_info.WIDTH - self.width
        else:
            new_x = mouse_x - self.width / 2

        self.move(new_x, game_info)
