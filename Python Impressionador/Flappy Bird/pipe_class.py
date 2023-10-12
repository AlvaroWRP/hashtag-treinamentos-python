import pygame
import random

SPRITES_DIR = r'Python Impressionador\Flappy Bird\sprites'


class Pipe:
    DISTANCE = 200
    SPEED = 6

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top_position = 0
        self.bottom_position = 0
        self.SPRITE = pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\pipe.png'))
        self.TOP_PIPE = pygame.transform.flip(self.SPRITE, False, True)
        self.BOTTOM_PIPE = self.SPRITE
        self.has_passed = False
        self.define_height()
    
    def define_height(self):
        self.height = random.randrange(50, 450)
        self.top_position = self.height - self.TOP_PIPE.get_height()
        self.bottom_position = self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED

    def draw(self, screen):
        screen.blit(self.TOP_PIPE, (self.x, self.top_position))
        screen.blit(self.BOTTOM_PIPE, (self.x, self.bottom_position))
    
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.TOP_PIPE)
        bottom_mask = pygame.mask.from_surface(self.BOTTOM_PIPE)

        top_distance = (self.x - bird.x, self.top_position - round(bird.y))
        bottom_distance = (self.x - bird.x, self.bottom_position - round(bird.y))

        top_hit = bird_mask.overlap(top_mask, top_distance)
        bottom_hit = bird_mask.overlap(bottom_mask, bottom_distance)

        if top_hit or bottom_hit:
            return True
        
        return False
