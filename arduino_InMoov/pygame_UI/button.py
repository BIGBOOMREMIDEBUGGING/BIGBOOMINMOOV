import pygame

class Button():
    def __init__(self, name, x, y, width, height, default_color, hover_color):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.default_color = default_color
        self.hover_color = hover_color

        self.color = default_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.SysFont("Arial", 24)
        value_text = font.render(self.name + " : " + f"{int(self.get_value())}", True, (0, 0, 0))
        screen.blit(value_text, (self.x + (self.width - value_text.get_width()) // 2, self.y + self.height / 2))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.default_color

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_pos):
                return True
        return False