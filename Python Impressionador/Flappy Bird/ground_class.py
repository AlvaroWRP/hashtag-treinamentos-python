import pygame

SPRITES_DIR = r'Python Impressionador\Flappy Bird\sprites'


class Ground:
    SPEED = 6
    SPRITE = pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\ground.png'))
    WIDTH = pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\ground.png')).get_width()

    def __init__(self, y):
        self.y = y
        self.first_ground = 0
        self.second_ground = self.WIDTH

    def move(self):
        self.first_ground -= self.SPEED
        self.second_ground -= self.SPEED

        if self.first_ground + self.WIDTH < 0:
            self.first_ground = self.second_ground + self.WIDTH

        if self.second_ground + self.WIDTH < 0:
            self.second_ground = self.first_ground + self.WIDTH

    def draw(self, screen):
        screen.blit(self.SPRITE, (self.first_ground, self.y))
        screen.blit(self.SPRITE, (self.second_ground, self.y))
