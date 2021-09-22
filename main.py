# Function to return the mean of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        median = numbers[round(len(numbers) / 2)]
    else:
        median = ((numbers[int((len(numbers) / 2)-1)] + numbers[int(len(numbers)/2)]) / 2)
    return median