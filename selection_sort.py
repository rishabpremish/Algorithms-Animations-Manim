from manim import *

class SelectionSort(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        title = Text("Selection Sort", color = WHITE).scale(0.9).to_edge(UP)
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
        j_label = Text(f"j = 0", color=WHITE).scale(0.7)
        j_label.next_to(i_label, DOWN, buff=0.15, aligned_edge=LEFT)
        j_label_position = j_label.get_center()
        self.add(j_label)

        # Red Circle (key)
        min_circle_key = Dot(radius=0.08, color=RED)
        current_min_label = Text("Current minimum", color=WHITE).scale(0.5)
        group_min = VGroup(min_circle_key, current_min_label)
        group_min.arrange(RIGHT, buff=0.1)
        group_min.next_to(j_label, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(group_min)

        # Blue Circle (key)
        current_circle_key = Dot(radius=0.08, color=BLUE)
        current_item_label = Text("Current item", color=WHITE).scale(0.5)
        group_current = VGroup(current_circle_key, current_item_label)
        group_current.arrange(RIGHT, buff=0.1)
        group_current.next_to(group_min, DOWN, buff=0.15, aligned_edge=LEFT)
        self.add(group_current)

        # Dots that move below the squares
        min_circle = Dot(radius=0.12, color=RED)
        current_circle = Dot(radius=0.12, color=BLUE)
        min_circle.move_to(squares[0].get_bottom() + DOWN * 0.3 + LEFT * 0.15)
        current_circle.move_to(squares[0].get_bottom() + DOWN * 0.3 + RIGHT * 0.15)
        self.add(min_circle, current_circle)

        n = len(numbers)
        for i in range(n - 1):
            # Update the value of i
            self.play(
                i_label.animate.become(Text(f"i = {i}", color = WHITE).scale(0.7).to_corner(UL)),
                run_time = 0.5
            )

            min_idx = i
            squares[i][0].set_fill(color = YELLOW_E, opacity = 0.5)
            
            # Move min_circle to current position
            self.play(
                min_circle.animate.move_to(squares[i].get_bottom() + DOWN * 0.3 + LEFT * 0.15),
                run_time = 0.3
            )

            for j in range(i + 1, n):
                # Update j label
                new_j_label = Text(f"j = {j}", color=WHITE).scale(0.7)
                new_j_label.move_to(j_label_position)
                self.play(
                    j_label.animate.become(new_j_label),
                    run_time = 0.3
                )
                
                # Move current_circle to current position
                self.play(
                    current_circle.animate.move_to(squares[j].get_bottom() + DOWN * 0.3 + RIGHT * 0.15),
                    run_time = 0.3
                )
                
                squares[j][0].set_fill(color = BLUE_E, opacity = 0.5)
                self.wait(0.5)
                
                if int(squares[j][1].text) < int(squares[min_idx][1].text):
                    # Remove old minimum highlighting
                    squares[min_idx][0].set_fill(color = WHITE, opacity = 0)
                    min_idx = j
                    squares[min_idx][0].set_fill(color = YELLOW_E, opacity = 0.5)
                    self.play(
                        min_circle.animate.move_to(squares[min_idx].get_bottom() + DOWN * 0.3 + LEFT * 0.15),
                        run_time = 0.3
                    )
                else:
                    squares[j][0].set_fill(color = WHITE, opacity = 0)

            if min_idx != i:
                squares[i][0].set_fill(color = GREEN_E, opacity = 0.7)
                squares[min_idx][0].set_fill(color = GREEN_E, opacity = 0.7)
                self.wait(0.5)
                
                self.play(
                    squares[i].animate.move_to(squares[min_idx].get_center()),
                    squares[min_idx].animate.move_to(squares[i].get_center()),
                    run_time = 0.8
                )
                
                temp = squares.submobjects[i]
                squares.submobjects[i] = squares.submobjects[min_idx]
                squares.submobjects[min_idx] = temp

            for square in squares:
                square[0].set_fill(color = WHITE, opacity = 0)
            
            self.wait(0.5)
        
        min_circle.animate.move_to(squares[0].get_bottom() + DOWN * 0.3 + LEFT * 0.15)
        current_circle.animate.move_to(squares[0].get_bottom() + DOWN * 0.3 + RIGHT * 0.15)
        for square in squares:
            self.play(
                square[0].animate.set_fill(color=GREEN_E, opacity=0.7).scale(1.1),
                run_time=0.2
            )
            self.play(
                square.animate.scale(1/1.1),
                run_time=0.1
            )

            
        self.wait(2)