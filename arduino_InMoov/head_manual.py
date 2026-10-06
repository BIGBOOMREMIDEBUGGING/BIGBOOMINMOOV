from pygame_UI import slider
import pygame
import time

class HeadManual():
    def __init__(self, horizontal, vertical, mouth):
        self.horizontal = horizontal
        self.vertical = vertical
        self.mouth = mouth

        self.SLIDER_COLOR = (100, 100, 255)
        self.TRACK_COLOR = (200, 200, 200)

        horizontal_slider = slider.Slider("horizontal head mech", 100, 75, 400, 20, 0, 180, 0.5, horizontal)
        vertical_slider = slider.Slider("vertical head mech", 100, 150, 400, 20, 0, 180, 0.5, vertical)
        mouth_slider = slider.Slider("mouth mech", 100, 225, 400, 20, 0, 180, 0.5, mouth)

        self.sliders = [
            horizontal_slider,
            vertical_slider, 
            mouth_slider
        ]

        self.objects = []
        for s in self.sliders:
            self.objects.append(s)


    def draw(self, screen):
        for slider in self.sliders:
            slider.draw(screen, self.TRACK_COLOR, self.SLIDER_COLOR)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for slider in self.sliders:
                if slider.x <= pygame.mouse.get_pos()[0] <= slider.x + slider.width and slider.y <= pygame.mouse.get_pos()[1] <= slider.y + slider.height:
                    slider.is_dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            for slider in self.sliders:
                slider.is_dragging = False
                match slider.name:
                    case "horizontal head mech":
                        self.horizontal.write(slider.get_value())
                    case "vertical head mech":
                        self.vertical.write(slider.get_value())
                    case "mouth mech":
                        self.mouth.write(slider.get_value())
                    case _:
                        print("motor not connected to slider")
                time.sleep(0.5)

        if event.type == pygame.MOUSEMOTION:
            for slider in self.sliders:
                if slider.is_dragging:
                    mouse_x = pygame.mouse.get_pos()[0]
                    slider.update(mouse_x)
            

    