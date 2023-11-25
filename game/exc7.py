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
        # Coun aligned dics
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        max_count = 0

        for direction in directions:
            dx, dy = direction
            count = 0
            current_row, current_col = row, column

            while 0 <= current_row < 6 and 0 <= current_col < 7 and self.grid[current_row][current_col] == color:
                count += 1
                current_row += dx
                current_col += dy

            current_row, current_col = row - dx, column - dy

            while 0 <= current_row < 6 and 0 <= current_col < 7 and self.grid[current_row][current_col] == color:
                count += 1
                current_row -= dx
                current_col -= dy

            max_count = max(max_count, count)

        return max_count

    def recommend_column(self, color):
        valid_columns = [col for col in range(1, 8) if is_valid_move(grid, col)]
        random.shuffle(valid_columns)  # Shuffle to recommend a random valid column
        max_alignment = 0
        recommended_column = valid_columns[0]

        for col in valid_columns:
            for row in range(6):
                if is_valid_move(self.grid, col):
                    alignment = count_aligned_disc(self.grid, col, row, color)
                    if alignment >= max_alignment:
                        max_alignment = alignment
                        recommended_column = col

        return recommended_column