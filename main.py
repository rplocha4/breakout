import pygame
from ball import Ball
from palette import Palette
from brick import Brick

pygame.init()
pygame.display.set_caption("BREAKOUT")
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))


class GameInfo:
    WIDTH, HEIGHT = 1000, 600
    BALL_RADIUS = 8
    PALETTE_WIDTH = 300
    PALETTE_HEIGHT = 10
    BRICK_MARGIN_LEFT = 15
    BRICK_MARGIN_TOP = 15
    BRICK_HEIGHT = 30
    BRICK_WIDTH = 100
    BALL_COLOR = 'white'
    PALETTE_COLOR = 'blue'
    BRICK_COLOR = 'red'

    WINDOW_BACKGROUND_COLOR = 'black'
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)


def draw(ball, palette, bricks, game_info):
    game_info.WINDOW.fill(game_info.WINDOW_BACKGROUND_COLOR)
    pygame.draw.circle(game_info.WINDOW, ball.color, (ball.x, ball.y), ball.radius)

    pygame.draw.rect(game_info.WINDOW, palette.color, pygame.Rect(palette.x, palette.y, palette.width, palette.height),
                     border_radius=game_info.PALETTE_HEIGHT // 2)
    for brick in bricks:
        pygame.draw.rect(game_info.WINDOW, brick.color, pygame.Rect(brick.x, brick.y, brick.width, brick.height))


def create_bricks(num, game_info):
    bricks = [Brick(game_info.BRICK_COLOR, game_info.BRICK_MARGIN_LEFT, game_info.BRICK_MARGIN_TOP,
                    game_info.BRICK_WIDTH, game_info.BRICK_HEIGHT)]
    for i in range(num - 1):
        if 2 * game_info.BRICK_MARGIN_LEFT + bricks[-1].x + 2 * game_info.BRICK_WIDTH < game_info.WIDTH:
            bricks.append(Brick(game_info.BRICK_COLOR,
                          2 * game_info.BRICK_MARGIN_LEFT + bricks[-1].x + game_info.BRICK_WIDTH,
                          bricks[-1].y,
                          game_info.BRICK_WIDTH,
                          game_info.BRICK_HEIGHT))
        else:
            bricks.append(Brick(game_info.BRICK_COLOR,
                          game_info.BRICK_MARGIN_LEFT,
                          bricks[-1].y + game_info.BRICK_HEIGHT + game_info.BRICK_MARGIN_TOP,
                          game_info.BRICK_WIDTH,
                          game_info.BRICK_HEIGHT))

    return bricks


def main():
    game_info = GameInfo()
    clock = pygame.time.Clock()
    run = True
    ball = Ball(game_info.BALL_COLOR, game_info.WIDTH / 3, game_info.HEIGHT / 2, game_info.BALL_RADIUS)
    palette = Palette(game_info.PALETTE_COLOR, game_info.WIDTH / 2 - game_info.PALETTE_WIDTH / 2,
                      game_info.HEIGHT - game_info.PALETTE_HEIGHT - 5,
                      game_info.PALETTE_WIDTH, game_info.PALETTE_HEIGHT)
    bricks = create_bricks(8, game_info)

    while run:
        clock.tick(120)
        pygame.event.set_grab(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        mouse = pygame.mouse.get_pos()
        palette.calculate_new_x(mouse[0], game_info)
        palette.detect_ball(ball, game_info)

        ball.move(game_info)
        ball.detect_brick(bricks, game_info)
        draw(ball, palette, bricks, game_info)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
