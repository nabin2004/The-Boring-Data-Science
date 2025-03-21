from manim import *

class InteractiveScene(Scene):
    def construct(self):
        # Create the quote text
        words = Text(
            """
            ``There is hardly any theory which is more elementary 
            than linear algebra, in spite of the fact that generations 
            of professors and textbook writers have obscured its 
            simplicity by preposterous calculations with matrices.''
            """, 
            organize_left_to_right=False  # Organize text from left to right
        )
        
        # Set the width and align it to the top
        # words.set_width(2*(FRAME_X_RADIUS-1))
        words.to_edge(UP)        
        
        # Highlight specific words (from index 48 to 49+13)
        for mob in words.submobjects[48:49+13]:
            mob.set_color(GREEN)
        
        # Create the author text
        author = Text("-Jean Dieudonn\\'e")
        author.set_color(YELLOW)
        author.next_to(words, DOWN)  # Place the author's name below the quote
        
        # Play the animations
        self.play(FadeIn(words))  # Fade in the quote
        self.wait(3)  # Wait for 3 seconds
        self.play(Write(author, run_time=5))  # Write the author's name
        self.wait()  # Wait before proceeding

        # Create and animate a circle
        circle = Circle()
        self.play(Create(circle))  # Use 'Create' for proper circle creation animation
        self.interactive_embed()  # Enable interactive mode

# Run the scene
if __name__ == "__main__":
    InteractiveScene().render()
