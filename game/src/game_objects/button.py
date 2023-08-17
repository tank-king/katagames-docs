import pygame
from src.game_objects.label import Label


class Button(Label):
    def __init__(self, x, y, text, size, color, font='consolas', anchor='center', callback=None):
        super().__init__(x, y, text, size, color, font, anchor)
        self.callback = callback

    def on_paint(self, ev):
        super().on_paint(ev)
        pygame.draw.rect(ev.screen, 'white', self.get_rect().inflate(10, 10), 5)

    def on_mousedown(self, ev):
        if self.get_rect().collidepoint(*ev.pos):
            if self.callback:
                self.callback()
