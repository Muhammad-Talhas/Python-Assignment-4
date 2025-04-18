import msvcrt          # For capturing keyboard input character-by-character 
from collections import Counter  # To count occurrences of numbers easily
import sys             # For writing to the terminal

# ANSI escape codes for coloring text in terminal (Windows 10+ supports this)
BLUE = '\033[94m'      # Bright blue text
RESET = '\033[0m'      # Reset to default terminal color

def colored_input(prompt=""):
    """
    Custom input function for Windows that displays typed characters in blue.
    Works by reading one character at a time from the keyboard.
    """
    sys.stdout.write(prompt)  # Print the prompt normally
    sys.stdout.flush()

    input_str = ''  # To store the full input string from the user
    while True:
        ch = msvcrt.getwch()  # Read one character from the user (Unicode safe)
        
        if ch in ('\r', '\n'):  # Enter key pressed
            print()  # Move to the next line
            break
        elif ch == '\x08':  # Backspace key
            if input_str:
                input_str = input_str[:-1]  # Remove last character
                # Erase character visually in terminal
                sys.stdout.write('\b \b')  
                sys.stdout.flush()
        else:
            input_str += ch  # Add character to the input string
            # Display the character in blue as the user types
            sys.stdout.write(f"{BLUE}{ch}{RESET}")
            sys.stdout.flush()

    return input_str  # Return the full input once Enter is pressed

def get_user_numbers():
    """
    Continuously prompts the user for numbers.
    Stops when the user enters a blank line.
    Returns a list of integers.
    """
    user_numbers = []

    while True:
        # Use our custom input function to get colored input
        user_input = colored_input("Enter a number (or press Enter to finish): ")
        
        if user_input.strip() == "":  # Blank line = stop input
            break
        try:
            user_numbers.append(int(user_input))  # Convert to integer and store
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input

    return user_numbers

def count_nums(num_list):
    """
    Takes a list of numbers and returns a dictionary with counts.
    Uses Counter for easy and efficient counting.
    """
    return Counter(num_list)

def print_counts(counts):
    """
    Prints the count of each number in a human-readable format.
    """
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Main function: collects user input, counts occurrences, and displays the result.
    """
    numbers = get_user_numbers()     # Get numbers from user
    counts = count_nums(numbers)     # Count how many times each number appears
    print_counts(counts)             # Print the results

# Run the program
if __name__ == '__main__':
    main()
