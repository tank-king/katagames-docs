import sys

import globals
from src.game_objects.background import ColorBackground
from src.game_objects.button import Button
from src.game_objects.label import Label

import pyved_engine as pyv


class HomeState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Label(480, 250, "Game Title", 100, "white"),
            Button(480, 450, " Play ", 50, "white",
                   callback=lambda: pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange,
                                                              state_ident=globals.GameStates.Game)),
            Button(480, 550, " Quit ", 50, "white", callback=lambda: sys.exit(0))
        ]

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
