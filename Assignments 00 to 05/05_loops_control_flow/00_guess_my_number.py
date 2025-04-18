import random

def get_user_guess():
    """Prompt the user to enter a guess and return it as an integer."""
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def give_feedback(guess, secret_number):
    """Print feedback based on the user's guess."""
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"🎉 Congrats! You guessed it! The number was: {secret_number}")

def play_guessing_game():
    """Main logic for the number guessing game with a single guess."""
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...\n")

    guess = get_user_guess()
    give_feedback(guess, secret_number)

def main():
    play_guessing_game()

if __name__ == '__main__':
    main()
