import pygame.draw

import pyved_engine as pyv


class Circle(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.state = 1
        self.radius = 20
        self.color = 'red'
        self.pos = pygame.display.get_surface().get_size()

    def on_update(self, ev):
        self.radius

    def on_paint(self, ev):
        pygame.draw.circle(ev.screen, self.color, )
