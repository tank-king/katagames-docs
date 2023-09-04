import pygame

import pyved_engine as pyv

from globals import GameStates, GameEvents

from src.game_states.home import HomeState
from src.game_states.game import GameState
from src.game_states.score import ScoreState


class Game(pyv.GameTpl):
    def enter(self, vms=None):
        super().enter(vms)

    def get_video_mode(self):
        return pyv.HIGHRES_MODE

    def list_game_events(self):
        return GameEvents

    def list_game_states(self):
        mapping = {
            GameStates.Game: GameState,
            GameStates.Home: HomeState,
            GameStates.Score: ScoreState,
        }
        return GameStates, mapping


Game().loop()
