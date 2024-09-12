import pygame
from random import randint
from pygame.math import Vector2
from objects import Point, Snake, Score
from sys import exit


class GameProperties:
    """Contains the properties of the game such as width, height, and object size."""
    width = 800
    height = 600
    objectSize = 50

    @classmethod
    def set(cls, width, height, objectSize):
        cls.width = width
        cls.height = height
        cls.objectSize = objectSize


class Object(GameProperties):
    """Contains methods to check object properties and update the game state."""

    def __init__(self) -> None:
        self.snake = Snake(self.objectSize, 'blue')
        self.point = Point(
            self.objectSize, self.generateRandomPosition(), 'red')
        self.score = Score()

    def isSnakeGotPoint(self) -> bool:
        return self.snake.body[0] == self.point.position

    def isSnakeColliding(self) -> bool:
        return self.snake.body[0] in self.snake.body[1:]

    def isSnakeOutOfBounds(self) -> bool:
        return self.snake.body[0].x < 0 or self.snake.body[0].x >= self.width or self.snake.body[0].y < 0 or self.snake.body[0].y >= self.height

    def changePointPosition(self) -> None:
        while self.point.position in self.snake.body:
            self.point.position = self.generateRandomPosition()

    def generateRandomPosition(self) -> Vector2:
        """
        Generate a random position for the object.
        Position is calculated by multiplying a random number between 0 and the screen width/height by the object size.
        This ensures that the objects are always in the grid and allow modifying game resolution.
        Returns:
            tuple: Position of the object, first element is width and second is height.
        """
        width = randint(
            0, (GameProperties.width//GameProperties.objectSize) - 1) * GameProperties.objectSize
        height = randint(0, (GameProperties.height //
                         GameProperties.objectSize) - 1) * GameProperties.objectSize
        return Vector2(width, height)

    def update(self) -> None:
        """Execute the necessary updates when the snake gets a point."""
        self.changePointPosition()
        self.snake.lengthen()
        self.score.update()
        try:
            pygame.mixer.Sound("sounds\snakeGotPoint.mp3").play()
        except FileNotFoundError:
            pass


class Renderer(GameProperties):
    """Contains methods to draw the game objects on the screen."""

    def __init__(self) -> None:
        self.object = Object()
        self.screen = pygame.display.set_mode((self.width, self.height))

    def drawGrass(self) -> None:
        for row in range(self.width // self.objectSize):
            for col in range(self.height // self.objectSize):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, (92, 237, 115),
                                     (row * self.objectSize, col * self.objectSize, self.objectSize, self.objectSize))
                else:
                    pygame.draw.rect(self.screen, (57, 231, 95),
                                     (row * self.objectSize, col * self.objectSize, self.objectSize, self.objectSize))

    def drawPoint(self) -> None:
        pointRect = pygame.Rect(
            self.object.point.position.x, self.object.point.position.y, self.objectSize, self.objectSize)
        pygame.draw.rect(self.screen, self.object.point.color, pointRect)

    def drawScore(self) -> None:
        font = pygame.font.Font(None, 36)
        scoreText = font.render(
            f"Score: {self.object.score.score}", True, 'white')
        self.screen.blit(scoreText, (10, 10))

    def drawGameOverMessage(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.width//2, self.height//2)
        self.screen.blit(text, textRect)

    def drawSnake(self) -> None:
        for pos in self.object.snake.body:
            snakeRect = pygame.Rect(
                pos.x, pos.y, self.object.snake.size, self.object.snake.size)
            pygame.draw.rect(self.screen, self.object.snake.color, snakeRect)

    def drawObjects(self):
        self.drawGrass()
        self.drawSnake()
        self.drawPoint()
        self.drawScore()
        pygame.display.flip()

    def drawGameOverScreen(self):
        self.screen.fill((0, 0, 0))
        self.drawGameOverMessage()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__init__()
                    return
