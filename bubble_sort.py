from manim import *

class BubbleSort(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        title = Text("Bubble Sort", color = WHITE).scale(0.9).to_edge(UP)
        self.add(title)
        """
        These are the numbers that will be animated.
        You can change them to whatever you would like.
        """
        numbers = [5, 4, 3, 2, 1]

        squares = VGroup()

        for num in numbers:
            square = Square(side_length = 1, color = WHITE)
            text = Text(str(num), color = WHITE).scale(0.7)
            text.move_to(square.get_center())
            square_and_number = VGroup(square, text)
            squares.add(square_and_number)
        
        # Add the squares in a line
        squares.arrange(RIGHT, buff = 0.20)
        squares.move_to(ORIGIN)

        # Show the squares on the screen
        self.add(squares)
        self.wait(1)

        # Show the value of i
        i_label = Text(f"i = 0", color = WHITE).scale(0.7).to_corner(UL)
        self.add(i_label)

        # Show the value of j
        j_label = Text(f"j = 0").scale(0.5)
        j_label.next_to(squares[0], DOWN, buff=0.2)
        self.add(j_label)

        n = len(numbers)
        for i in range(n):
            # Update the value of i
            self.play(
                i_label.animate.become(Text(f"i = {i}", color = WHITE).scale(0.7).to_corner(UL)),
                run_time = 0.5
            )

            for j in range(n - i - 1):
                self.play(
                    j_label.animate.become(Text(f"j = {j}")).scale(0.5).next_to(squares[j], DOWN, buff = 0.2),
                    run_time = 0.2
                )
                num1 = int(squares[j][1].text)
                num2 = int(squares[j+1][1].text)

                # Initialize the comparison text field
                comparison_label = Text(f"Compare {num1} and {num2}", color=WHITE).scale(0.5)
                comparison_label.next_to(squares, DOWN, buff=0.8)
                self.add(comparison_label)

                if num1 > num2:
                    self.wait(0.25)
                    squares[j][0].set_fill(color=YELLOW_E, opacity = 0.5)
                    squares[j+1][0].set_fill(color=YELLOW_E, opacity = 0.5)
                    self.wait(0.1)
                    self.play(
                        squares[j].animate.scale(1.15),
                        squares[j+1].animate.scale(1.15),
                        run_time=0.3
                    )
                    self.play(
                        squares[j].animate.move_to(squares[j+1].get_center()),
                        squares[j+1].animate.move_to(squares[j].get_center()),
                        run_time=1.2
                    )
                    self.play(
                        squares[j].animate.scale(1/1.15),
                        squares[j+1].animate.scale(1/1.15),
                        run_time=0.3
                    )
                    squares[j][0].set_fill(color = BLACK, opacity = 0)
                    squares[j+1][0].set_fill(color = BLACK, opacity = 0)

                    temp = squares.submobjects[j+1]
                    squares.submobjects[j+1] = squares.submobjects[j]
                    squares.submobjects[j] = temp
                    self.remove(comparison_label)


                elif num1 < num2 or num1 == num2:
                    self.wait(0.5)
                    squares[j][0].set_fill(color=GREEN_E, opacity = 0.5)
                    self.wait(0.3)
                    squares[j+1][0].set_fill(color=GREEN_E, opacity = 0.5)
                    self.wait(0.8)
                    squares[j][0].set_fill(color = BLACK, opacity = 0)
                    squares[j+1][0].set_fill(color = BLACK, opacity = 0)
                    self.wait(0.7)
                    self.remove(comparison_label)
                    
        for square in squares:
            self.play(
                square[0].animate.set_fill(color=GREEN_E, opacity=0.7).scale(1.1),
                run_time=0.2
            )
            self.play(
                square.animate.scale(1/1.1),
                run_time=0.1
            )