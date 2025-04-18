def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')

def is_odd(value: int):
    return value % 2 != 0  # Returns True if value is odd, False if even

if __name__ == '__main__':
    main()
