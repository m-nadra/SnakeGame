import pygame
from objects import Point, Snake, Score
from pygame.math import Vector2
from sys import exit

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_SIZE = 50


def main() -> None:
    """Window setup and main loop."""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Snake Game")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    point = Point()
    score = Score()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == SCREEN_UPDATE:
                snake.move()
                if snake.body[0] == point.position:
                    point.position = point.generateRandomPosition()
                    snake.lengthen()
                    score.update()
                if snake.isOutOfBounds() or snake.isColliding():
                    pygame.quit()
                    exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake.direction.y != -snake.size:
                    snake.direction = Vector2(0, snake.size)
                if event.key == pygame.K_UP and snake.direction.y != snake.size:
                    snake.direction = Vector2(0, -snake.size)
                if event.key == pygame.K_LEFT and snake.direction.x != snake.size:
                    snake.direction = Vector2(-snake.size, 0)
                if event.key == pygame.K_RIGHT and snake.direction.x != -snake.size:
                    snake.direction = Vector2(snake.size, 0)

        drawGrass(screen)
        snake.draw(screen)
        point.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        clock.tick(60)


def drawGrass(screen: pygame.Surface) -> None:
    for row in range(SCREEN_WIDTH // OBJECT_SIZE):
        for col in range(SCREEN_HEIGHT // OBJECT_SIZE):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (92, 237, 115),
                                 (row * OBJECT_SIZE, col * OBJECT_SIZE, OBJECT_SIZE, OBJECT_SIZE))
            else:
                pygame.draw.rect(screen, (57, 231, 95),
                                 (row * OBJECT_SIZE, col * OBJECT_SIZE, OBJECT_SIZE, OBJECT_SIZE))


if __name__ == "__main__":
    main()
