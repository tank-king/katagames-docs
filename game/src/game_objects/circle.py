import pyved_engine as pyv


class Circle(pyv.EvListener):
    def __init__(self):
        super().__init__()
        self.state = 1

    def on_update(self, ev):
        pass

    def on_paint(self, ev):
        pass
