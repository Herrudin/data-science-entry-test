def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Invalid input: both arguments must be numeric"

    if divisor == 0:
        return "Error: division by zero"

    return num % divisor == 0

# Task 2: Invoke the function with the given scenarios
print(check_divisibility(10, 2))  # Output: True
print(check_divisibility(7, 3))   # Output: False
