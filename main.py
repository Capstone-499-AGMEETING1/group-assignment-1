from collections import Counter


# Function to return the mean of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


# Function to return the median of a list of numbers.
def calculate_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        median = numbers[round(len(numbers) / 2)]
    else:
        median = ((numbers[int((len(numbers) / 2) - 1)] + numbers[int(len(numbers) / 2)]) / 2)
    return median


# Function to return the mode of a list of numbers.
def calculate_mode(numbers):
    c = Counter(numbers)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
