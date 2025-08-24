import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # if asteroid was small, just destroy it and do nothing else
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # sets new velocity for the new asteroids
        self.random_angle = random.uniform(20, 50)
        new_velocity_1 = pygame.Vector2.rotate(self.velocity, self.random_angle)
        new_velocity_2 = pygame.Vector2.rotate(self.velocity, -self.random_angle)
        
        # sets the new radius for the new asteroids
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS

        # creates the new asteroids
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)

        # assigns the new velocity to each asteroid
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2.velocity = new_velocity_2 * 1.2
