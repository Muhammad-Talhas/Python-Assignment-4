import random

NUM_SIDES = 6

def roll_die(sides=NUM_SIDES):
    """Simulate rolling one die with the given number of sides."""
    return random.randint(1, sides)

def main():
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()
