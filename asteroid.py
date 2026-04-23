import pygame
import random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.position), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        random_degrees = int(random.uniform(20, 50))

        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        ast1.velocity = self.velocity.rotate(random_degrees)
        ast1.velocity *= 1.2
        
        

        ast2 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        ast2.velocity = self.velocity.rotate(-random_degrees)
        ast2.velocity *= 1.2


       

