import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.circle import Circle
from src.game_objects.label import Label
from src.game_objects.game_manager import GameManager
import globals


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Circle(),
            GameManager(),
            score_label := Label(480, 60, "0", 60, "white"),
        ]
        self.score_label = score_label
        score_label.on_score_update = lambda ev: score_label.update_text(str(globals.SharedVars.SCORE))

    def enter(self):
        for i in self.components:
            i.turn_on()
        self.score_label.update_text(str(globals.SharedVars.SCORE))

    def release(self):
        for i in self.components:
            i.turn_off()
