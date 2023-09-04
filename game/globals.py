import pyved_engine as pyv

GameStates = pyv.struct.enum(
    'Home',
    'Game',
    'Score',
)

GameEvents = pyv.game_events_enum((
    'ScoreUpdate',
))


class SharedVars:
    SCORE = 0
    HIGH_SCORE = 0


class Config:
    SCREEN_SIZE = None
