import random
def makeMove(sticks):
    a = sticks % 4
    if a == 0:
        return random.randint(1, 3)
    return a