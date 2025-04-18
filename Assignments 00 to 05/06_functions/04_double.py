def double(num: int):
    return num * 2

def get_valid_number():
    user_input = input("Enter a number: ")
    while not user_input.isdigit():
        print("Invalid input! Please enter a valid integer.")
        user_input = input("Enter a number: ")

    return int(user_input)

def main():
    num = get_valid_number()
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
