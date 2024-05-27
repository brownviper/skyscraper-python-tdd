class Node:
    def __init__(self, weight, right=None, left=None):
        self._weight = weight
        self._right = right
        self._left = left

        right_weight = self.right.calculate_children_weight() if self.right else 0
        left_weight = self.left.calculate_children_weight() if self.left else 0

        self._balanced = self.right is not None and self.left is not None and right_weight == left_weight

    @property
    def weight(self):
        return self._weight

    @property
    def right(self):
        return self._right

    @property
    def left(self):
        return self._left

    @property
    def balanced(self):
        return self._balanced

    def calculate_children_weight(self):
        right_weight = self.right.calculate_children_weight() if self.right else 0
        left_weight = self.left.calculate_children_weight() if self.left else 0

        res = sum([self.weight, right_weight, left_weight])

        return res

    def calculate_balanced_nodes(self, balanced_nodes):
        balanced_nodes = balanced_nodes + 1 if self.balanced else balanced_nodes

        if self.right:
            balanced_nodes = self.right.calculate_balanced_nodes(balanced_nodes)

        if self.left:
            balanced_nodes = self.left.calculate_balanced_nodes(balanced_nodes)

        return balanced_nodes

