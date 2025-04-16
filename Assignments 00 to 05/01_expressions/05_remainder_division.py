def main():
    # Ask the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate the quotient of the division
    quotient = num1 // num2
    
    # Calculate the remainder of the division
    remainder = num1 % num2

    # Display the result in the requested format
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Call the main function to run the program
main()
