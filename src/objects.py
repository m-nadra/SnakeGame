import pygame
from pygame.math import Vector2


class Point:
    def __init__(self, size, position) -> None:
        self.size = size
        self.position = position
        self.color = 'red'


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
