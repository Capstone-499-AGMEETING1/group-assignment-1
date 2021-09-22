from main import calculate_mean, calculate_median


def test_calculate_mean():
    assert calculate_mean([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
    assert calculate_mean([10, 36, 2, 3, 78]) == 25.8


def test_calculate_median():
    assert calculate_median([1, 2, 3, 4, 5]) == 3
    assert calculate_median({4, 2, 7, 2, 6, 2}) == 3