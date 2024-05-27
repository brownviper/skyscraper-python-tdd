# src/tests/test_sky_scraper_util.py

from src.skyscraper_util import process_skyscrapers_heights, number_exist_in_array


def test_number_exist_in_array_returns_true():
    heights = [4, 9, 1]
    assert number_exist_in_array(4, heights) == True


def test_number_exist_in_array_returns_false():
    heights = [9, 4]
    assert number_exist_in_array(5, heights) == False


def test_skyscraper_are_processed_for_unique_heights():
    heights = [4, 9]

    assert process_skyscrapers_heights(heights) == [4, 9]


def test_heights_are_interpolated_for_duplicated_heights():
    heights = [4, 4, 9]

    assert process_skyscrapers_heights(heights) == [3, 4, 9]


def test_processing_is_starting_from_last_element():
    heights = [2, 5, 4, 5, 5]

    assert process_skyscrapers_heights(heights) == [1, 2, 3, 4, 5]
