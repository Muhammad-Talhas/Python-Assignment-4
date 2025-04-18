def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Start from 1, and go up to num (inclusive)
        if num % i == 0:  # Check if i is a divisor of num
            print(i)

def main():
    user_input = input("Enter a number: \033[34m") 
    print("\033[0m")
    num = int(user_input)  # Convert the user input to an integer
    print_divisors(num)

if __name__ == '__main__':
    main()
