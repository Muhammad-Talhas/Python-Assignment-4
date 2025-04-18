def read_phone_numbers():
    """
    Prompts the user to enter name-number pairs to store in a phonebook dictionary.
    Returns:
        dict: A dictionary with names as keys and numbers as values.
    """
    phonebook = {}

    while True:
        name = input("Name: ").strip()
        if not name:
            break
        number = input("Number: ").strip()
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints all name-number pairs in the phonebook.
    """
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows the user to look up phone numbers by name.
    """
    print("\nPhonebook Lookup (press Enter to stop):")
    while True:
        name = input("Enter name to lookup: ").strip()
        if not name:
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

def main():
    """
    Main program flow: read phonebook entries, display them, and allow lookups.
    """
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
