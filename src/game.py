import pygame
from objects import Point, Snake, Score
from sys import exit


class GameScreen:
    def __init__(self, width, height, size, snake, point, score) -> None:
        self.width = width
        self.height = height
        self.objectSize = size
        self.screen = pygame.display.set_mode((width, height))
        self.snake = snake
        self.point = point
        self.score = score

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
            self.point.position.x, self.point.position.y, self.point.size, self.point.size)
        pygame.draw.rect(self.screen, self.point.color, pointRect)

    def drawScore(self) -> None:
        font = pygame.font.Font(None, 36)
        scoreText = font.render(f"Score: {self.score.score}", True, 'white')
        self.screen.blit(scoreText, (10, 10))

    def drawGameOverMessage(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.width//2, self.height//2)
        self.screen.blit(text, textRect)

    def drawSnake(self) -> None:
        for pos in self.snake.body:
            snakeRect = pygame.Rect(
                pos.x, pos.y, self.snake.size, self.snake.size)
            pygame.draw.rect(self.screen, self.snake.color, snakeRect)


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(50)
        self.point = Point(50)
        self.score = Score()
        self.gameScreen = GameScreen(
            800, 600, 50, self.snake, self.point, self.score)

    def drawObjects(self):
        self.gameScreen.drawGrass()
        self.gameScreen.drawSnake()
        self.gameScreen.drawPoint()
        self.gameScreen.drawScore()
        pygame.display.flip()

    def gameOver(self):
        self.gameScreen.screen.fill((0, 0, 0))
        self.gameScreen.drawGameOverMessage()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__init__()
                    return

    def isSnakeGotPoint(self):
        return self.snake.body[0] == self.point.position

    def isSnakeColliding(self) -> bool:
        return self.snake.body[0] in self.snake.body[1:]

    def isSnakeOutOfBounds(self) -> bool:
        return self.snake.body[0].x < 0 or self.snake.body[0].x >= self.gameScreen.width or self.snake.body[0].y < 0 or self.snake.body[0].y >= self.gameScreen.height
