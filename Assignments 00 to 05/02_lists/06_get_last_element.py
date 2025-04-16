def print_last_item(items):
    """Prints the last item from the list if it exists."""
    if items:
        print(f"\nLast item: {items[-1]}")
    else:
        print("\nThe list is empty. No last item to display.")

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
    print_last_item(user_items)

if __name__ == "__main__":
    main()
