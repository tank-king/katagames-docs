import pyved_engine as pyv
import globals


class HomeState(pyv.BaseGameState):
    def enter(self):
        pyv.get_ev_manager().post(pyv.EngineEvTypes.StatePush, state_ident=globals.GameStates.Game)

    def pause(self):
        pass

    def resume(self):
        pass

    def release(self):
        pass
