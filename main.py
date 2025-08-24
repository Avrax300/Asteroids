import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import *
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initializes pygame
    pygame.init()

    # sets groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assigning objects to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    # creates a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creates a clock object
    clock = pygame.time.Clock()
    dt = 0

    # creates a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # creates the asteroid field
    asteroid_field = AsteroidField()

    # sets the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # rotates the player left or right depending on input
        updatables.update(dt)

        # checks for collisions bettwen asteroids and player
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game over!")

        #checks for collisions between asteroids and bullets
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")

        # draws the sprites on screen
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # limits the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
