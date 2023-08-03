import pyved_engine as pyv

from globals import GameStates

from src.game_states.home import HomeState
from src.game_states.game import GameState
from src.game_states.win import WinState
from src.game_states.lose import LoseState


class Game(pyv.GameTpl):
    def get_video_mode(self):
        return pyv.HIGHRES_MODE

    def list_game_states(self):
        mapping = {
            GameStates.Game: GameState,
            GameStates.Home: HomeState,
            GameStates.Win: WinState,
            GameStates.Lose: LoseState
        }
        return GameStates, mapping


Game().loop()
