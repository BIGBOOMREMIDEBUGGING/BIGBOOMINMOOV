from pygame_UI import slider
import pygame
import time

class HeadManual():
    def __init__(self):
        self.running_mode = True

        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()

        self.SLIDER_COLOR = (100, 100, 255)
        self.TRACK_COLOR = (200, 200, 200)

        horizontal_slider = slider.slider("horizontal head mech", 100, 25, 400, 20, 0, 180, 0.5)
        vertical_slider = slider.slider("vertical head mech", 100, 100, 400, 20, 0 , 160, 0.5)

        self.sliders = [
            horizontal_slider,
            vertical_slider
        ]

        objects = []

        for i in self.sliders:
            objects.append(i)

    def run_head_manual(self, horizontal, vertical):
        while self.running_mode:
            self.screen.fill("white")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_mode = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for trackbar in self.sliders:
                        if trackbar.x <= pygame.mouse.get_pos()[0] <= trackbar.x + trackbar.width and trackbar.y <= pygame.mouse.get_pos()[1] <= trackbar.y + trackbar.height:
                            trackbar.is_dragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    for trackbar in self.sliders:
                        trackbar.is_dragging = False
                        match trackbar.name:
                            case "horizontal head mech":
                                horizontal.write(trackbar.get_value())
                                time.sleep(1)
                            case "vertical head mech":
                                vertical.write(trackbar.get_value())
                                print("twin v")
                            case _:
                                print("twinington thiers")
                        print(trackbar.get_value())

                if event.type == pygame.MOUSEMOTION:
                    for trackbar in self.sliders:
                        if trackbar.is_dragging:
                            mouse_x = pygame.mouse.get_pos()[0]
                            trackbar.update(mouse_x)

            for trackbar in self.sliders:
                trackbar.draw(self.screen, self.TRACK_COLOR, self.SLIDER_COLOR)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()