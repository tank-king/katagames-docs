import pygame

import pyved_engine as pyv
import globals


class HomeState(pyv.BaseGameState):
    def enter(self):
        globals.Config.SCREEN_SIZE = pygame.Vector2(pyv.get_surface().get_size())
        pyv.get_ev_manager().post(pyv.EngineEvTypes.StatePush, state_ident=globals.GameStates.Game)

    def pause(self):
        pass

    def resume(self):
        pass

    def release(self):
        pass
