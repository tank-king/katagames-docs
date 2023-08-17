import pygame

import pyved_engine as pyv

from globals import GameStates, GameEvents, Config

from src.game_states.home import HomeState
from src.game_states.game import GameState
from src.game_states.score import ScoreState


class Game(pyv.GameTpl):
    def enter(self, vms=None):
        super().enter(vms)
        Config.SCREEN_SIZE = pygame.Vector2(pyv.get_surface().get_size())

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
