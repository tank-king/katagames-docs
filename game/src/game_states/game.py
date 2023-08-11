import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.circle import Circle
from src.game_objects.label import ScoreLabel
from src.game_objects.game_manager import GameManager
import globals


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Circle(),
            GameManager(),
            ScoreLabel("0", 60, "white"),
        ]

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
