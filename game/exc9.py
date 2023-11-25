import random

class Connect4:
    def __init__(self):
        # Initialize an empty grid with six rows and seven columns
        self.grid = [[' ' for _ in range(7)] for _ in range(6)]

    def __str__(self):
        # Return a string representation of the grid
        grid_str = ""
        for row in self.grid:
            grid_str += "|".join(row) + "\n"
        grid_str += "---------------\n"
        return grid_str

    def clear_grid(self):
        # Clear the grid by resetting each cell to empty
        for row in range(6):
            for col in range(7):
                self.grid[row][col] = ' '


    def show_grid(self):
        # Display column numbers at the top
        print("    1 2 3 4 5 6 7")
        print("  " + "---------------")
        
        # Display the contents of the grid with row numbers on the left and right sides
        for row_num, row in enumerate(self.grid, start=1):
            print(f"{row_num} | {' '.join(row)} | {row_num}")
        
        # Display column numbers at the bottom
        print("  " + "---------------")
        print("    1 2 3 4 5 6 7")


    def is_valid_move(self, column):
        # Check if it is possible to play in a given column
        return self.grid[0][column - 1] == ' '


    def drop_disc(self, column, color):
        # Drop a disc in the specified column
        for row in range(5, -1, -1):
            if self.grid[row][column - 1] == ' ':
                self.grid[row][column - 1] = color
                break

    def count_aligned_disc(self, column, row, color):
        # Count aligned discs in all directions
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Include vertical, horizontal, and both diagonals
        max_count = 0

        for direction in directions:
            dx, dy = direction
            count = 1  # Start with 1 to account for the current disc

            # Check in one direction
            current_row, current_col = row + dx, column + dy
            while 0 <= current_row < 6 and 0 <= current_col < 7 and self.grid[current_row][current_col] == color:
                count += 1
                current_row += dx
                current_col += dy

            # Check in the opposite direction
            current_row, current_col = row - dx, column - dy
            while 0 <= current_row < 6 and 0 <= current_col < 7 and self.grid[current_row][current_col] == color:
                count += 1
                current_row -= dx
                current_col -= dy

            max_count = max(max_count, count)

        return max_count


    def recommend_column(self, color):
        # Check if a winning move exists and recommend it
        for col in range(1, 8):
            if self.is_valid_move(col):
                # Create a copy of the grid for simulation
                grid_copy = [row[:] for row in self.grid]
                self.drop_disc(col, color)
                if self.count_aligned_disc(col, 5, color) >= 4:
                    self.grid[col - 1][5] = ' '  # Undo the move
                    return col
                # Undo the move
                self.grid = [row[:] for row in grid_copy]

        valid_columns = [col for col in range(1, 8) if self.is_valid_move(col)]
        random.shuffle(valid_columns)
        max_alignment = 0
        recommended_column = valid_columns[0]

        for col in valid_columns:
            for row in range(6):
                if self.is_valid_move(col):
                    # Create a copy of the grid for simulation
                    grid_copy = [row[:] for row in self.grid]
                    self.drop_disc(col, color)
                    alignment = self.count_aligned_disc(col, row, color)
                    if alignment >= max_alignment:
                        max_alignment = alignment
                        recommended_column = col
                    # Undo the move
                    self.grid = [row[:] for row in grid_copy]

        return recommended_column

    def check_winner(self, color):
        # Check if the current player has won
        for row in range(6):
            for col in range(7):
                if self.grid[row][col] == color:
                    if (
                        self.count_aligned_disc(col, row, color) >= 4 or  # Horizontal
                        self.count_aligned_disc(col, row, color) >= 4 or  # Vertical
                        self.count_aligned_disc(col, row, color) >= 4 or  # Diagonal /
                        self.count_aligned_disc(col, row, color) >= 4     # Diagonal \
                    ):
                        return True
        return False




    def play_game(self):
        print("Welcome to Connect 4!")

        # Decide who goes first
        current_player = 'o'  # Yellow goes first
        computer_player = '*'  # Red is the computer player

        while True:
            # Display the current state of the grid
            self.show_grid()

            # Check if the current player is a human or the computer
            if current_player == 'o':
                # Human player's turn
                while True:
                    try:
                        column = int(input(f"Player {current_player.upper()}, choose a column (1-7): "))
                        if 1 <= column <= 7 and self.is_valid_move(column):
                            break
                        else:
                            print("Invalid move. Please choose a valid column.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            else:
                # Computer player's turn
                column = self.recommend_column(computer_player)
                print(f"Computer chooses column {column}")

            # Drop the disc in the chosen column
            self.drop_disc(column, current_player)

            # Check if the current player has won
            if self.check_winner(current_player):
                self.show_grid()
                print(f"Player {current_player.upper()} wins!")
                break

            # Check for a tie
            if all(self.grid[row][col] != ' ' for row in range(6) for col in range(7)):
                self.show_grid()
                print("It's a tie!")
                break

            # Switch to the next player
            current_player = '*' if current_player == 'o' else 'o'