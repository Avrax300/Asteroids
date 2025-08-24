from constants import *
from player import Player
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

    # adds the Player class to both groups
    Player.containers = (updatables, drawables)

    # creates a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creates a clock object
    clock = pygame.time.Clock()
    dt = 0

    # creates a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # sets the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # rotates the player left or right depending on input
        updatables.update(dt)

        screen.fill("black")

        # draws the sprites on screen
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # limits the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
