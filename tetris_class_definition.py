"""Remember: "class" is like blueprint and instances are the things you build 
with the blueprint"""

# https://github.com/tucna/Programming_Projects/blob/main/Python/tetris.py code base

# STEP 1: INSTALL AND IMPORT PYGAME
import pygame
import random

# Code needs to handle the player's INPUTS, UPDATES, and DRAWING assets.

# STEP 2: DEFINE THE GRIDS AND PIECES AND RULES
class Tetris:
    def __init__(self):
        # Initialise Pygame, set up the screen, clock, etc.
        # Initialise the game grid, current piece, score, etc.
        # So "self" refers to the instance of the class that is being created. So when we create a new Tetris game, we can access these attributes and methods using "self". 
        # 
        # Note variables refer to instances where instances are the actual objects created from the class. 

    def newPiece(self):
        # Create a new tetronimo piece

    def validMove(self, piece, x, y):
        # Check if the piece movement is valid

    def placePiece(self, piece):
        # PLace a piece on the grid
    
    def removeFullRows(self): 
        # Remove completed rows and update score
    
    def rotatePiece(self, piece):
        # Rotate a piece
    
    def draw(self):
        # Draw the game state
        self.screen.fill(Black)

        # Draw placed pieces
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(self.screen, color, (x * BlockSize + BorderWidth, y * BlockSize, BlockSize - 1, BlockSize -1))
        
        # Draw current piece
        for i, row in enumerate(self.)

    def run(self):
        # Main game loop
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    # Handle key presses

            self.handle_continuous_movement()
            # Update game state

            self.draw()

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

# Define game dimensions
BlockSize = 30  # Size of each block in pixels
GridWidth = 10  # Number of columns in the game grid
GridHeight = 20  # Number of rows in the game grid
BorderWidth = 4  # Width of the border around the grid
screenWidth = (
    BlockSize * GridWidth + BorderWidth * 2 + 200
)  # Total width of the screen (grid + border + extra space for score)
screenHeight = BlockSize * GridHeight + BorderWidth  # Total height of the screen

# Define the tetromino shapes - 1 is a filled block, 0 is an empty block.
# First sublist is the first layer of the shape.
Shapes = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[1, 0, 0], [1, 1, 1]],  # J shape
    [[0, 0, 1], [1, 1, 1]],  # L shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]],  # Z shape
]
