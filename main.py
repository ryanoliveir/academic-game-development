import pygame
import os 

WIDTH, HEIGTH = 900, 500

WHITE = (255,255,255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 

window = pygame.display.set_mode((WIDTH, HEIGTH))

pygame.display.set_caption("Game")


space_ship_yellow_image = pygame.image.load(
    os.path.join('assets','spaceship_yellow.png'))
space_ship_yellow = pygame.transform.rotate(pygame.transform.scale(space_ship_yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)


space_ship_red_image = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
space_ship_red = pygame.transform.rotate(pygame.transform.scale(space_ship_red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window():
    window.fill(WHITE)
    window.blit(space_ship_yellow, (300, 100))
    window.blit(space_ship_red, (700, 100))
    

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    player_red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()