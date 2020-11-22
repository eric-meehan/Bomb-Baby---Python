"""
Eric Meehan
2020-11-22

Bomb Baby
"""

from Node import Node
import sys

def main():
    # The user may specify a goal position through command line arguments
    if len(sys.argv) > 1:
        # Get X from the first argument
        Position = [int(sys.argv[1])]
        # Get Y from the second argument
        Position.append(int(sys.argv[2]))
    # Alternatively, the default goal of [4, 7] will be used
    else:
        Position = [4, 7]
    # Create two instances of Node
    Source = Node([1, 1])
    Goal = Node(Position)
    # Assume it is possible to reach the goal
    Possible = True
    while Goal != Source:
        Goal.ConditionedSubtraction()
        if Goal < Source:
            Possible = False
            break
    if Possible:
        print(Goal.Operations)
    else:
        print("Impossible")

main()
