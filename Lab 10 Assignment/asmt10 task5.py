def divide_numbers(a, b):
    """
    Divide two numbers safely with error handling.

    Parameters
    ----------
    a : float or int
        The numerator.
    b : float or int
        The denominator.

    Returns
    -------
    float or str
        The result of division, or an error message if division fails.

    Notes
    -----
    This function uses a try-except block to catch ZeroDivisionError
    and return a user-friendly message instead of crashing the program.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


print(divide_numbers(10, 0))