def calculate_average(scores):
    """Return the average of the score list."""
    return sum(scores) / len(scores)


def find_highest(scores):
    """Return the highest score."""
    return max(scores)


def find_lowest(scores):
    """Return the lowest score."""
    return min(scores)


def process_scores(scores):
    """Process scores using helper functions and display results."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("\nAverage:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# ----------- USER INPUT -----------
scores = list(map(int, input("Enter scores separated by space: ").split()))

process_scores(scores)