#game graphical constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
LINE_WIDTH = 2

#Player
PLAYER_RADIUS = 20 #radius of the player ship
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 50

#Asteroid
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

#bullet
SHOT_RADIUS = 5
PLAYER_SHOT_SPEED = 300
PLAYER_SHOOT_COOLDOWN_CONSTANT = 0.8

#lvl
EXP_PER_ASTEROID = 15

#multiplicateurs
multiplier_shot_speed = 1
multiplier_shot_cooldown = 1
multiplier_player_speed = 1
multiplier_exp = 1