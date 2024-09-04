import pygame
from game import Game
from sys import exit


def main() -> None:
    """Main function to run the game"""

    game = Game()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == SCREEN_UPDATE:
                game.snake.move()
                if game.isSnakeGotPoint():
                    game.point.changePosition()
                    game.snake.lengthen()
                    game.score.update()
                if game.isSnakeOutOfBounds() or game.isSnakeColliding():
                    game.gameOver()
                game.drawObjects()

            if event.type == pygame.KEYDOWN:
                game.snake.changeDirection(event.key)


if __name__ == "__main__":
    main()
