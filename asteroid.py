import pygame
from circleshape import CircleShape
import constants as con
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, con.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= con.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - con.ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = first_asteroid_velocity * 1.2
        second_asteroid.velocity = second_asteroid_velocity * 1.2
