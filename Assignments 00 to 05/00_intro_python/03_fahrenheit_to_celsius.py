def main():

    # Prompt the user for the temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: \033[1m\033[3m"))
    
    # Convert the Fahrenheit temperature to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Output the result
    print(f"\033[0mTemperature: {fahrenheit}F = {celsius}C")

# Call the main function to run the program
if __name__ == "__main__":
    main()
