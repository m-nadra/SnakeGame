import pygame
from pygame.math import Vector2
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_SIZE = 50


class Point:
    def __init__(self) -> None:
        self.size = OBJECT_SIZE
        self.position = self.generateRandomPosition()
        self.color = 'red'

    def draw(self, screen: pygame.Surface) -> None:
        pointRect = pygame.Rect(
            self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, pointRect)

    def generateRandomPosition(self) -> Vector2:
        """
        Generate a random position for the object.
        Position is calculated by multiplying a random number between 0 and the screen width/height by the object size.
        This ensures that the objects are always in the grid and allow modifying game resolution.
        Returns:
            tuple: Position of the object, first element is width and second is height.
        """
        width = randint(0, (SCREEN_WIDTH//OBJECT_SIZE) - 1) * OBJECT_SIZE
        height = randint(0, (SCREEN_HEIGHT//OBJECT_SIZE) - 1) * OBJECT_SIZE
        return Vector2(width, height)


class Snake:
    def __init__(self) -> None:
        self.size = OBJECT_SIZE
        self.body = [Vector2(100, 100), Vector2(75, 100), Vector2(50, 100)]
        self.direction = Vector2()
        self.color = 'blue'

    def draw(self, screen: pygame.Surface) -> None:
        for pos in self.body:
            snakeRect = pygame.Rect(pos.x, pos.y, self.size, self.size)
            pygame.draw.rect(screen, self.color, snakeRect)

    def move(self) -> None:
        if self.direction != Vector2(0, 0):
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy

    def lengthen(self) -> None:
        self.body.append(self.body[-1])

    def isColliding(self) -> bool:
        return self.body[0] in self.body[1:]

    def isOutOfBounds(self) -> bool:
        return self.body[0].x < 0 or self.body[0].x >= SCREEN_WIDTH or self.body[0].y < 0 or self.body[0].y >= SCREEN_HEIGHT


class Score:
    def __init__(self) -> None:
        self.score = 0

    def update(self) -> None:
        self.score += 1

    def draw(self, screen: pygame.Surface) -> None:
        font = pygame.font.Font(None, 36)
        scoreText = font.render(f"Score: {self.score}", True, 'white')
        screen.blit(scoreText, (10, 10))
