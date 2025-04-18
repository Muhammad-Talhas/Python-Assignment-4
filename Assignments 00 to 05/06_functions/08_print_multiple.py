def print_multiple(message, repeats):
    """
    Prints the message a specified number of times.
    """
    for _ in range(repeats):  
        print(message)

def main():
    message = input("Please type a message: \033[34m")  
    print("\033[0m")  
    repeats = int(input("Enter a number of times to repeat your message: \033[34m"))
    print("\033[0m")
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
