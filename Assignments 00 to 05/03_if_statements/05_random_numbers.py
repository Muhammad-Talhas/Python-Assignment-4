import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def generate_random_numbers(count, min_val, max_val):
    """Generates a list of random integers within the given range."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def display_numbers(numbers):
    """Prints the list of numbers."""
    print("Generated numbers:")
    for num in numbers:
        print(num)

def main():
    random_numbers = generate_random_numbers(N_NUMBERS, MIN_VALUE, MAX_VALUE)
    display_numbers(random_numbers)

if __name__ == '__main__':
    main()
