import pygame.font

import pyved_engine as pyv


class Label(pyv.EvListener):
    def __init__(self, x, y, text, size, color, font='consolas', anchor='center'):
        super().__init__()
        self.pos = (x, y)
        self.args = [size, color, font]
        self.anchor = anchor
        self.text = pygame.font.SysFont(font, size).render(text, True, color)

    def get_rect(self):
        rect = self.text.get_rect()
        rect.__setattr__(self.anchor, self.pos)
        rect.y -= 5
        return rect

    def update_text(self, text):
        self.text = pygame.font.SysFont(self.args[2], self.args[0]).render(text, True, self.args[1])

    def on_paint(self, ev):
        ev.screen.blit(self.text, self.text.get_rect(**{self.anchor: self.pos}))
