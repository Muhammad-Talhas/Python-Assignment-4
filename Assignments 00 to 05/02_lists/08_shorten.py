MAX_LENGTH = 3

def shorten(lst):
    """Shorten the list to MAX_LENGTH by removing elements from the end and printing each removed element."""
    if len(lst) > MAX_LENGTH:
        removed_items = lst[MAX_LENGTH:]  # Get items to remove
        lst[:] = lst[:MAX_LENGTH]  # Keep only the first MAX_LENGTH items
        for item in removed_items:
            print(item)  # Print removed items

def get_input_list():
    """Prompt the user for list elements and return the list."""
    lst = []
    print("Please enter items for the list (press Enter without input to stop):")
    while True:
        elem = input("> ")
        if not elem:
            break  # Exit the loop if input is empty
        lst.append(elem)
    return lst

def main():
    """Main function to get the list from the user and shorten it."""
    lst = get_input_list()
    shorten(lst)  # Shorten and print the list

if __name__ == "__main__":
    main()
