from manim import *

class DatasetOnNumberLine(Scene):
    def construct(self):
        # Create horizontal and vertical number lines
        x_axis = NumberLine(x_range=[-1, 10, 1], length=12, color=BLUE)
        y_axis = NumberLine(x_range=[-1, 10, 1], length=12, color=RED).rotate(PI/2)

        # Position vertical axis correctly
        y_axis.shift(LEFT * x_axis.n2p(0)[0])  # Align with x-axis center

        # Group axes for easier manipulation
        axes = VGroup(x_axis, y_axis)

        # Add labels
        x_label = MathTex("x").next_to(x_axis, RIGHT)
        y_label = MathTex("y").next_to(y_axis, UP)

       
        dataset = [(-1, 2), (2, 4), (5, -3), (7, 1), (9, -2)]

        # Create dots for each data point
        dots = VGroup(*[Dot(point=x_axis.n2p(x) + y_axis.n2p(y), color=YELLOW) for x, y in dataset])

        # Play animations
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(FadeIn(dots))  # Show dataset points
        self.wait(2)
