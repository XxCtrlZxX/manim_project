from manimlib.imports import *


class WriteText(Scene):
    def construct(self):
        text = TextMobject("Hello World!")
        self.play(Write(text))
        self.wait(3)



