def main():
    # Ask the user to input a number (using ANSI codes for bold italics directly in the string)
    number = input(f"Type a number to see its square: \033[1m\033[3m") 
    
    # Convert input to float for decimals
    number = float(number)

    # Calculate the square of the number
    square = number * number

    # Reset formatting and print the result
    print(f"\033[0m{number} squared is {square}")  

# Call the main function to execute the program
if __name__ == '__main__':
    main()
