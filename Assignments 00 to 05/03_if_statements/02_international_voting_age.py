# Voting ages in fictional countries
VOTING_AGES = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

def check_voting_eligibility(age):
    """Prints voting eligibility for each fictional country based on user's age."""
    for country, voting_age in VOTING_AGES.items():
        if age >= voting_age:
            print(f"You can vote in {country} where the voting age is {voting_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {voting_age}.")

def main():
    try:
        # Use ANSI escape codes to make user input appear in blue
        user_age = int(input("How old are you? \033[34m"))  # Blue input starts here
        print("\033[0m", end="")  # Reset color after input
        check_voting_eligibility(user_age)
    except ValueError:
        print("\033[0m", end="")  # Reset in case of error
        print("Please enter a valid number for age.")

if __name__ == '__main__':
    main()
