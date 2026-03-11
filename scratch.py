import pygame
import random


class Tetromino:
    Shapes = [
        [[1, 1, 1, 1]],  # I shape
        [[1, 1], [1, 1]],  # O shape
        [[0, 1, 0], [1, 1, 1]],  # T shape
        [[1, 0, 0], [1, 1, 1]],  # J shape
        [[0, 0, 1], [1, 1, 1]],  # L shape
        [[1, 1, 0], [0, 1, 1]],  # S shape
        [[0, 1, 1], [1, 1, 0]],  # Z shape
    ]
    """Define the constants for the grid dimensions and cell size"""
    # Define colors for each tetromino type
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Cyan = (0, 255, 255)
    Blue = (0, 0, 255)
    Orange = (255, 165, 0)
    Yellow = (255, 255, 0)
    Green = (0, 255, 0)
    Purple = (128, 0, 128)
    Magenta = (255, 0, 255)
    Gray = (128, 128, 128)  # colour for the border
    Colors = {
        "I": "cyan",
        "O": "yellow",
        "T": "purple",
        "J": "blue",
        "L": "orange",
        "S": "green",
        "Z": "red",
    }
    # Define game dimensions
    BlockSize = 30  # Size of each block in pixels
    GridWidth = 10  # Number of columns in the game grid
    GridHeight = 20  # Number of rows in the game grid
    BorderWidth = 4  # Width of the border around the grid
    screenWidth = (
        BlockSize * GridWidth + BorderWidth * 2 + 200
    )  # Total width of the screen (grid + border + extra space for score)
    screenHeight = BlockSize * GridHeight + BorderWidth  # Total height of the screen


class Tetris:
    # def __init__(self):
    # Initialise Pygame, set up the screen, clock, etc.
    # Initialise the game grid, current piece, score, etc.
    # So "self" refers to the instance of the class that is being created. So when we create a new Tetris game, we can access these attributes and methods using "self".
    #
    # Note variables refer to instances where instances are the actual objects created from the class.

    def newPiece(self):
        # Create a new tetronimo piece
        key = random.choice(list(self.Shapes.keys()))
        shape = self.Shapes[key]
        color = self.Colors[key]
        return shape, color


if __name__ == "__main__":
    piece = Tetromino()
    print("Shape:", piece.Shapes[2])
