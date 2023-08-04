import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.circle import Circle
from src.game_objects.label import ScoreLabel
import globals


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Circle(),
            ScoreLabel(0, 0, "Score: 0", 40, "white")
        ]

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
