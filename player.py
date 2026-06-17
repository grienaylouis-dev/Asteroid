import pygame
from circleshape import CircleShape #extension of the base Sprite class
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN_CONSTANT
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shootrate_cooldown = 0


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen, color: str = "White", line_width: int = LINE_WIDTH) -> None:
        pygame.draw.polygon(screen, color, self.triangle(), line_width)

    
    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt: float) -> None:
        self.shootrate_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.shootrate_cooldown <= 0:
            self.shoot()
            self.shootrate_cooldown = PLAYER_SHOOT_COOLDOWN_CONSTANT

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.position += rotated_vector * PLAYER_SPEED * dt

    
    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        player_direction = pygame.Vector2(0, 1)
        player_direction = player_direction.rotate(self.rotation)
        bullet.velocity = player_direction * PLAYER_SHOT_SPEED

