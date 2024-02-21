import pygame
import os 

WIDTH, HEIGTH = 900, 500

WHITE = (255,255,255)

FPS = 60
VELOCITY = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 

window = pygame.display.set_mode((WIDTH, HEIGTH))

pygame.display.set_caption("Game")


space_ship_yellow_image = pygame.image.load(
    os.path.join('assets','spaceship_yellow.png'))
space_ship_yellow = pygame.transform.rotate(pygame.transform.scale(space_ship_yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)


space_ship_red_image = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
space_ship_red = pygame.transform.rotate(pygame.transform.scale(space_ship_red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(player_1, player_2_):
    window.fill(WHITE)
    window.blit(space_ship_yellow, (player_1.x, player_1.y))
    window.blit(space_ship_red, (player_2_.x, player_2_.y))
    pygame.display.update()



def yellow_handle_movement(keys_pressed, player_1):
    if keys_pressed[pygame.K_a]: #left
        player_1.x -= VELOCITY
    if keys_pressed[pygame.K_d]: #right
        player_1.x += VELOCITY
    if keys_pressed[pygame.K_w]: #up
        player_1.y -= VELOCITY
    if keys_pressed[pygame.K_s]: #down
        player_1.y += VELOCITY
            

def red_handle_movement(keys_pressed, player_2):
    if keys_pressed[pygame.K_LEFT]: #left
        player_2.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]: #right
        player_2.x += VELOCITY
    if keys_pressed[pygame.K_UP]: #up
        player_2.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]: #down
        player_2.y += VELOCITY
            


def main():
    clock = pygame.time.Clock()

    player_red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, player_yellow)
        red_handle_movement(keys_pressed, player_red)
        


        draw_window(player_yellow, player_red)
        


    pygame.quit()

if __name__ == "__main__":
    main()