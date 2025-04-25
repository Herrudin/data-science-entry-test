def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"

# Task 2: Invoke the function with the given scenarios
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Output: -1
print(find_first_negative([2, 10, 7, 0]))         # Output: "No negatives"
