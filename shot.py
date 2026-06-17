import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SPEED

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen, color: str = "White", line_width: int = LINE_WIDTH) -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)

    def update(self, dt) -> None:
        self.position += self.velocity * dt