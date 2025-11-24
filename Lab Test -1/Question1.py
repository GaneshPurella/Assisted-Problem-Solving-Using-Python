def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
        n (int): Non-negative integer whose factorial is required.

    Returns:
        int: Factorial of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Type check
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    # Factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # 0! is defined as 1
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except (TypeError, ValueError) as e:
        print("Error:", e)
