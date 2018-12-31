class Node:

    def __init__(self, position, parent = None):
        self.position = position
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0
