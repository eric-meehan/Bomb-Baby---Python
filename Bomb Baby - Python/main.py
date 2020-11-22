"""
Eric Meehan
2020-11-22

Bomb Baby
"""

from Node import Node

def main():
    # Create two instances of Node
    Source = Node([1, 1])
    Goal = Node([4, 7])
    # Assume it is possible to reach the goal
    Possible = True
    while Goal != Source:
        Goal.ConditionedSubtraction()
        if Goal < Source:
            Possible = False
            break
    print(Goal.Operations)

main()
