def main():
    # Create a dictionary to store the names and ages
    ages = {
        'Anton': 21,            # Anton's age is given as 21 years old
        'Beth': 21 + 6,         # Beth is 6 years older than Anton
        'Chen': 21 + 6 + 20,    # Chen is 20 years older than Beth
    }
    
    # Drew's age is the sum of Anton's and Chen's ages
    ages['Drew'] = ages['Anton'] + ages['Chen']
    
    # Ethan is the same age as Chen
    ages['Ethan'] = ages['Chen']
    
    # Print out all of the ages using a loop
    for name, age in ages.items():
        print(f"{name} is {age}")

# Call the main function to run the program
if __name__ == '__main__':
    main()
