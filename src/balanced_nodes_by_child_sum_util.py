class Node:
    def __init__(self, weight, right=None, left=None):
        self._weight = weight
        self._right = right
        self._left = left

    @property
    def weight(self):
        return self._weight

    @property
    def right(self):
        return self._right

    @property
    def left(self):
        return self._left

    def process(self):
        return True
