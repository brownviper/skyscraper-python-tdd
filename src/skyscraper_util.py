def get_max_skyscraper_height(skyscraper_heights):
    max_skyscraper_height = 0
    max_skyscraper_height_index = 0
    index = 0
    for skyscraper_height in skyscraper_heights:
        if skyscraper_height >= max_skyscraper_height:
            max_skyscraper_height = skyscraper_height
            max_skyscraper_height_index = index
        index = index + 1

    return max_skyscraper_height, max_skyscraper_height_index


def process_skyscrapers_heights(skyscraper_heights):
    results = []

    for height in skyscraper_heights:
        if number_is_unique(height, results):
            results.append(height)

    return results


def number_is_unique(number, skyscraper_heights):
    idx = len(list(filter(lambda x: x == number, skyscraper_heights)))

    return idx == 0
