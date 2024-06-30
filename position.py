class Position:
    """
    Class representing a position on the grid.

    Attributes:
        row (int): The row position.
        column (int): The column position.
    """
    def __init__(self, row, column):
        """
        Initialize a Position instance.

        Args:
            row (int): The row position.
            column (int): The column position.
        """
        self.row = row
        self.column = column
