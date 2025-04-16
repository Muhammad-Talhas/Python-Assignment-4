def duplicate_message(target_list, message_to_add):
    target_list += [message_to_add] * 3  # Adds three copies at once using list multiplication

# ----------- Main Program Starts Here -----------

def run():
    user_input = input("Enter a message to copy: \033[1m\033[3m")
    messages = []
    
    print("\033[0mList before:", messages)
    duplicate_message(messages, user_input)
    print("List after:", messages)

if __name__ == "__main__":
    run()
