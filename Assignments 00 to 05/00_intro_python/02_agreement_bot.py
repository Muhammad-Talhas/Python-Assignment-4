def main():

    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? \033[1m\033[3m")
    
    # Respond with a message that includes the user's input in bold and italics
    print(f"\033[0mMy favorite animal is also {favorite_animal}!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
