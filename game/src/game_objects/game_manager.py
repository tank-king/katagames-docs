import time

import pyved_engine as pyv
import globals

from src.game_objects.label import Label


class GameManager(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.timer = time.time()
        self.time_left = 15
        self.timer_label = Label(20, 20, ":00", 60, "white", anchor="topleft")

    def turn_on(self):
        super().turn_on()
        self.timer_label.turn_on()

    def turn_off(self):
        super().turn_off()
        self.timer_label.turn_off()

    def on_score_update(self, ev):
        globals.SharedVars.SCORE += ev.score

    def on_update(self, ev):
        self.time_left -= time.time() - self.timer
        self.timer = time.time()
        if self.time_left <= 0:
            pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange, state_ident=globals.GameStates.Score)
        t = int(self.time_left)
        text = ":" + str(t).zfill(2)
        self.timer_label.update_text(text)
