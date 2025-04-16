
def main():
    print("This program adds two numbers.")

    # Prompt the user to enter the first number
    num1 = input("Enter the first number: ")
    
    # Convert the input to an integer
    num1 = int(num1)
    
    # Prompt the user to enter the second number
    num2 = input("Enter the second number: ")
    
    # Convert the input to an integer
    num2 = int(num2)
    
    # Calculate the sum of the two numbers
    total_sum = num1 + num2
    
    # Print the total sum with an appropriate message
    print(f"The sum of {num1} and {num2} is {total_sum}")

# Call the main function to execute the program
main()
