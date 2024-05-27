
class Node:
    def __init__(self, weight):
        self.weight = weight
        self.left_child = None
        self.right_child = None

    def left_child(self, child):
        self.left_child = child

    def right_child(self, child):
        self.right_child = child

    def process(self):
        return True