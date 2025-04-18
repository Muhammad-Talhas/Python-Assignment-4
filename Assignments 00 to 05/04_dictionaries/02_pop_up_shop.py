def main():
    """
    Prompts the user for the quantity of each fruit they want to buy,
    then calculates and prints the total cost.
    """
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0.0

    for fruit, price in fruits.items():
        try:
            amount = int(input(f"How many ({fruit}) do you want?: ").strip())
            if amount < 0:
                print("Please enter a non-negative number.")
                continue
            total_cost += price * amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"\nYour total is ${total_cost:.2f}")


if __name__ == '__main__':
    main()
