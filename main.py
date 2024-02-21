import pygame

WIDTH, HEIGTH = 900, 500

WHITE = (255,255,255)

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGTH))

pygame.display.set_caption("Game")



def draw_window():
    window.fill(WHITE)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

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