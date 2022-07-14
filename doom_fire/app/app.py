import pygame
from doom_fire import DoomFire

if __name__ == '__main__':
    fire_width = 150
    fire_height = 100
    fire_pixel_size = 3
    fire_decay_rate = 2
    fire_windforce = 1

    doom = DoomFire(fire_width,fire_height,fire_pixel_size, fire_decay_rate, fire_windforce)

    pygame.init()
    pygame.display.set_caption("DOOM")
    screen = pygame.display.set_mode((fire_width * fire_pixel_size, fire_height * fire_pixel_size))
    clock = pygame.time.Clock()

    doom.create_fire_source()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        doom.calculate_fire_propagation()
        doom.render(screen)
        pygame.display.flip()
        clock.tick(15) 