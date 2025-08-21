import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password contains at least one character from each set
    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining length of the password with random choices from all sets
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Welcome to the Secure Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        number_of_passwords = int(input("Enter the number of passwords to generate: "))
        
        print("\nGenerated Passwords:")
        for _ in range(number_of_passwords):
            print(generate_password(length))
    except ValueError:
        print("Invalid input. Please enter numeric values for length and number of passwords.")

if _name_ == "_main_":
    main()
