# Defining the `Game` state

As `pyved_engine` uses the `ECS` structure, everything in the engine is going
to be a `Component` object. The `Component` objects can **_post_** other `events` to the system (`Emitter`),
or both **_post_** and **_listen_** to events (`EventListener`).

### Adding Background

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

### Making the Circle Object

Let us now define the `Circle` object - the clickable object
that we will clck to get points in the game.<br>
Make a new file `src/game_objects/circle.py`.
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

The details of the code is not relevant to this tutorial, so any other code
can be used to achieve the same effect. The above code describes the
flowchart we designed earlier.

We will now need to define the `setup` function of the `Circle` class. This is what we use
to reset the circle to a new position once it is clicked.
The setup function will spawn the circle at a random position across the screen.
But for that we need to have access the screen dimensions.
With the **HD** mode of `pyved-engine`, the created display size is of the resolution
`960px X 720px`

So the setup function will be like this:

```python

def setup(self):
    self.state = 'Start'
    self.radius = 0
    self.max_radius = 50
    self.color = random.choice(['black', 'blue', 'grey', 'magenta', 'red'])
    self.image = pygame.transform.smoothscale_by(pygame.image.load(f'assets/images/circle_{self.color}.png'), 0.5)
    w, h = self.image.get_size()
    self.pos = pygame.Vector2(
        random.randint(w // 2, 960 - w // 2),
        random.randint(h // 2, 720 - w // 2)
    )
```

And, now we need to define what will happen when the mouse button is clicked.

```python
def on_mousedown(self, ev):
    if ev.button == 1 and pygame.Vector2(self.pos).distance_to(ev.pos) <= self.current_img_radius:
        self.state = 'C'
        self.pev(GameEvents.ScoreUpdate, score=+3)
    else:
        self.pev(GameEvents.ScoreUpdate, score=-2)
```

The `pev` method is basically an acronym for `post-event`. When the circle
is clicked, the object will notify the system that the score needs to be updated
(and by how much)

And finally, we need to define the `on_paint` method to draw the circle on the screen.

```python
def on_paint(self, ev):
    img = pygame.transform.smoothscale_by(self.image, self.radius / self.max_radius)
    self.current_img_radius = pygame.Vector2().distance_to(img.get_size()) * 0.4
    ev.screen.blit(img, img.get_rect(center=self.pos))
```

Don't forget to add the necessary imports and define the `__init__` method.
The full code for the `circle.py` file is:

```python
import random
import time

import pygame.draw

import pyved_engine as pyv
import globals

from game.globals import GameEvents


class Circle(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.state = None
        self.radius = None
        self.max_radius = None
        self.color = None
        self.pos = None
        self.image = None
        self.current_img_radius = None

    def turn_on(self):
        super().turn_on()
        self.setup()

    def setup(self):
        self.state = 'Start'
        self.radius = 0
        self.max_radius = 50
        self.color = random.choice(['black', 'blue', 'grey', 'magenta', 'red'])
        self.image = pygame.transform.smoothscale_by(pygame.image.load(f'assets/images/circle_{self.color}.png'), 0.5)
        w, h = self.image.get_size()
        self.pos = pygame.Vector2(
            random.randint(w // 2, 960 - w // 2),
            random.randint(h // 2, 720 - w // 2)
        )

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

    def on_mousedown(self, ev):
        if ev.button == 1 and pygame.Vector2(self.pos).distance_to(ev.pos) <= self.current_img_radius:
            self.state = 'C'
            self.pev(GameEvents.ScoreUpdate, score=+3)
        else:
            self.pev(GameEvents.ScoreUpdate, score=-2)

    def on_paint(self, ev):
        img = pygame.transform.smoothscale_by(self.image, self.radius / self.max_radius)
        self.current_img_radius = pygame.Vector2().distance_to(img.get_size()) * 0.4
        ev.screen.blit(img, img.get_rect(center=self.pos))

```

### Adding the Label(s)

The `Circle` method has been done, now we need to think of displaying the score
and timer. Make a new file `src/game_objects/label.py` and add the following code:

```python
import pygame.font

import pyved_engine as pyv


class Label(pyv.EvListener):
    def __init__(self, x, y, text, size, color, font='consolas', anchor='center'):
        super().__init__()
        self.pos = (x, y)
        self.args = [size, color, font]
        self.anchor = anchor
        self.text = pygame.font.SysFont(font, size).render(text, True, color)

    def get_rect(self):
        rect = self.text.get_rect()
        rect.__setattr__(self.anchor, self.pos)
        rect.y -= 5
        return rect

    def update_text(self, text):
        self.text = pygame.font.SysFont(self.args[2], self.args[0]).render(text, True, self.args[1])

    def on_paint(self, ev):
        ev.screen.blit(self.text, self.text.get_rect(**{self.anchor: self.pos}))

```

This code is self-explanatory: we define a label class which inherits the
`EventListener` type and define various methods for it.

### Adding the Game Manager

Now we have the Label and the Circle, but how do we manage the timeout? We can
make another object for that called `GameManager`.
Make a new file `src/game_objects/game_manager.py` and add the following code:

```python
import time

import pyved_engine as pyv
import globals

from src.game_objects.label import Label


class GameManager(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.timer = time.time()
        self.time_left = 15
        self.timer_label = Label(20, 20, ":00", 60, "white", anchor="topleft")

    def turn_on(self):
        super().turn_on()
        self.timer = time.time()
        self.time_left = 15
        self.timer_label.turn_on()

    def turn_off(self):
        super().turn_off()
        self.timer_label.turn_off()

    def on_score_update(self, ev):
        globals.SharedVars.SCORE += ev.score

    def on_update(self, ev):
        self.time_left -= time.time() - self.timer
        self.timer = time.time()
        if self.time_left <= 0:
            pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange, state_ident=globals.GameStates.Score)
        t = int(self.time_left)
        text = ":" + str(t).zfill(2)
        self.timer_label.update_text(text)

```


The line `pyv.get_ev_manager().post(pyv.EngineEvTypes.StateChange, state_ident=globals.GameStates.Score)`
is used to change the state to the `Score` state where we will display the final score and high score.

Note that we added a `timer_label` Label as a child of this class. The good thing
about EventListener objects is that one can add them in a hierarchical fashion without
affecting anything.
We have added a time counter of `15` seconds, and use the `time.time()` method
for measuring the time difference.

We also defined a method `on_score_update` which will be called when the
`ScoreUpdate` event has been posted. When the method is called, we update the
global Score variable.

### Defining the `Game State` completely

We have now defined all the required components for the `Game` state. Let us add
them as components to the state.

```python
import pyved_engine as pyv

from src.game_objects.background import ColorBackground
from src.game_objects.circle import Circle
from src.game_objects.label import Label
from src.game_objects.game_manager import GameManager
import globals


class GameState(pyv.BaseGameState):
    def __init__(self, ident):
        super().__init__(ident)
        self.components = [
            ColorBackground(color="#36354A"),
            Circle(),
            GameManager(),
            score_label := Label(480, 60, "0", 60, "white"),
        ]
        self.score_label = score_label
        score_label.on_score_update = lambda ev: score_label.update_text(str(globals.SharedVars.SCORE))

    def enter(self):
        for i in self.components:
            i.turn_on()
        self.score_label.update_text(str(globals.SharedVars.SCORE))

    def release(self):
        for i in self.components:
            i.turn_off()

```

The line: `score_label.on_score_update = lambda ev: score_label.update_text(str(globals.SharedVars.SCORE))
` is used to dynamically assign the `on_score_update` method to the score_label.

We now have the full Game State done.