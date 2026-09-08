import pygame
import time

class Slider():
    def __init__(self, name, x, y, width, height, min, max, current, motor):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min = min
        self.max = max
        self.current = current
        self.motor = motor

        self.slider_width = 20
        self.slider_height = height

        self.is_dragging = False

    def draw(self, screen, TRACK_COLOR, SLIDER_COLOR):
        pygame.draw.rect(screen, TRACK_COLOR, (self.x, self.y, self.width, self.height))
        slider_x = self.x + self.current * (self.width - self.slider_width)
        pygame.draw.rect(screen, SLIDER_COLOR, (slider_x, self.y - (self.slider_height - self.height) / 2, self.slider_width, self.slider_height))

        font = pygame.font.SysFont("Arial", 24)
        value_text = font.render(self.name + " : " + f"{int(self.get_value())}", True, (0, 0, 0))
        screen.blit(value_text, (self.x + (self.width - value_text.get_width()) // 2, self.y + self.height + 5))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_pos):
                self.is_dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.is_dragging = False
            self.motor.write(self.get_value())
            time.sleep(1)

        if event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                self.update(mouse_pos[0])


    def update(self, mouse_x):
        if self.x <= mouse_x <= self.x + self.width:
            self.current = (mouse_x - self.x) / self.width

    def get_value(self):
        return int(self.current * (self.max - self.min) + self.min)
