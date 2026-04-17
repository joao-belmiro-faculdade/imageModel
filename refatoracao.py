def compute_statistics(values):
    """Calculate total, average, maximum, and minimum for a list of numbers."""
    if not values:
        raise ValueError("The list of values must not be empty.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return total, average, maximum, minimum


if __name__ == "__main__":
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = compute_statistics(numbers)

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")