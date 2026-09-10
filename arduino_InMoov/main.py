from pygame_UI import button
from head_manual import HeadManual
from enum import Enum
import pyfirmata2
import pygame
import time
import sys

manual_button = button.Button("MANUAL", 0, 0, 50, 50, (0, 0, 255), (100, 100, 255))
look_at_button = button.Button("LOOK AT", 100, 100, 50, 50, (0, 0, 255), (100, 100, 255))

class CURRENT_WINDOW(Enum):
    MANUAL = 1, 
    LOOKAT = 2
current_window = CURRENT_WINDOW.MANUAL

def change_window(state):
    current_window = state

board = pyfirmata2.Arduino('COM4')

HORIZONTAL_PIN = 11
VERTICAL_PIN = 12

horizontal = board.get_pin('d:11:s')
vertical = board.get_pin('d:12:s')

manual_window = HeadManual(horizontal, vertical)

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True

has_sliders = False
sliders = []

horizontal.write(90)
time.sleep(2)
vertical.write(90)
time.sleep(2)

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if has_sliders:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for slider in sliders:
                    if slider.x <= pygame.mouse.get_pos()[0] <= slider.x + slider.width and slider.y <= pygame.mouse.get_pos()[1] <= slider.y + slider.height:
                        slider.is_dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                for slider in sliders:
                    slider.is_dragging = False
                    match slider.name:
                        case "horizontal head mech":
                            horizontal.write(slider.get_value())
                            time.sleep(1)
                        case "vertical head mech":
                            vertical.write(slider.get_value())
                            print("twin v")
                        case _:
                            print("twinington thiers")
                    print(slider.get_value())

            if event.type == pygame.MOUSEMOTION:
                for slider in sliders:
                    if slider.is_dragging:
                        mouse_x = pygame.mouse.get_pos()[0]
                        slider.update(mouse_x)

        manual_button.handle_event(event, change_window, CURRENT_WINDOW.MANUAL)
        look_at_button.handle_event(event, change_window, CURRENT_WINDOW.LOOKAT)

    match current_window:
        case CURRENT_WINDOW.MANUAL:
            manual_window.draw(screen)
            has_sliders = True
            sliders = manual_window.sliders
        case CURRENT_WINDOW.LOOKAT:
            pass
        case _:
            print("failed bro")


    manual_button.draw(screen)
    look_at_button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

horizontal.write(90)
time.sleep(2)
vertical.write(90)
time.sleep(2)

board.exit()
sys.exit()
