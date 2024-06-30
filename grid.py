import pygame
from colors import Colors

class Grid:
    """
    Class representing the game grid.

    Attributes:
        num_rows (int): Number of rows in the grid.
        num_cols (int): Number of columns in the grid.
        cell_size (int): Size of each cell in the grid.
        grid (list): 2D list representing the grid.
        colors (list): List of colors for the cells.
    """
    def __init__(self):
        """
        Initialize a Grid instance.
        """
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        """
        Print the grid to the console.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        """
        Check if a position is inside the grid.

        Args:
            row (int): Row position.
            column (int): Column position.

        Returns:
            bool: True if inside the grid, False otherwise.
        """
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols

    def is_empty(self, row, column):
        """
        Check if a cell is empty.

        Args:
            row (int): Row position.
            column (int): Column position.

        Returns:
            bool: True if the cell is empty, False otherwise.
        """
        return self.grid[row][column] == 0

    def is_row_full(self, row):
        """
        Check if a row is full.

        Args:
            row (int): Row index.

        Returns:
            bool: True if the row is full, False otherwise.
        """
        return all(self.grid[row][column] != 0 for column in range(self.num_cols))

    def clear_row(self, row):
        """
        Clear a row by setting all its cells to 0.

        Args:
            row (int): Row index.
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Move a row down by a given number of rows.

        Args:
            row (int): Row index.
            num_rows (int): Number of rows to move down.
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Clear all full rows and move the above rows down.

        Returns:
            int: Number of rows cleared.
        """
        completed = 0
        for row in range(self.num_rows - 1, -1, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """
        Reset the grid by clearing all cells.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        """
        Draw the grid on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                # Draw the grid lines
                pygame.draw.rect(screen, Colors.black, cell_rect, 1)
