import cv2
import math
from ultralytics import YOLO
import cvzone
import pygame

class HeadLookAt():
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

        self.horizontal_angle = 90
        self.vertical_angle = 90

        self.horizontal.write(self.horizontal_angle)
        self.vertical.write(self.vertical_angle)

        self.cap = cv2.VideoCapture(0)

        self.middle_x = -1
        self.middle_y = -1

        self.model = YOLO("../yolov8n.pt")

    def draw(self, screen):
        success, frame = self.cap.read()
        if success:
            results = self.model(frame, stream=True, verbose=False)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    self.middle_x = (x2 + x1) / 2
                    self.middle_y = (y2 + y1) / 2

                    w, h = x2 - x1, y2 - y1
                    cvzone.cornerRect(frame, (x1, y1, w, h))

                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])

                    cvzone.putTextRect(frame, f'{self.model.names[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
            frame = cv2.flip(frame, 1)

            height, width = frame.shape[0], frame.shape[1]

            camera_surface = pygame.image.frombuffer(
                frame.tobytes(), 
                (width, height), 
                "BGR"
            )
            camera_surface = pygame.transform.scale(camera_surface, (600, 400))

            screen.blit(camera_surface, (0, 0))
        else:
            print("Failed to grab frame")

    def handle_event(self):
        middle_screen_x = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2
        middle_screen_y = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2
        print("middle screen x: " + middle_screen_x)

        while not self.is_in_range(self.middle_x, middle_screen_x - 10, middle_screen_x + 10) and self.is_in_range(self.horizontal_angle, 15, 165):
            if self.middle_x < middle_screen_x:
                self.horizontal_angle += 1
            elif self.middle_x > middle_screen_x:
                self.horizontal_angle -= 1
            self.horizontal.write(self.horizontal_angle)
            print("horizontal angle: " + self.horizontal_angle)
        while not self.is_in_range(self.middle_y, middle_screen_y - 10, middle_screen_y + 10) and self.is_in_range(self.vertical_angle, 15, 165):
            if self.middle_y < middle_screen_y:
                self.vertical_angle += 1
            elif self.middle_y < middle_screen_y:
                self.vertical_angle -= 1
            self.vertical.write(self.vertical_angle)

    def is_in_range(self, value, min, max):
        if value >= min and value <= max:
            return True
        return False