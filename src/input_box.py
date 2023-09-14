import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class InputBox:
    def __init__(self, x, y, width, height, left_text="", side_text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = ""
        self.font = pygame.font.Font(None, 45)
        self.active = False
        self.left_text = left_text
        self.side_text = side_text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = WHITE if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        # Remove commas and convert to an integer
                        self.text = str(int(self.text.replace(',', '')))
                    except ValueError:
                        self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit() or event.unicode == ',':
                    self.text += event.unicode

    def update(self):
        width = max(200, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def draw(self, screen):
        # Display left text
        left_text_surface = self.font.render(self.left_text, True, BLACK)
        screen.blit(left_text_surface, (self.rect.x - left_text_surface.get_width() - 10, self.rect.y + 5))

        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Display side text
        side_text_surface = self.font.render(self.side_text, True, BLACK)
        screen.blit(side_text_surface, (self.rect.x + self.rect.width + 10, self.rect.y + 5))

    def get_text(self):
        return self.text

