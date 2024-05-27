def number_exist_in_array(number, skyscraper_heights):
    idx = len(list(filter(lambda x: x == number, skyscraper_heights)))

    return idx > 0


def solution(heights):
    results = [heights[-1]]

    for height in reversed(heights[:-1]):
        if number_exist_in_array(height, results) is False:
            results.insert(0, height)
        else:
            tmp = height - 1
            while number_exist_in_array(tmp, results) is True:
                tmp = tmp-1
            results.insert(0, tmp)

    return results
