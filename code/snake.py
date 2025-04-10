from settings import *
from os import walk

class Snake:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.get_surface()
        
        # graphics
        self.draw_data = []
        self.surfs = self.import_surfs()
        self.reset()
        self.head_surf = self.surfs['head_right']
        self.tail_surf = self.surfs['tail_left']

    def import_surfs(self):
        surf_dict = {}
        for folder_path, _, image_names in walk(join('graphics', 'snake')):
            for image_name in image_names:
                full_path = join(folder_path, image_name)
                surface = pygame.image.load(full_path).convert_alpha()
                surf_dict[image_name.split('.')[0]] = surface
        
        return surf_dict
    
    def update_head(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.Vector2(-1, 0): self.head_surf = self.surfs['head_right']
        elif head_relation == pygame.Vector2(1, 0): self.head_surf = self.surfs['head_left']
        elif head_relation == pygame.Vector2(0, -1): self.head_surf = self.surfs['head_down']
        elif head_relation == pygame.Vector2(0, 1): self.head_surf = self.surfs['head_up']

    def update_tail(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.Vector2(-1, 0): self.tail_surf = self.surfs['tail_right']
        elif tail_relation == pygame.Vector2(1, 0): self.tail_surf = self.surfs['tail_left']
        elif tail_relation == pygame.Vector2(0, -1): self.tail_surf = self.surfs['tail_down']
        elif tail_relation == pygame.Vector2(0, 1): self.tail_surf = self.surfs['tail_up']

    def update_body(self):
        self.draw_data = []
        for index, part in enumerate(self.body):
            x = part.x * CELL_SIZE
            y = part.y * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if index == 0:
                self.draw_data.append((self.head_surf, rect))
            elif index == (len(self.body) - 1):
                self.draw_data.append((self.tail_surf, rect))
            else:
                last_part = self.body[index + 1] - part
                next_part = self.body[index - 1] - part
                if last_part.x == next_part.x:
                    self.draw_data.append((self.surfs['body_horizontal'], rect))
                elif last_part.y == next_part.y:
                    self.draw_data.append((self.surfs['body_vertical'], rect))
                else: # corners
                    if last_part.x == -1 and next_part.y == -1 or last_part.y == -1 and next_part.x == -1:
                        self.draw_data.append((self.surfs['body_tl'], rect))
                    elif last_part.x == -1 and next_part.y == 1 or last_part.y == 1 and next_part.x == -1:
                        self.draw_data.append((self.surfs['body_bl'], rect))
                    elif last_part.x == 1 and next_part.y == -1 or last_part.y == -1 and next_part.x == 1:
                        self.draw_data.append((self.surfs['body_tr'], rect))
                    elif last_part.x == 1 and next_part.y == 1 or last_part.y == 1 and next_part.x == 1:
                        self.draw_data.append((self.surfs['body_br'], rect))

    def update(self):
        body_copy = self.body[:] if self.has_eaten else self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.has_eaten = False

        self.update_head()
        self.update_tail()
        self.update_body()

    def reset(self):
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]
        self.direction = pygame.Vector2(1, 0)
        self.has_eaten = False

        self.update_head()
        self.update_tail()
        self.update_body()

    def draw(self):
        for surf, rect in self.draw_data:
            self.display_surface.blit(surf, rect)