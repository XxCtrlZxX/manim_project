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

COLOR_P = "#3EFC24"


class TextColor(Scene):
    def construct(self):
        text = TextMobject("A", "B", "C", "D", "E", "F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)
