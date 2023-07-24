# Defining the `Game` state

Let us make a file called `game.py` inside the `src/game_states` directory. <br>
To define the main `Game` state, we need to inherit the
`BaseGameState` class.

```python
import pyved_engine as pyv

class GameState(pyv.BaseGameState):
    pass
```

The `GameState` object must define the `enter` and `exit` methods.
They are called when the game enters this state and exits
from this state respectively.

<div align="center">

```mermaid
 flowchart LR
    start((Start)) -->|enter| Game[Game State]
    Game -->|release| exit((Exit))
```

</div>

```python
import pyved_engine as pyv

class GameState(pyv.BaseGameState):
    def enter(self):
        pass

    def release(self):
        pass

```

Now that we have defined the `game` state, let us do the same
for the rest of the states, i.e. `home`, `win`, and `lose`.
So, let us make the following files with the following code
in the `src/game_states` directory:

### Home `home.py`
```python
import pyved_engine as pyv


class HomeState(pyv.BaseGameState):
    def enter(self):
        pass

    def release(self):
        pass

```

### Win `win.py`
```python
import pyved_engine as pyv


class WinState(pyv.BaseGameState):
    def enter(self):
        pass

    def release(self):
        pass

```

### Lose `lose.py`
```python
import pyved_engine as pyv


class LoseState(pyv.BaseGameState):
    def enter(self):
        pass

    def release(self):
        pass

```

Now that we have defined the states, we can map them
to the actual game in the `main.py` file so that we can run them.

Let us go to `main.py` and add the following code:

```python
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
            GameStates.Home: HomeState,
            GameStates.Game: GameState,
            GameStates.Win: WinState,
            GameStates.Lose: LoseState
        }
        return GameStates, mapping


Game().loop()
```

We define a `Game` class which inherits `pyv.GameTpl`. 
The `GameTpl` is an abstract class that will make handling scenes
easier for us. We are going to override the following `2` methods:
- `get_video_mode`
- `list_game_states`

The `get_video_mode` method will now return the constant
`pyv.HIGHRES_MODE`. This means the game window will render in
100% resolution of the screen.

The `list_game_states` method is used to return a mapping, i.e.
a dictionary with keys referencing the `GameStates` enums, and 
the corresponding values being the respective states we defined
in the `game_states` directory.

Now, we need to define the `Game` State in details. But, before
we do that, we need to note that the current **active** state is
the `Home` state because of the order of definitions in our mapping
returned from the `list_game_states` method.

So, to set our current **active** state to the `Game` state,
we need to add the following code to the `enter` method of the
`Home` state in `home.py` file:

```python
import pyved_engine as pyv
import globals


class HomeState(pyv.BaseGameState):
    def enter(self):
        pyv.get_ev_manager().post(
            pyv.EngineEvTypes.StatePush, 
            state_ident=globals.GameStates.Game
        )

    def pause(self):
        pass

    def resume(self):
        pass

    def release(self):
        pass

```