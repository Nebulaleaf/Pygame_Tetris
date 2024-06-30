class Colors:
    """
    Class containing color definitions used in the game.
    """
    black = (0, 0, 0)
    dark_grey = (50, 50, 50)
    grey = (100, 100, 100)
    light_grey = (150, 150, 150)
    very_light_grey = (200, 200, 200)
    red_1 = (139, 0, 0)         # Dark red
    red_2 = (178, 34, 34)       # Firebrick
    red_3 = (220, 20, 60)       # Crimson
    red_4 = (255, 0, 0)         # Red
    red_5 = (255, 99, 71)       # Tomato
    red_6 = (255, 127, 80)      # Coral
    red_7 = (255, 160, 122)     # Light Salmon
    white = (255, 255, 255)

    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.red_1, cls.red_2, cls.red_3, cls.red_4, cls.red_5, cls.red_6, cls.red_7]
