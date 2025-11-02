def is_prime(n):
    # Handle special cases
    if n < 2:
        return False
    
    # Check for divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    # Test cases
    test_numbers = [1, 2, 3, 4, 5, 7, 11, 12, 23, 97]
    for num in test_numbers:
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
