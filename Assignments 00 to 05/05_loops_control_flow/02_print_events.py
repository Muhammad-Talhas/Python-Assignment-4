def print_even_numbers(count):
    """
    Prints the first `count` even numbers starting from 0.

    Parameters:
        count (int): The number of even numbers to print.
    """
    for i in range(count):
        print(i * 2)

def main():
    TOTAL_NUMBERS = 20  # Total even numbers to print
    print_even_numbers(TOTAL_NUMBERS)

if __name__ == "__main__":
    main()
