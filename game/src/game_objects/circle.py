import random
import time

import pygame.draw

import pyved_engine as pyv
import globals

from game.globals import GameEvents


class Circle(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.state = None
        self.radius = None
        self.max_radius = None
        self.color = None
        self.pos = None
        self.image = None
        self.current_img_radius = None

    def turn_on(self):
        super().turn_on()
        self.setup()

    def setup(self):
        self.state = 'Start'
        self.radius = 0
        self.max_radius = 50
        self.color = random.choice(['black', 'blue', 'grey', 'magenta', 'red'])
        self.image = pygame.transform.smoothscale_by(pygame.image.load(f'assets/images/circle_{self.color}.png'), 0.5)
        w, h = self.image.get_size()
        self.pos = pygame.Vector2(
            random.randint(w // 2, 960 - w // 2),
            random.randint(h // 2, 720 - w // 2)
        )

    def on_update(self, ev):
        match self.state:
            case 'Start':
                self.state = 'A'
            case 'A':
                dr = pygame.Vector2(self.radius, self.radius).lerp(
                    pygame.Vector2(self.max_radius, self.max_radius), 0.25
                )
                self.radius = dr.x
                if self.max_radius - self.radius <= 1:
                    self.state = 'B'
            case 'B':
                self.radius -= 0.3
                if self.radius <= 0:
                    self.radius = 0
                    pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange, state_ident=globals.GameStates.Score)
            case 'C':
                if self.radius > 1:
                    dr = pygame.Vector2(self.radius, self.radius).lerp(
                        pygame.Vector2(0, 0), 0.5
                    )
                    self.radius = dr.x
                else:
                    self.state = 'End'
            case 'End':
                self.setup()
            case _:
                pass

    def on_mousedown(self, ev):
        if ev.button == 1 and pygame.Vector2(self.pos).distance_to(ev.pos) <= self.current_img_radius:
            self.state = 'C'
            self.pev(GameEvents.ScoreUpdate, score=+3)
        else:
            self.pev(GameEvents.ScoreUpdate, score=-2)

    def on_paint(self, ev):
        img = pygame.transform.smoothscale_by(self.image, self.radius / self.max_radius)
        self.current_img_radius = pygame.Vector2().distance_to(img.get_size()) * 0.4
        ev.screen.blit(img, img.get_rect(center=self.pos))
