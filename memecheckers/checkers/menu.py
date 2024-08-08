import pygame
import sys
from checkers.constants import WINDOW_HEIGHT, WINDOW_WIDTH, WOOD_BUTTON, BACKGROUND_PRIMARY, LOGO, FONT

class Menu:
    def __init__(self, window):
        self.window = window
        pygame.font.init()
        self.font = FONT
        self.clock = pygame.time.Clock()
        self.button_image = WOOD_BUTTON
        self.button_margin = 30
        self.buttons = {
            'Iniciar': (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100 - self.button_margin),
            'Créditos': (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
            'Sair': (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100 + self.button_margin)
        }

    def draw_buttons(self):
        for text, pos in self.buttons.items():
            button_text = self.font.render(text, True, (255, 255, 255))
            button_rect = button_text.get_rect(center=pos)
            button_image_rect = self.button_image.get_rect(center=pos)
            self.window.blit(self.button_image, button_image_rect)
            self.window.blit(button_text, button_rect)


    def draw_title(self):
        title = self.font.render("Memecheckers", True, (255,255,255))
        logo_image = LOGO
    
        self.window.blit(logo_image, ((title.get_size()[0] + 280), WINDOW_HEIGHT // 2 - 250 - self.button_margin))
        self.window.blit(title, (WINDOW_WIDTH // 2 - (title.get_size()[0] //2), WINDOW_HEIGHT // 2 - 230 - self.button_margin))


    def run(self):
        running = True
        while running:
            self.window.fill(BACKGROUND_PRIMARY)
            self.draw_title()
            self.draw_buttons()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for text, pos in self.buttons.items():
                        button_text = self.font.render(text, True, (255, 255, 255))
                        button_rect = button_text.get_rect(center=pos)
                        if button_rect.collidepoint(mouse_pos):
                            if text == 'Iniciar':
                                running = False
                            elif text == 'Créditos':
                                self.show_credits()
                            elif text == 'Sair':
                                pygame.quit()
                                sys.exit()

            self.clock.tick(60)

    def show_credits(self):
        credit_font = pygame.font.SysFont('Arial', 30)
        credits = [
            "Criado por: Ryan Oliveira",
            "Gráficos: Vinícius Sá",
            "Sonoplastia: FreeSound.com",
            "Agradecimentos: Madrugada Produções"
        ]

        running = True
        while running:
            self.window.fill(BACKGROUND_PRIMARY)
            for i, line in enumerate(credits):
                credit_text = credit_font.render(line, True, (255, 255, 255))
                self.window.blit(credit_text, (WINDOW_WIDTH // 2 - credit_text.get_width() // 2, 100 + i * 40))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False

            self.clock.tick(60)

 