from manim import *

class PiCreatureExample(Scene):
    def construct(self):
        # Load the PiCreature SVG
        pi_creature = SVGMobject("PiCreatures_confused.svg")
        pi_creature.scale(1)  # Scale down if too large
        pi_creature.move_to(ORIGIN)  # Move to the center of the screen

        # Load the thought bubble SVG and position it above PiCreature
        thought_bubble = SVGMobject("Bubbles_thought.svg",color=WHITE)
        thought_bubble.scale(0.5)  # Adjust the scale of the bubble
        thought_bubble.next_to(pi_creature, UP, buff=0.3)  # Position above PiCreature

        # Add text to the thought bubble
        thought_text = Text("WTF is going on?", color=WHITE).move_to(thought_bubble.get_center())

        # Add PiCreature, thought bubble, and text to the scene
        self.play(Write(pi_creature))
        self.play(Write(thought_bubble), Write(thought_text))  # Display the thought bubble and text
        self.wait(2)  # Wait for a couple of seconds to view the scene
