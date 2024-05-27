# src/tests/test_balanced_nodes_by_child_sum_util.py

from src.balanced_nodes_by_child_sum_util import Node


def test_can_create_node_with_weight():
    node = Node(1)
    assert node.weight == 1


def test_can_create_node_with_children():
    tree = Node(3, Node(2), Node(1))
    assert tree.weight == 3
    assert tree.right.weight == 2
    assert tree.left.weight == 1


def test_can_construct_a_tree():
    rr = Node(0)
    lr = Node(3)
    ll = Node(-1)

    r = Node(4, rr)
    l = Node(2, lr, ll)

    root = Node(9, r, l)


def test_calculate_weight_returns_two_for_one_node_and_2_children():
    r = Node(3)
    l = Node(-1)
    node = Node(2, r, l)
    res = node.calculate_children_weight()

    assert node.calculate_children_weight() == 4


def test_calculate_weight_returns_17_for_multi_level_binary_tree():
    rr = Node(0)
    lr = Node(3)
    ll = Node(-1)

    r = Node(4, rr)
    l = Node(2, lr, ll)

    root = Node(9, r, l)

    assert root.calculate_children_weight() == 17


def test_calculate_balanced_nodes_returns_one():
    rr = Node(0)
    lr = Node(3)
    ll = Node(-1)

    r = Node(4, rr)
    l = Node(2, lr, ll)

    root = Node(9, r, l)

    balanced_nodes = 0

    assert root.calculate_balanced_nodes(balanced_nodes) == 1


def test_calculate_balanced_nodes_returns_three_for_multi_level_tree():
    lrrl = Node(3)

    lrr = Node(-3, None, lrrl)
    llr = Node(0)
    lll = Node(0)

    lr = Node(3, lrr, None)
    ll = Node(3, llr, lll)

    r = Node(10)
    l = Node(4, lr, ll)

    root = Node(7, r, l)

    balanced_nodes = 0

    assert root.calculate_balanced_nodes(balanced_nodes) == 3


def test_calculate_balanced_nodes_returns_zero_if_node_has_only_one_child():
    l = Node(10)
    root = Node(9, None, l)

    balanced_nodes = 0

    assert root.calculate_balanced_nodes(balanced_nodes) == 0


def test_calculate_balanced_nodes_returns_one_if_node_has_only_one_child():
    r = Node(10)
    l = Node(10)
    root = Node(9, r, l)

    balanced_nodes = 0

    assert root.calculate_balanced_nodes(balanced_nodes) == 1
