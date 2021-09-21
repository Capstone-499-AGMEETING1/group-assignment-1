from main import calculate_mean


def test_calculate_mean():
    assert calculate_mean([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
    assert calculate_mean([10, 36, 2, 3, 78]) == 25.8
