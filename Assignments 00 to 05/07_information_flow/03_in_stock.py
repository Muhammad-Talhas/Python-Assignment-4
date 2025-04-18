def main():
    fruit = input("Enter a fruit: \033[1;3m")
    print("\033[0m")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit: str) -> int:
    """
    Returns the number of a specific fruit in stock.
    """
    stock_inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }

    return stock_inventory.get(fruit, 0)  # Default to 0 if fruit not found

if __name__ == '__main__':
    main()
