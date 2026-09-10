from pygame_UI import slider

class HeadManual():
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

        self.SLIDER_COLOR = (100, 100, 255)
        self.TRACK_COLOR = (200, 200, 200)

        horizontal_slider = slider.Slider("horizontal head mech", 100, 25, 400, 20, 0, 180, 0.5, horizontal)
        vertical_slider = slider.Slider("vertical head mech", 100, 100, 400, 20, 0, 180, 0.5, vertical)

        self.sliders = [
            horizontal_slider,
            vertical_slider
        ]

        self.objects = []
        for s in self.sliders:
            self.objects.append(s)


    def draw(self, screen):
        for slider in self.sliders:
            slider.draw(screen, self.TRACK_COLOR, self.SLIDER_COLOR)

    