import pygame
import os 

WIDTH, HEIGHT = 900, 500

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60
MAX_BULLETS = 3
VELOCITY = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Caça fariseu")


space_ship_yellow_image = pygame.image.load(
    os.path.join('assets','spaceship_yellow.png'))
space_ship_yellow = pygame.transform.rotate(pygame.transform.scale(space_ship_yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)


space_ship_red_image = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
space_ship_red = pygame.transform.rotate(pygame.transform.scale(space_ship_red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(player_1, player_2_):
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, BORDER) 
    window.blit(space_ship_yellow, (player_1.x, player_1.y))
    window.blit(space_ship_red, (player_2_.x, player_2_.y))
    pygame.display.update()



def yellow_handle_movement(keys_pressed, player_1):
    if keys_pressed[pygame.K_a] and player_1.x - VELOCITY > 0: #left
        player_1.x -= VELOCITY
    if keys_pressed[pygame.K_d] and player_1.x + player_1.width + VELOCITY < BORDER.x: #right
        player_1.x += VELOCITY
    if keys_pressed[pygame.K_w] and player_1.y - VELOCITY > 0: #up
        player_1.y -= VELOCITY
    if keys_pressed[pygame.K_s] and player_1.y + player_1.height + VELOCITY < HEIGHT - 15 :  #down
        player_1.y += VELOCITY
            

def red_handle_movement(keys_pressed, player_2):
    if keys_pressed[pygame.K_LEFT] and player_2.x - VELOCITY > BORDER.x + BORDER.width: #left
        player_2.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player_2.x + player_2.width  + VELOCITY  < WIDTH: #right
        player_2.x += VELOCITY
    if keys_pressed[pygame.K_UP] and player_2.y  - VELOCITY > 0: #up
        player_2.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and player_2.y + player_2.height + VELOCITY   < HEIGHT - 15: #down              
        player_2.y += VELOCITY  


def handle_bullets(yellow_bullets, red_bullets, player_1, player_2):
    

def main():
    clock = pygame.time.Clock()

    player_red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    red_bullets = []
    yellow_bullets = []


    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_yellow.x + player_yellow.width, player_yellow.y + player_yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_red.x, player_red.y + player_red.height/2 -2 ,10, 5)
                    red_bullets.append(bullet)


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, player_yellow)
        red_handle_movement(keys_pressed, player_red)
        
        handle_bullets(yellow_bullets, red_bullets, player_yellow, player_red)

        draw_window(player_yellow, player_red)
        


    pygame.quit()

if __name__ == "__main__":
    main()