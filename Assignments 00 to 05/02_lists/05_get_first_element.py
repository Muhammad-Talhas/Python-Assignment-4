def print_first_item(items):
    """Prints the first item from the list if it exists."""
    if items:
        print(f"\nFirst item: {items[0]}")
    else:
        print("\nThe list is empty. No first item to display.")

def collect_items():
    """Prompts the user to enter items one at a time, returning the completed list."""
    items = []
    print("Enter items for the list (press Enter to finish):")
    while True:
        entry = input("> ")
        if not entry:
            break
        items.append(entry)
    return items

def main():
    user_items = collect_items()
    print_first_item(user_items)

if __name__ == "__main__":
    main()
