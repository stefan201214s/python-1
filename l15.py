import pygame
import os
window = pygame.display.set_mode((900, 500))

y_image = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"   ))
r_image = pygame.image.load(os.path.join("assets", "spaceship_red.png"   ))
y_image_resize = pygame.transform.scale(y_image, (80, 60))
r_image_resize = pygame.transform.scale(r_image, (80, 60))
y_image_rotate = pygame.transform.rotate(y_image_resize, 90)
r_image_rotate = pygame.transform.rotate(r_image_resize, 270)
y_image = y_image_rotate
r_image = r_image_rotate
pygame.display.set_caption("Star Wars")
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((0, 0, 255))
        red=pygame.rect(100, 250, 80, 60)
        yellow=pygame.rect(800, 250, 80, 60)
        window.blit(r_image, (yellow.x, yellow.y))
        window.blit(y_image, (red.x, red.y))
        pygame.display.update()
    pygame.quit()

main()