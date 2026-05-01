def compute_statistics(values):
    """Calcula estatísticas de uma lista de números.

    Args:
        values: Lista de números.

    Returns:
        Tupla com (total, média, máximo, mínimo).

    Raises:
        ValueError: Se a lista estiver vazia.
    """
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