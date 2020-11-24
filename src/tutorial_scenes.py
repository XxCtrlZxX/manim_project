from manimlib.imports import *
from .screen_grid import ScreenGrid


class WriteText(Scene):
    def construct(self):
        text_eng = TextMobject("Hello World!")
        text_eng.move_to(UP)
        text_kor = TextMobject("안녕!")
        self.play(Write(text_eng))
        self.wait()
        self.play(Write(text_kor))
        self.wait()


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


class CrossText1(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i", "=", "-\\frac{1}{2}").scale(3)
        cross = Cross(text[2])
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait()


class TransformationText1V1(Scene):
    def construct(self):
        texto1 = TextMobject("First text")
        texto1.to_edge(UP)
        texto2 = TextMobject("Second text").set_color(RED)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()


class CopyTextV1(Scene):
    def construct(self):
        formula = TexMobject(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
            # 0               1    2    3    4    5    6    7                8    9    10               11
            )
        formula.scale(2)
        self.play(Write(formula[0:7]))
        self.wait()
        changes = [
            # step 1
            [(2, 4, 3), (8, 11, 9)],
            # step 2
            [(0, 0), (7, 10)]
        ]
        for pre_ind, post_ind in changes:
            self.play(
                *[
                    ReplacementTransform(formula[i].copy(), formula[j])
                    for i, j in zip(pre_ind, post_ind)
                ]
            )
            self.wait()
        self.wait()
        # self.play(
        #     ReplacementTransform(formula[2].copy(), formula[8]),
        #     ReplacementTransform(formula[4].copy(), formula[11]),
        #     ReplacementTransform(formula[3].copy(), formula[9])
        #     )
        # self.wait()
        # self.play(
        #     ReplacementTransform(formula[0].copy(), formula[7]),
        #     ReplacementTransform(formula[0].copy(), formula[10])
        #     )
        # self.wait()


class SVGText(Scene):
    def construct(self):
        car_wheel = SVGMobject("car-wheel").scale(1.5)
        car_wheel.move_to(UP)
        self.play(DrawBorderThenFill(car_wheel, rate_func=linear))
        self.wait()
