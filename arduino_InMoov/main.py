from pygame_UI import button
from head_manual import HeadManual
from head_lookat import HeadLookAt
from enum import Enum
import pyfirmata2
import pygame
import time
import sys

manual_button = button.Button("MANUAL", 0, 0, 50, 50, (0, 0, 255), (100, 100, 255))
look_at_button = button.Button("LOOK AT", 75, 0, 50, 50, (0, 0, 255), (100, 100, 255))

class WINDOW(Enum):
    MANUAL = 1
    LOOKAT = 2

def change_window(state):
    global current_window
    current_window = state
current_window = WINDOW.MANUAL

board = pyfirmata2.Arduino('COM3')

horizontal = board.get_pin('d:11:s')
vertical = board.get_pin('d:12:s')
mouth = board.get_pin('d:13:s')

manual_window = HeadManual(horizontal, vertical, mouth)
lookat_window = HeadLookAt(horizontal, vertical)

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True

horizontal.write(90)
time.sleep(2)
vertical.write(90)
time.sleep(2)

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_window == WINDOW.MANUAL:
            manual_window.handle_event(event)

        if current_window == WINDOW.LOOKAT:
            lookat_window.handle_event()

        manual_button.handle_event(event, change_window, WINDOW.MANUAL)
        look_at_button.handle_event(event, change_window, WINDOW.LOOKAT)

    match current_window:
        case WINDOW.MANUAL:
            manual_window.draw(screen)
        case WINDOW.LOOKAT:
            lookat_window.draw(screen)
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
