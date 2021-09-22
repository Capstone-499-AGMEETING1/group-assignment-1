# Function to return the mean of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    numbers.sorted()
    if len(numbers) % 2 != 0:
        median = numbers[round(len(numbers) / 2)]
    else:
        median = ((len(numbers) / 2) + (len(numbers) / 2 + 1)) / 2
    return median
