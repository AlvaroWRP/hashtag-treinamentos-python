import pygame

SPRITES_DIR = r'Python Impressionador\Flappy Bird\sprites'


class Bird:
    SPRITES = [
        pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\bird1.png')),
        pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\bird2.png')),
        pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\bird3.png')),
    ]
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = self.y
        self.angle = 0
        self.speed = 0
        self.time = 0
        self.sprite_counter = 0
        self.sprite = Bird.SPRITES[0]

    def jump(self):
        self.speed = -9
        self.time = 0
        self.height = self.y

    def move(self):
        self.time += 1
        displacement = 1.5 * (self.time ** 2) + self.speed * self.time

        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 6

        self.y += displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def draw(self, screen):
        self.sprite_counter += 1

        if self.sprite_counter < self.ANIMATION_TIME:
            self.sprite = Bird.SPRITES[0]

        elif self.sprite_counter < self.ANIMATION_TIME * 2:
            self.sprite = Bird.SPRITES[1]

        elif self.sprite_counter < self.ANIMATION_TIME * 3:
            self.sprite = Bird.SPRITES[2]

        elif self.sprite_counter < self.ANIMATION_TIME * 4:
            self.sprite = Bird.SPRITES[1]

        elif self.sprite_counter < self.ANIMATION_TIME * 4 + 1:
            self.sprite = Bird.SPRITES[0]
            self.sprite_counter = 0

        # definir o sprite pra quando o pássaro estiver caindo
        if self.angle == -80:
            self.sprite = Bird.SPRITES[1]
            self.sprite_counter = self.ANIMATION_TIME * 2

        # desenhar o sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, self.angle)
        sprite_center = self.sprite.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_sprite.get_rect(center=sprite_center)
        screen.blit(rotated_sprite, rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.sprite)
