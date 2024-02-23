import sys
import pygame
import os 

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

FPS = 60
MAX_BULLETS = 3
VELOCITY = 5
BULLET_VELOCITY = 10
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 40)


BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit_sound.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'fire.mp3'))

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space.png')), (WIDTH, HEIGHT))



window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("STAR SEM WARS")


space_ship_yellow_image = pygame.image.load(
    os.path.join('assets','spaceship_yellow.png'))
space_ship_yellow = pygame.transform.rotate(pygame.transform.scale(space_ship_yellow_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)


space_ship_red_image = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
space_ship_red = pygame.transform.rotate(pygame.transform.scale(space_ship_red_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(player_1, player_2, yellow_bullets, red_bullets, player_1_health, player_2_health):
    window.blit(BACKGROUND_IMAGE, (0,0))
    pygame.draw.rect(window, BLACK, BORDER) 

    red_health_text = HEALTH_FONT.render(f'HEALTH: {player_1_health}', 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(f'HEALTH: {player_2_health}', 1, WHITE)

    window.blit(yellow_health_text, (10, 10))
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() -10, 10))

    window.blit(space_ship_yellow, (player_1.x, player_1.y))
    window.blit(space_ship_red, (player_2.x, player_2.y))


    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(window, RED, bullet)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    window.blit(draw_text, (WIDTH//2- draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

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
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if(player_2.colliderect(bullet)):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)



    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if(player_1.colliderect(bullet)):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    global window
    clock = pygame.time.Clock()

    player_red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    red_bullets = []
    yellow_bullets = []

    yellow_health = 10
    red_health = 10 
    

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_yellow.x + player_yellow.width, player_yellow.y + player_yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_red.x, player_red.y + player_red.height//2 -2 ,10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()


            if event.type == RED_HIT:
                BULLET_HIT_SOUND.play()
                red_health -= 1

            if event.type == YELLOW_HIT:
                BULLET_HIT_SOUND.play()
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, player_yellow)
        red_handle_movement(keys_pressed, player_red)
        
        handle_bullets(yellow_bullets, red_bullets, player_yellow, player_red)

        draw_window(player_yellow, player_red, yellow_bullets, red_bullets, yellow_health, red_health)
    
    main()

if __name__ == "__main__":
    main()