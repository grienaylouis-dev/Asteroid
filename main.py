import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from exp import ExpBar

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    bars = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group() # call the .update(dt) method
    drawable = pygame.sprite.Group() # call the .draw(screen) method

    ExpBar.containers = (bars, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    level_bar = ExpBar(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (1-0.03), SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.02, 100)
    exp_bar = ExpBar(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (1-0.06), SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.02, 100)
    level_display = ExpBar(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (1-0.03), SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.02, 20, True)
    exp_display = ExpBar(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (1-0.06), SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.02, 0, True)

    #GAME LOOP
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.Collision_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.Collision_with(asteroid):
                    log_event("asteroid_shot")
                    exp = asteroid.split()
                    shot.kill()
                    exp_display.add_point(exp)
        
        #draw
        exp_display.draw(screen)
        if exp_display.max_point():
            level_display.add_point(20)
            level_display.draw(screen)

        #render
        screen.fill("black")
        for element in drawable:
            element.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

