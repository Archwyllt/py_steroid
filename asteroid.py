import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            pos_angle = self.velocity.rotate(random_angle)
            neg_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            pos_ast = Asteroid(self.position[0], self.position[1], new_radius)
            pos_ast.velocity = 1.2 * pos_angle
            neg_ast = Asteroid(self.position[0], self.position[1], new_radius)
            neg_ast.velocity = 1.2 * neg_angle