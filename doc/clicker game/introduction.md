# Introduction

## Prerequisites

This tutorial assumes that you have a basic knowledge of Python and Object-Oriented Programming (OOP) concepts, such as
inheritance and abstraction.

## Installing the engine

Before we begin, you need to install the game engine. Please follow the installation instructions provided by the
engine's [documentation]().

## Writing the Code

Since we don't have a GUI at this point, we will be writing the entire game code. However, the game engine will simplify
our work by handling many aspects internally.

The first step is to create a main script called `main.py`.

### Importing libraries

Start by importing the pyved_engine module in our script

```python
import pyved_engine as pyv
```

The `as` keyword will help us refer to the engine as pyv from now on, saving us
from writing `pyved_engine` repeatedly.

### Creating the Game class

Create the `Game` class, which serves as the main class that defines everything related to running the game. To utilize
the engine's features, we need to inherit this class from the `GameTpl` class:

```python
class Game(pyv.GameTpl)
```

### Creating a window

The next step is to create a window where our game will run. To achieve this, the `GameTpl` class requires the
`get_video_mode` method to be overridden, which determines the game's resolution scaling. Modify the code as follows:

```python
class Game(pyv.GameTpl):
    def get_video_mode(self):
        return pyv.HIGHRES_MODE
```

Here, we returned pyv.HIGHRES_MODE, which is one of the available [graphics resolutions]() supported by the engine. You can
find more details about available resolutions in the engine's [documentation]().

Now, at the bottom of the file, write:
```python
if __name__ == '__main__':
    game = Game()
    game.loop()
```

Running the `main.py` file should give us a game window with a black screen.
The screen is now set up!

Now we can jump to making a Clickable circle in the [next page]().