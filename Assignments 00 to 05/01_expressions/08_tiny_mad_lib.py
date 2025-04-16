# Constants for the sentence start
SENTENCE_START = "Coding is fun. I learned to program and used Python to make my"

def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Create the fun sentence by combining the inputs
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
    # Print the final sentence
    print(sentence)

# Call the main function to run the program
main()
