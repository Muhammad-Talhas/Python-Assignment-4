# Import the math library so we can use the sqrt function
import math

# Define the main function
def main ():
    # Ask the user for the lengths of the sides
    ab : float = float(input("Enter the length of the Perpendicular side AB: "))
    ac : float = float(input("Enter the length of the Base side AC: "))

    # Calculate the length of the hypotenuse
    hypotenuse : float = float(math.sqrt(ab**2 + ac**2))

    # Display the result
    print(f"The length of the hypotenuse BC is: {hypotenuse}")

# Call the main function to run the program
main()