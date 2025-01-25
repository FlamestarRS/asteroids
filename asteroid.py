import pygame
import random
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        half1 = Asteroid(self.position.x, self.position.y, new_radius)
        half1.velocity = self.velocity.rotate(angle) * 1.2
        
        half2 = Asteroid(self.position.x, self.position.y, new_radius)
        half2.velocity = self.velocity.rotate(-angle) * 1.2


