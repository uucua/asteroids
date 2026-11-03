from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame
class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    #pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)

    #self.position += self.velocity * dt    
    def update(self, dt):
        self.position += self.velocity * dt
