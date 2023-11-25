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
