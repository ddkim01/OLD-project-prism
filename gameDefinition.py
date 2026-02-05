# `""" Remember: "class" is like blueprint and instances are the things you build
# with the blueprint """

# import pygame
# # Create blueprint for the grid

# class TetrisGrid:
#     def __init__(self) -> None:  # Define grid dimensions as attributes
#         self.num_rows = 20
#         self.num_cols = 10
#         self.cell_size = 40

#         self.grid = [
#             [0 for x in range(self.num_rows)] for y in range(self.num_cols)
#         ]  # flake is cringe with E501
#         # draw lines to draw the grid
#         self.surface = pygame.surface((30,40))
#         self.color = pygame.color(200,200,200)
#         self.start_pos =
#     """
#     Drawing a grid requires a surface to draw on and a
#     """

#     def draw_grid(self):  # This is a method (actions this object can perform)Draw and display the grid
#         for row in range(self.num_rows):
#             for col in range(self.num_cols):
#                 print(self.grid[row][col], end=" ")
#                 pygame.draw.line()
#             # print()

"""Using this video for building this game: https://www.youtube.com/watch?v=gIjVwODrXC8"""

"""Deine the constants for the grid dimensions and cell size"""
# Define colors for each tetromino type
black = (0, 0, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
magenta = (255, 0, 255)
gray = (128, 128, 128)  # colour for the border

# Define game dimensions
blockSize = 30  # Size of each block in pixels
gridWidth = 10  # Number of columns in the game grid
gridheight = 20  # Number of rows in the game grid
borderWidth = 4  # Width of the border around the grid
screenWidth = (
    blockSize * gridWidth + borderWidth * 2 + 200
)  # Total width of the screen (grid + border + extra space for score)
screenHeight = blockSize * gridheight + borderWidth  # Total height of the screen


# Define the tetromino shapes - 1 is a filled block, 0 is an empty block.
# First sublist is the first layer of the shape.
shapes = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[1, 0, 0], [1, 1, 1]],  # J shape
    [[0, 0, 1], [1, 1, 1]],  # L shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]],  # Z shape
]


