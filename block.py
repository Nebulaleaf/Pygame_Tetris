import pygame
from colors import Colors
from position import Position

from colors import Colors

class Block:
    """
    Class representing a Tetris block.

    Attributes:
        id (int): The block ID.
        cells (dict): Dictionary of block rotation states.
        cell_size (int): Size of a single cell.
        row_offset (int): Row offset of the block.
        column_offset (int): Column offset of the block.
        rotation_state (int): Current rotation state of the block.
        colors (list): List of colors for the blocks.
        color (tuple): The color of the block.
    """
    def __init__(self, id):
        """
        Initialize a Block instance.

        Args:
            id (int): The block ID.
        """
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        self.color = Colors.red_4  # Default color, update this if needed

    def move(self, rows, columns):
        """
        Move the block by a given number of rows and columns.

        Args:
            rows (int): Number of rows to move.
            columns (int): Number of columns to move.
        """
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        """
        Get the positions of the cells in the current rotation state.

        Returns:
            list: List of cell positions.
        """
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        """
        Rotate the block to the next rotation state.
        """
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        """
        Undo the last rotation.
        """
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        """
        Draw the block on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
            offset_x (int): X offset for drawing.
            offset_y (int): Y offset for drawing.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color, tile_rect)
