import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.label import Label


class ScoreState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            score_label := Label(0, 0, ),
        ]
        self.score = ...

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
