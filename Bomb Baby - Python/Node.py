"""
Eric Meehan
2020-11-22

Bomb Baby - Node Class
"""

class Node():
    def __init__(position):
        # Initializes the Node class to have the
        self.Position = position
        # The dividend of the two numbers in Position is stored to eliminate redundant operations later
        self.CalculateDividend()
        # Also store the number of operations
        self.Operations = 0
        
    def __ne__(self, other):
        # Tests if the position of two nodes are not equivalent
        return self.Position[0] != other.Position[0] or self.Position[1] != other.Position[1]
        
    def __lt__(self, other):
        # Tests if either vertex of self is less than the respective vertex in other
        return self.Position[0] < other.Position[0] or self.Position[1] < other.Position[1]
        
    def CalculateDividend(self):
        # Calculates the dividend between the two vertices of Position
        # Note that integer division is required to handle large numbers
        self.Dividend = int(max(self.Position) // min(self.Position))
        # In order to function properly in ConditionedSubtraction, there must be a remainder after this operation
        if max(self.Position) % min(self.Position) == 0:
            self.Dividend -= 1
        
    def ConditionedSubtraction(self):
        # Alters the Position of the Node by subtracting the smaller number from the larger until their positions flip
        max(self.Position) -= min(self.Position) * self.Dividend
        # Calculate the new dividend
        self.CalculateDividend()
        # Increment Operations
        self.Operations += self.Dividend
