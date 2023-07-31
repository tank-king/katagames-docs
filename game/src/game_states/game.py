import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.circle import Circle


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Circle()
        ]

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
