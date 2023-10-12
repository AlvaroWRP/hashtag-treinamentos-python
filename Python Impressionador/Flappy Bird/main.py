import pygame
from bird_class import Bird
from pipe_class import Pipe
from ground_class import Ground

SPRITES_DIR = r'Python Impressionador\Flappy Bird\sprites'

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

SPRITE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(rf'{SPRITES_DIR}\background.png'))

pygame.font.init()
FONT_POINTS = pygame.font.SysFont('Arial', 50)

def draw_screen(screen, bird, pipes, ground, points):
    screen.blit(SPRITE_BACKGROUND, (0, 0))
    bird.draw(screen)

    for pipe in pipes:
        pipe.draw(screen)

    points_text = FONT_POINTS.render(f'Pontuação: {points}', 1, (255, 255, 255))
    screen.blit(points_text, (SCREEN_WIDTH - 10 - points_text.get_width(), 10))
    ground.draw(screen)

    pygame.display.update()

def main():
    birds = [Bird(230, 350),]
    pipes = [Pipe(700),]
    ground = Ground(730)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    points = 0
    clock = pygame.time.Clock()

    is_running = True

    while is_running:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        for bird in birds:
            bird.move()
        ground.move()

        add_pipe = False
        remove_pipes = []

        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)

                if not pipe.has_passed and bird.x > pipe.x:
                    pipe.has_passed = True
                    add_pipe = True
        
            pipe.move()

            if pipe.x + pipe.TOP_PIPE.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            points += 1
            pipes.append(Pipe(600))

        for pipe in remove_pipes:
            pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if bird.y + bird.sprite.get_height() > ground.y or bird.y < 0:
                birds.pop(i)

        draw_screen(screen, bird, pipes, ground, points)

main()
