import pygame
import random
import constants
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, EXP_PER_ASTEROID

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen, color: str = "White", line_width: int = LINE_WIDTH):
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)
    
    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self)-> int:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return EXP_PER_ASTEROID * constants.multiplier_exp
        log_event("asteroid_split")
        new_asteroids_angle = random.uniform(20, 50)
        asteroid_velocity_1 = self.velocity.rotate(new_asteroids_angle)
        asteroid_velocity_2 = self.velocity.rotate(-new_asteroids_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = asteroid_velocity_1 * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = asteroid_velocity_2 * 1.2
        return 2 * constants.multiplier_exp