from settings import *
from random import choice
from math import sin

class Apple:
    def __init__(self, unavailable_pos):
        self.display_surface = pygame.display.get_surface()
        self.set_pos(unavailable_pos)

        self.surf = pygame.image.load(join('graphics', 'apple.png')).convert_alpha()
        self.surf.set_colorkey((255, 255, 255))
        self.scaled_surf = self.surf.copy()
        cell_center = (self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2)
        self.scaled_rect = self.scaled_surf.get_rect(center = cell_center)

    def set_pos(self, unavailable_pos):
        available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS)
                         if pygame.Vector2(x, y) not in unavailable_pos]
        self.pos = pygame.Vector2(choice(available_pos))

    def draw(self):
        scale = 1 + sin(pygame.time.get_ticks() / 600) / 3
        self.scaled_surf = pygame.transform.smoothscale_by(self.surf, scale)
        cell_center = (self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2)
        self.scaled_rect = self.scaled_surf.get_rect(center = cell_center)
        
        self.display_surface.blit(self.scaled_surf, self.scaled_rect)