# src/tests/test_balanced_nodes_by_child_sum_util.py

from src.balanced_nodes_by_child_sum_util import Node


def test_can_create_node_with_weight():
    node = Node(1)
    assert node.weight == 1


def test_process_returns_true():
    assert Node(1).process() == True


def test_can_create_node_with_children():
    tree = Node(3, Node(2), Node(1))
    assert tree.weight == 3
    assert tree.right.weight == 2
    assert tree.left.weight == 1
