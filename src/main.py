"""Main module of the game. It contains the main function that runs the game."""

import pygame
from game import GameProperties, Renderer
from sys import exit


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Snake Game")

    GameProperties.set(800, 600, 50)
    game = Renderer()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == SCREEN_UPDATE:
                game.object.snake.move()
                if game.object.isSnakeGotPoint():
                    game.object.update()
                if game.object.isSnakeOutOfBounds() or game.object.isSnakeColliding():
                    game.drawGameOverScreen()
                game.drawObjects()

            if event.type == pygame.KEYDOWN:
                game.object.snake.changeDirection(event.key)


if __name__ == "__main__":
    main()
