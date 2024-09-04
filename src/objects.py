import pygame
from pygame.math import Vector2
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OBJECT_SIZE = 50


class Point:
    def __init__(self, size) -> None:
        self.size = size
        self.position = self.generateRandomPosition()
        self.color = 'red'

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

    def changePosition(self) -> None:
        self.position = self.generateRandomPosition()


class Snake:
    def __init__(self, size) -> None:
        self.size = size
        self.body = [Vector2(100, 100), Vector2(75, 100), Vector2(50, 100)]
        self.direction = Vector2()
        self.color = 'blue'

    def move(self) -> None:
        if self.direction == Vector2():
            return
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy

    def lengthen(self) -> None:
        self.body.append(self.body[-1])

    def changeDirection(self, event):
        if event == pygame.K_DOWN and self.direction.y != -self.size:
            self.direction = Vector2(0, self.size)
        if event == pygame.K_UP and self.direction.y != self.size:
            self.direction = Vector2(0, -self.size)
        if event == pygame.K_LEFT and self.direction.x != self.size:
            self.direction = Vector2(-self.size, 0)
        if event == pygame.K_RIGHT and self.direction.x != -self.size:
            self.direction = Vector2(self.size, 0)


class Score:
    def __init__(self) -> None:
        self.score = 0

    def update(self) -> None:
        self.score += 1
