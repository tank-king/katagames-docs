import pyved_engine as pyv

GameStates = pyv.struct.enum(
    'Home',
    'Game',
    'Win',
    'Lose',
)
