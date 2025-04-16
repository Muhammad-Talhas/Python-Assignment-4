import sys

def print_entire_list(items):
    """Prints the entire list."""
    if items:
        print("\nThe entire list:", items)
    else:
        print("\nThe list is empty. Nothing to display.")

def collect_items():
    """Prompts the user to enter items one at a time, returning the completed list."""
    items = []
    print("Enter items for the list (press Enter to finish):")

    # Set the color to blue for the prompt and user input
    sys.stdout.write("\033[34m")  # ANSI escape code for blue text

    while True:
        entry = input("> ")  # The user will see this in blue
        if not entry:  # If the user presses Enter without input, stop
            break
        items.append(entry)
    
    # Reset to the default color after input
    sys.stdout.write("\033[39m")  # ANSI escape code for resetting to default color

    return items

def main():
    user_items = collect_items()
    print_entire_list(user_items)

if __name__ == "__main__":
    main()
