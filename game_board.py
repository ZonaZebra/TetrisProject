from tetrimino import Tetrimino


class GameBoard:
    def __init__(self, width, height):
        # Initialize game board, lines_cleared, score, level
        # ...
        pass

    def get_empty_board(self):
        # Return an empty board with the dimensions board_width x board_height
        # ...
        pass

    def add_tetrimino(self, tetrimino):
        # Add a Tetrimino to the board after it reaches its final position
        # ...
        pass

    def clear_lines(self):
        # Check for and clear any full lines
        # ...
        pass

    def is_game_over(self):
        # Check if the game is over (e.g., a new Tetrimino cannot be placed)
        # ...
        pass

    def get_next_tetrimino(self):
        # Generate the next Tetrimino piece
        # ...
        pass
