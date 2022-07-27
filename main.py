import pygame
from ball import Ball
from palette import Palette

pygame.init()


WIDTH, HEIGHT = 600, 600
BALL_RADIUS = 15
PALETTE_WIDTH = 200
PALETTE_HEIGHT = 20
BALL_COLOR = 'white'
PALETTE_COLOR = 'white'

WINDOW_BACKGROUND_COLOR = 'black'
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(WINDOW_BACKGROUND_COLOR)

pygame.display.set_caption("BREAKOUT")


def draw(ball, palette):
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    pygame.draw.circle(WINDOW, ball.color, (ball.x, ball.y), ball.radius)

    pygame.draw.rect(WINDOW, palette.color, pygame.Rect(palette.x, palette.y, palette.width, palette.height))


def main():
    clock = pygame.time.Clock()
    run = True
    ball = Ball(BALL_COLOR, WIDTH/3, HEIGHT/2, BALL_RADIUS)
    palette = Palette(PALETTE_COLOR, WIDTH/2 - PALETTE_WIDTH/2, HEIGHT - PALETTE_HEIGHT - 5, PALETTE_HEIGHT, PALETTE_WIDTH)

    while run:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        new_x = mouse[0] - palette.width/2
        palette.move(new_x, WIDTH)
        palette.detect_ball(ball, HEIGHT)

        ball.move(WIDTH, HEIGHT)
        draw(ball, palette)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
