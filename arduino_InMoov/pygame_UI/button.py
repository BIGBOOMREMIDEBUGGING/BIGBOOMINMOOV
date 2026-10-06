import pygame

class Button():
    def __init__(self, name, x, y, width, height, default_color, hover_color):
        self.name = name
        # Create a Pygame Rect object right away to manage position and size
        self.rect = pygame.Rect(x, y, width, height)
        self.default_color = default_color
        self.hover_color = hover_color

        self.color = default_color

    def draw(self, screen):
        # 1. Use self.rect directly for drawing
        pygame.draw.rect(screen, self.color, self.rect)

        font = pygame.font.SysFont("Arial", 24)
        value_text = font.render(self.name, True, (0, 0, 0))
        
        # 2. Use self.rect attributes for precise text centering
        text_x = self.rect.x + (self.rect.width - value_text.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - value_text.get_height()) // 2
        screen.blit(value_text, (text_x, text_y))

    def handle_event(self, event, func, param):
        mouse_pos = pygame.mouse.get_pos()

        # 3. Add Hover Effect (Optional but highly recommended since you have hover_color)
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.default_color

        # 4. Process the mouse click (This will now work!)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_pos):
                func(param)
                print("jsdopfnsdfapsdfoahfewoweifn")
