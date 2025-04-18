MAX_TERM_VALUE: int = 10000

def generate_fibonacci_up_to(limit):
    """
    Generates and prints Fibonacci numbers up to a given limit.

    Parameters:
        limit (int): The maximum value a Fibonacci number can have.
    """
    curr, next_ = 0, 1  # Initialize first two Fibonacci numbers

    while curr <= limit:
        print(curr)
        curr, next_ = next_, curr + next_

def main():
    """Entry point of the program."""
    generate_fibonacci_up_to(MAX_TERM_VALUE)

if __name__ == '__main__':
    main()

