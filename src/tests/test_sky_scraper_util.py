# src/tests/test_sky_scraper_util.py

from src.skyscraper_util import process_skyscrapers_heights, number_is_unique


def test_number_is_unique_return_true():
    heights = [4, 9, 1]
    assert number_is_unique(4, heights) == True


def test_number_is_unique_return_false():
    heights = [4, 9, 4]
    assert number_is_unique(4, heights) is False


def test_max_skyscraper_is_kept():
    skyScrapersHeights = [4, 9]

    assert process_skyscrapers_heights(skyScrapersHeights) == [4, 9]
