def sum_even_odd_ai(numbers):
    """
    Returns the sum of even and odd numbers from the given list.

    Parameters:
        numbers (list): List of integers.

    Returns:
        tuple: (sum_of_even, sum_of_odd)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum


# --- User Input Section ---
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_sum, odd_sum = sum_even_odd_ai(numbers)
print("AI-Generated Docstring Function Result:")
print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)