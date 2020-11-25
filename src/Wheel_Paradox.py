from manimlib.imports import *


class MainScene(Scene):
    def construct(self):
        wheel = SVGMobject("car-wheel").scale(1.5).shift(UP)
        self.play(DrawBorderThenFill(wheel, rate_func=linear, run_time=3))
        self.wait(2)

        name = TextMobject("20626 정해성").shift(DOWN * 2)
        self.play(Write(name))
        self.wait(2)


class CircleScene(Scene):
    def construct(self):
        wheel = SVGMobject("car-wheel").scale(1.5).shift(UP)
        name = TextMobject("20626 정해성").shift(DOWN * 2)
        self.add(wheel, name)

        wheel.generate_target()
        wheel.target.shift(LEFT * PI + DOWN)
        wheel.target.scale(0.66)
        self.play(MoveToTarget(wheel), run_time=2)
        self.wait(2)

        circle_big = Circle().move_to(wheel).set_color(YELLOW).set_stroke(width=5)
        circle_small = Circle().scale(0.5).move_to(wheel).set_color(ORANGE).set_stroke(width=5)
        self.play(ReplacementTransform(wheel, circle_big))
        self.play(ReplacementTransform(name, circle_small))
        self.wait(2)


class RollACircle(Scene):
    def construct(self):
        # 초기 화면 설정
        circle_big = Circle().set_color(YELLOW).set_stroke(width=5)
        circle_small = Circle().scale(0.5).set_color(ORANGE).set_stroke(width=5)
        circle_big.shift(LEFT * PI)
        circle_small.shift(LEFT * PI)
        self.add(circle_big, circle_small)

        center_line = Line(circle_big.get_center(), circle_big.get_bottom())
        self.play(ShowCreation(center_line))
        self.wait()
        
        # Rolling : 고쳐야 함
        wheel = VGroup(circle_big, circle_small, center_line)
        wheel.generate_target()
        wheel.target.shift(RIGHT * 2 * PI)
        wheel.target.rotate(2 * PI)
        self.play(MoveToTarget(wheel), run_time=3)
        self.wait()

        line1 = Line(circle_big.get_bottom(), circle_big.get_bottom() + RIGHT * PI * 2)
        line1.set_color(YELLOW).set_stroke(width=3)
        line2 = Line(circle_small.get_bottom(), circle_small.get_bottom() + RIGHT * PI * 2)
        line2.set_color(ORANGE).set_stroke(width=3)
        self.play(ShowCreation(line1), ShowCreation(line2))
        self.wait()