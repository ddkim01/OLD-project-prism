"""Remember: "class" is like blueprint and instances are the things you build 
with the blueprint"""

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
