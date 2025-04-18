def count_even(lst):
    """
    Returns the number of even numbers in the list.
    
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  # Variable to store the count of even numbers

    # Loop through each number in the list
    for num in lst:
        if num % 2 == 0:  # Check if the number is even (divisible by 2)
            count += 1  # Increment the count of even numbers

    return count  # Return the final count of even numbers

def get_list_of_ints():
    """
    Reads integers from user input until the user presses enter without entering any number,
    and returns the list of entered integers.
    """
    lst = []  # Create an empty list to store the integers
    
    # Continuously ask for input until the user presses Enter with no input
    while True:
        user_input = input("Enter an integer or press enter to stop: ").strip()  # Get user input
        
        if user_input == "":  # If input is empty (just Enter was pressed)
            break  # Exit the loop if no input is entered
        
        try:
            # Try to convert the input into an integer and add it to the list
            lst.append(int(user_input))
        except ValueError:
            # If the input is not a valid integer, notify the user and prompt again
            print("That's not a valid integer. Please try again.")
    
    return lst  # Return the list of integers entered by the user

def main():
    """
    Main function to drive the program:
    - Collects a list of integers from the user.
    - Counts and displays the number of even numbers in the list.
    """
    lst = get_list_of_ints()  # Get the list of integers from the user
    even_count = count_even(lst)  # Count the even numbers in the list
    print(f"Number of even numbers: {even_count}")  # Output the result

# Run the program if the file is executed directly
if __name__ == '__main__':
    main()
