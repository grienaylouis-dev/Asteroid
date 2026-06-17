import pygame
from constants import LINE_WIDTH

class RectangleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, center_x: float, center_y: float, width: float, height: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(center_x - width / 2, center_y - height / 2, width, height)
        self.rect_max = pygame.Rect(center_x - width / 2, center_y - height / 2, width, height)

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass


class ExpBar(RectangleShape):
    def __init__(self, center_x: float, center_y: float, width: float, height: float, points, fill:bool = False) -> None:
        super().__init__(center_x, center_y, width, height)
        self.points: int = points
        self.fill = fill

    def draw(self, screen, color: str = "grey", line_width: int = int(LINE_WIDTH/2)):
        self.rect.width = int(self.rect_max.width * self.points/100)
        if self.fill:
            pygame.draw.rect(screen, color, self.rect)
        else:
            pygame.draw.rect(screen, color, self.rect, line_width)

    def update(self, points) -> None:
        pass

    def add_point(self, points: int):
        self.points += points
    
    def max_point(self) -> bool:
        if self.points >= 100:
            self.points = 0
            return True
        else:
            return False