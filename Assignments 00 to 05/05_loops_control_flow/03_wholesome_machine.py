AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def prompt_user_for_affirmation():
    """Prompts the user to type the affirmation and returns their input."""
    print("Please type the following affirmation:")
    print(AFFIRMATION)
    return input()

def check_affirmation():
    """
    Continuously prompts the user until they type the correct affirmation.
    """
    user_input = prompt_user_for_affirmation()

    while user_input != AFFIRMATION:
        print("\nThat was not the affirmation. Let's try again.\n")
        user_input = prompt_user_for_affirmation()

    print("\nThat's right! :)")

def main():
    check_affirmation()

if __name__ == '__main__':
    main()


