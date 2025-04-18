ADULT_AGE: int = 18  

def is_adult(age: int) -> bool:
    """Returns True if age is 18 or older, False otherwise."""
    return age >= ADULT_AGE

def main():
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Please enter a valid integer age.")

if __name__ == "__main__":
    main()
