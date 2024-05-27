# src/tests/test_largest_possible_squares_util.py

from src.largest_possible_squares_util import process


def test_process_returns_one_when_single_stick_is_provided():
    sticks = [5]
    assert process(sticks) == 1


def test_process_returns_one_when_two_sticks_are_provided():
    sticks = [1, 4]
    assert process(sticks) == 1


def test_process_returns_five_to_account_for_the_four_sides_needed_to_create_a_square():
    sticks = [13, 11]
    assert process(sticks) == 5


def test_process_returns_seven():
    sticks = [10, 21]
    assert process(sticks) == 7


def test_returns_zero_when_not_possible_to_create_a_square():
    sticks = [2, 1]
    assert process(sticks) == 0


def test_returns_two_when_only_one_stick_can_be_used_to_create_a_square():
    sticks = [1, 8]
    assert process(sticks) == 2
