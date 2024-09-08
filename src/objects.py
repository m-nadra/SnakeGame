"""This module contains the classes for the game objects with methods to manipulate their properties."""

import pygame
from pygame.math import Vector2
from dataclasses import dataclass


@dataclass
class Point:
    size: int
    position: Vector2
    color: str


@dataclass
class Score:
    score = 0

    def update(self) -> None:
        self.score += 1


@dataclass
class Snake:
    size: int
    color: str
    body = [Vector2(100, 100), Vector2(75, 100), Vector2(50, 100)]
    direction = Vector2()

    def move(self) -> None:
        """Move the snake by adding a new segment to the front of the snake's body and removing the last segment.
        The new segment is calculated by adding the current direction to the first segment of the snake's body.
        Avoid moving the snake before user will not start the game.
        """
        if self.direction == Vector2():
            return
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy

    def lengthen(self) -> None:
        """Lengthen the snake by adding a new segment to the end of the snake's body."""
        self.body.append(self.body[-1])

    def changeDirection(self, pressedKey) -> None:
        """Change the direction of the snake based on the key pressed.
        Pressed key can't be the opposite of the current direction. For example, if the snake is moving right, it can't move left.

        Args:
            pressedKey: The key pressed by the user.
        """
        if pressedKey == pygame.K_DOWN and self.direction.y != -self.size:
            self.direction = Vector2(0, self.size)
        elif pressedKey == pygame.K_UP and self.direction.y != self.size:
            self.direction = Vector2(0, -self.size)
        elif pressedKey == pygame.K_LEFT and self.direction.x != self.size:
            self.direction = Vector2(-self.size, 0)
        elif pressedKey == pygame.K_RIGHT and self.direction.x != -self.size:
            self.direction = Vector2(self.size, 0)
