# Making a Clickable Object

## Making the file

The `Clickable` Object needs to be defined now. The benefit of `pyved-engine` is that
it allows us to define our own classes while inheriting features from existing ones.
This allows for a range of flexibility that you get while designing your game.

To maintain proper organization, we should create a new file named `clickable.py`. Within this file, we will include all
the necessary definitions for the `Clickable` object.

## Writing the class

The `Clickable` class needs to react to user events like `MousePressed` etc.
This means that it should **_listen_** to **_events_**.
Therefore, we should inherit the `EventListener` class, or as the engine describes,
`EvListener` class.

```python
import pyved_engine as pyv

class Clickable(pyv.EvListener):
    def __init__(self):
        super().__init__(self)
```

