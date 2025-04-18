from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    This function checks if the provided password matches the stored hashed password for a specific email.
    
    email: str - The email address of the user trying to log in.
    stored_logins: dict - A dictionary where the keys are email addresses and the values are the hashed passwords.
    password_to_check: str - The password the user is attempting to log in with.
    
    Returns: 
    bool - True if the hashed version of the provided password matches the stored hash, False otherwise.
    """
    # Hash the input password using the hash_password function
    hashed_password = hash_password(password_to_check)
    
    # Compare the stored hash (from stored_logins) with the hashed password
    # Using `.get(email)` to safely access the email's hash (returns None if email is not found)
    return stored_logins.get(email) == hashed_password

def hash_password(password):
    """
    This function hashes the provided password using the SHA256 algorithm.
    
    password: str - The password to be hashed.
    
    Returns: 
    str - The SHA256 hash of the input password.
    """
    # Use sha256 from hashlib to encode the password into a hash and return its hexadecimal string form
    return sha256(password.encode()).hexdigest()

def main():
    """
    This function serves as the main program flow. It defines a dictionary of stored logins
    (with hashed passwords) and tests the login function with different email and password combinations.
    """
    # A dictionary that stores emails as keys and their corresponding hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    # List of test cases, each case includes: email, password, and expected result
    test_cases = [
        ("example@gmail.com", "word", False),  # Invalid password for this email
        ("example@gmail.com", "password", True),  # Correct password for this email
        ("code_in_placer@cip.org", "Karel", False),  # Incorrect password (case-sensitive)
        ("code_in_placer@cip.org", "karel", True),  # Correct password (lowercase 'k')
        ("student@stanford.edu", "password", False),  # Invalid password
        ("student@stanford.edu", "123!456?789", True)  # Correct password
    ]
    
    # Loop through each test case and perform the login check
    for email, password, expected in test_cases:
        result = login(email, stored_logins, password)  # Call login function
        # Print the result of the login attempt along with the expected result for verification
        print(f"Login attempt for {email} with password '{password}': {result} (Expected: {expected})")

# This line ensures the main function runs only if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    main()
