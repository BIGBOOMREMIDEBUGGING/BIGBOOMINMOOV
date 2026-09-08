from pygame_UI import button
from enum import Enum, auto
import pyfirmata2
import pygame
import time
import sys

class mode(Enum):
    MANUAL = 1, 
    LOOK_AT = 2,
    FAILED = auto()

open_window = mode.MANUAL

manual_button = button.Button("MANUAL", 0, 0, 50, 50, (0, 0, 255), (100, 100, 255))
look_at_button = button.Button("LOOK AT", 100, 100, 50, 50, (0, 0, 255), (100, 100, 255))

button_to_mode = {
    manual_button : mode.MANUAL, 
    look_at_button : mode.LOOK_AT
}

board = pyfirmata2.Arduino('COM4')

HORIZONTAL_PIN = 11
VERTICAL_PIN = 12

horizontal = board.get_pin('d:11:s')
vertical = board.get_pin('d:12:s')

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True

horizontal.write(90)
time.sleep(2)
vertical.write(90)
time.sleep(2)

def toggle_window(button):
    open_window = button_to_mode[button]

while running:
    for event in pygame.get_event().get():
        if event.type == pygame.QUIT:
            running = False

    manual_button.handle_event(pygame.event.Event(pygame.MOUSEMOTION))
    look_at_button.handle_event(pygame.event.Event(pygame.MOUSEMOTION))

    screen.fill("white")
    manual_button.draw(screen)
    look_at_button.draw(screen)

    pygame.display.flip
    clock.tick(60)

horizontal.write(90)
time.sleep(2)
vertical.write(90)
time.sleep(2)

board.exit()
pygame.quit()
sys.exit()
