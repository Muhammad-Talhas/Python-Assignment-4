from typing import List

def add_many_numbers(numbers: List[int]) -> int:
    """Returns the sum of a list of numbers using Python's built-in sum() function."""
    return sum(numbers)

# Main execution block
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]  # List of numbers
    print(add_many_numbers(numbers))  # Print the sum of the numbers
