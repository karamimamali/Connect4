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