from settings import *
from random import choice

class Apple:
    def __init__(self, unavailable_pos):
        self.display_surface = pygame.display.get_surface()
        self.set_pos(unavailable_pos)
    
    def set_pos(self, unavailable_pos):
        available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS)
                         if pygame.Vector2(x, y) not in unavailable_pos]
        self.pos = pygame.Vector2(choice(available_pos))

    def draw(self):
        rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display_surface, 'blue', rect)