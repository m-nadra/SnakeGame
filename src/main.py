import pygame
from game import Game
from sys import exit


def main() -> None:
    """Main function to run the game"""

    game = Game()
    objects = game.renderer.object

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == SCREEN_UPDATE:
                objects.snake.move()
                if objects.isSnakeGotPoint():
                    objects.changePointPosition()
                    objects.snake.lengthen()
                    objects.score.update()
                if objects.isSnakeOutOfBounds() or objects.isSnakeColliding():
                    game.printGameOverScreen()
                game.drawObjects()

            if event.type == pygame.KEYDOWN:
                objects.snake.changeDirection(event.key)


if __name__ == "__main__":
    main()
