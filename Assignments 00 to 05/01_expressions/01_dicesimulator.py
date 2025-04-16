"""
Program: dice_simulator_v3
---------------------------
Simulate rolling two dice three times and display the results.
This version demonstrates variable scope in a unique way.
"""

# Importing the random library to generate random values for dice rolls
import random

# Constant to define the number of sides on the dice
NUM_SIDES = 6

def roll_two_dice():
    """
    Simulates rolling two dice and returns the total value.
    """
    return random.randint(1, NUM_SIDES) + random.randint(1, NUM_SIDES)

def main_program():
    die_value = 10  # Local variable 'die_value' initialized to 10
    print(f"Value of die_value in main_program() before rolls: {die_value}")
    
    # Roll the dice three times and display the results
    for i in range(3):
        roll_result = roll_two_dice()
        print(f"Roll {i + 1} result: {roll_result}")
    
    print(f"Value of die_value in main_program() after rolls: {die_value}")

# Standard Python entry point to start the program
if __name__ == '__main__':
    main_program()
