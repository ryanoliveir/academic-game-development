import pygame
import sys
from checkers.constants import WINDOW_HEIGHT, WINDOW_WIDTH, WOOD_BUTTON, FONT_INFO_PANEL_LABEL, FONT, FONT_SMALL

class WinnerPanel:
    def __init__(self, window, winner):
        self.window = window
        self.winner = winner  # Winner should be a string like "Red" or "White"
        pygame.font.init()
        self.font_large = FONT
        self.font_small = FONT_SMALL
        self.clock = pygame.time.Clock()
        self.button_image = WOOD_BUTTON
        
        self.button_margin = 20  # Space between buttons

        self.buttons = {
            'Jogar Novamente': (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 ),
            'Menu': (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 180 + self.button_margin)
        }

    def draw(self):
        self.window.fill((143, 75, 58))  # Background color

        # Display winner
        winner_text = self.font_large.render(f'{self.winner} Ganhou', True, (255, 255, 255))
        winner_rect = winner_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 140))
        self.window.blit(winner_text, winner_rect)

        # Draw buttons
        for text, pos in self.buttons.items():
            button_text = self.font_small.render(text, True, (255, 255, 255))
            button_rect = button_text.get_rect(center=pos)
            button_image_rect = self.button_image.get_rect(center=pos)
            self.window.blit(self.button_image, button_image_rect)
            self.window.blit(button_text, button_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for text, pos in self.buttons.items():
                        button_image_rect = self.button_image.get_rect(center=pos)
                        if button_image_rect.collidepoint(mouse_pos):
                            
                            if text == 'Jogar Novamente':
                                return 'play_again'
                            elif text == 'Menu':
                                return 'menu'

            self.clock.tick(60)