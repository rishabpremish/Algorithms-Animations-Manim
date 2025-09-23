from manim import *


class InsertionSort(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        title = Text("Insertion Sort", color=WHITE).scale(0.9).to_edge(UP)
        self.add(title)
        """
        These are the numbers that will be animated.
        You can change them to whatever you would like.
        """
        numbers = [5, 4, 3, 2, 1]

        squares = VGroup()
        for num in numbers:
            square = Square(side_length=1, color=WHITE)
            text = Text(str(num), color=WHITE).scale(0.7)
            text.move_to(square.get_center())
            square_and_number = VGroup(square, text)
            squares.add(square_and_number)

        # Add the squares in a line
        squares.arrange(RIGHT, buff=0.20)
        squares.move_to(ORIGIN)

        # Show the squares on the screen
        self.add(squares)
        self.wait(1)

        # Show the value of i
        i_label = Text(f"i = 1", color=WHITE).scale(0.7).to_corner(UL)
        self.add(i_label)

        # Show the value of j
        j_label = Text(f"j = 1").scale(0.5)
        j_label.next_to(squares[1], DOWN, buff=0.2)
        self.add(j_label)

        n = len(numbers)
        # Since the first number is already sorted
        squares[0][0].set_fill(color=GREEN, opacity=0.5)
        for i in range(1, n):
            # Update the value of i
            self.play(
                i_label.animate.become(
                    Text(f"i = {i}", color=WHITE).scale(0.7).to_corner(UL)
                ),
                run_time=0.5,
            )
            j = i
            # Move j label to track the square it originally starts with
            self.play(
                j_label.animate.become(Text(f"j = {j}"))
                .scale(0.5)
                .next_to(squares[j], DOWN, buff=0.2),
                run_time=0.3,
            )
            self.wait(0.5)
            while j > 0 and int(squares[j - 1][1].text) > int(squares[j][1].text):
                num1 = int(squares[j][1].text)
                num2 = int(squares[j - 1][1].text)

                # Initialize the comparison text field
                comparison_label = Text(
                    f"Compare {num2} and {num1}", color=WHITE
                ).scale(0.5)
                comparison_label.next_to(squares, DOWN, buff=0.8)
                self.add(comparison_label)

                if num2 > num1:
                    squares[j][0].set_fill(color=YELLOW_E, opacity=0.5)
                    squares[j - 1][0].set_fill(color=YELLOW_E, opacity=0.5)
                    self.wait(0.5)
                    self.play(
                        squares[j].animate.move_to(squares[j - 1].get_center()),
                        squares[j - 1].animate.move_to(squares[j].get_center()),
                        j_label.animate.next_to(squares[j - 1], DOWN, buff=0.2),
                        run_time=0.5,
                    )

                    # Swap the squares in the VGroup
                    temp = squares.submobjects[j]
                    squares.submobjects[j] = squares.submobjects[j - 1]
                    squares.submobjects[j - 1] = temp

                    # Set the sorted part of the array to green
                    squares[j][0].set_fill(color=GREEN, opacity=0.5)
                    squares[j - 1][0].set_fill(color=GREEN, opacity=0.5)
                    self.wait(0.25)
                    j -= 1

                    # Update the j label to show the new value of j
                    self.play(
                        j_label.animate.become(Text(f"j = {j}"))
                        .scale(0.5)
                        .next_to(squares[j], DOWN, buff=0.2),
                        run_time=0.3,
                    )
                    self.remove(comparison_label)
                    self.wait(0.5)
                else:
                    squares[j][0].set_fill(color=GREEN, opacity=0.5)

                    self.remove(comparison_label)
