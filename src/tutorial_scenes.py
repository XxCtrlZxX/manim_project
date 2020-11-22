from manimlib.imports import *
from .screen_grid import ScreenGrid


class WriteText(Scene):
    def construct(self):
        text = TextMobject("Hello World!")
        self.play(Write(text))
        self.wait(3)


class Positions(Scene):
    def construct(self):
        grid = ScreenGrid()
        object = Dot()
        object.to_edge(UP)
        self.add(grid, object)
        self.wait()
