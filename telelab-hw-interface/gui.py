import pygame
import sys

class TelelabGUI:
    def __init__(self, width=600, height=400):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Telelab')
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, pos):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, pos)

    def input_box(self, prompt, pos):
        input_active = False
        user_input = ""
        input_rect = pygame.Rect(pos[0], pos[1], 140, 32)
        color_inactive = pygame.Color('gray')
        color_active = pygame.Color('blue')
        color = color_inactive

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        input_active = not input_active
                    else:
                        input_active = False
                    color = color_active if input_active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            return user_input
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        else:
                            user_input += event.unicode

            self.screen.fill((0, 0, 0))
            self.draw_text(prompt, (50, 50))
            pygame.draw.rect(self.screen, color, input_rect, 2)

            txt_surface = self.font.render(user_input, True, (255, 255, 255))
            self.screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect.w = max(100, txt_surface.get_width() + 10)

            pygame.display.flip()

    def show_login(self):
        nrp = self.input_box('Enter your NRP:', (50, 100))
        password = self.input_box('Enter your Password:', (50, 150))
        return nrp, password

    def show_module_selection(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_text('Select a module (1-5):', (50, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in range(pygame.K_1, pygame.K_6):
                        return event.key - pygame.K_0

            pygame.display.flip()

    def display_message(self, message):
        self.screen.fill((0, 0, 0))
        self.draw_text(message, (50, 150))
        pygame.display.flip()
        pygame.time.delay(2000)
