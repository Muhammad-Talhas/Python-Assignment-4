# Constant for speed of light (in meters per second)
C = 299792458  # m/s

# Define the main function
def main():
    # Ask user for mass input
    mass = float(input("Enter kilos of mass: "))  # Convert input to a float
    
    # Calculate energy using E = m * C^2
    energy = mass * C**2
    
    # Print out the results
    print(f"\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!\n")

# Call the main function to run the program
main()
