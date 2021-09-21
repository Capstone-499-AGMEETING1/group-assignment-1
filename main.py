# Function to return the mean of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Test that the calculate_mean() function works as expected.
    print("Calculate Mean Tests:")
    print(calculate_mean([1, 2, 3, 4, 5, 6, 7, 8]))
    print(calculate_mean([10, 36, 2, 3, 78]))
