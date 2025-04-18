MINIMUM_HEIGHT: int = 50  # Minimum required height to ride

def check_height(height):
    """Check if the user's height meets the minimum requirement."""
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    try:
        user_height = float(input("How tall are you? \033[1m\033[3m"))
        print("\033[0m", end="")
        check_height(user_height)
    except ValueError:
        print("\033[0m", end="")
        print("Please enter a valid number for height.")

# No need to edit below this line
if __name__ == '__main__':
    main()
