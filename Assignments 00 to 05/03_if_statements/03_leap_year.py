def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Leap year check:
    if year % 4 != 0:
        print("That's not a leap year.")
    elif year % 100 != 0:
        print("That's a leap year!")
    elif year % 400 == 0:
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
