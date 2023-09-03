# Defining the `Game` state

As `pyved_engine` uses the `ECS` structure, everything in the engine is going
to be a `Component` object. The `Component` objects can **_post_** other `events` to the system (`Emitter`),
or both **_post_** and **_listen_** to events (`EventListener`).

Every frame, we need to refresh the screen with a color or a background.
So let us write a `Background` component which will fill the screen
with a color per frame.

Let us make a file named `background.py` in `src/game_objects` and
add the following code:

```python
import pyved_engine as pyv


class ColorBackground(pyv.EvListener):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def on_paint(self, ev):
        ev.screen.fill(self.color)

```

A couple of things to note here:

We defined a `BackgroundColor` class which inherits the `pyv.EvListener`
class. This means this class can **_post_** as well as **_listen_** to events.

Then we passed a color value to the `__init__` method. This color
will be the color that is used to fill the screen per frame.

Then, we defined the `on_paint` event. Remember to have the exact
signature of the method. The `ev` argument passed to the method is
the event object that triggered this method. We can get the `screen`
object using the `ev.screen` attribute.<br>
Then we fill the screen using the color value we passed.

Let us now instantiate this object and add it as a component to
the `GameState` class.

Go over to `src/game_states/game.py` and modify it using the following code:

```python
import pyved_engine as pyv

from src.game_objects.background import ColorBackground


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A")
        ]

    def enter(self):
        for i in self.components:
            i.turn_on()

    def release(self):
        for i in self.components:
            i.turn_off()
```

In the `__init__` method, we have created a list of components.
And in the `enter` method, we turn on the components, i.e. *activate*
them. We turn them off in the `release` method.

Let us now define the `Circle` object - the clickable object
that we will clck to get points in the game.<br>
Before writing the code, let us draw a class diagram for the Circle class:

<div align="center">

```mermaid
classDiagram
Circle

class Circle{
<<EventListener>>
radius: float
max_radius: float
color: Color
position: Vector2

on_paint()
on_update()
on_mousedown()
}

```

</div>
And here is the flowchart for the stages / states:
<div align="center">

```mermaid
flowchart LR
    start --> A
    A --> B
    B --> C
    C --> D[END]
```

| state | description                                                                  | transition |
|-------|------------------------------------------------------------------------------|------------|
| Start | the object is initialized                                                    | A          |
| A     | the `radius` increases until it reaches `max_radius`                         | B          |
| B     | the object waits for user input and keeps decreasing radius with time        | C          |
| C     | if clicked or timer ends for the object, its `radius` decreases rapidly to 0 | End        |
| End   | the object is re-initialized into a new position                             |            |

</div>

The code for the structure can be written as follows in the `on_update` function:
```python
def on_update(self, ev):
    match self.state:
        case 'Start':
            self.state = 'A'
        case 'A':
            dr = pygame.Vector2(self.radius, self.radius).lerp(
                pygame.Vector2(self.max_radius, self.max_radius), 0.25
            )
            self.radius = dr.x
            if self.max_radius - self.radius <= 1:
                self.state = 'B'
        case 'B':
            self.radius -= 0.3
            if self.radius <= 0:
                self.radius = 0
                pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange, state_ident=globals.GameStates.Score)
        case 'C':
            if self.radius > 1:
                dr = pygame.Vector2(self.radius, self.radius).lerp(
                    pygame.Vector2(0, 0), 0.5
                )
                self.radius = dr.x
            else:
                self.state = 'End'
        case 'End':
            self.setup()
        case _:
            pass
```
The details of the code is not related to this tutorial, so any other code
can be used to achieve the same effect. The above code describes the
flowchart we designed earlier.




