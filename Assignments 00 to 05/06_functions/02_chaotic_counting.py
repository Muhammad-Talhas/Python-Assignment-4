import random

# Constant to define the probability of stopping
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping

def chaotic_counting():
    """Counts from 1 to 10 or stops based on random chance."""
    for i in range(10):
        curr_num = i + 1  # Count from 1 to 10
        if done():  # Check if we should stop early
            return  # Exit the function if done() returns True
        print(curr_num)  # Print the current number

def done():
    """Returns True with a probability defined by DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD  # Return True with a chance of DONE_LIKELIHOOD

def main():
    """Main function to start the counting process."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting
    print("I'm done")

# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()
