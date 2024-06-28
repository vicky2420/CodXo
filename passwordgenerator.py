import random
import string

# Generate a random password of specified length with given character sets
def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choices(characters, k=length))
    return password

 # Save the generated password to a file
def save_password(password):
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    print("Password saved to 'passwords.txt'.")

 # Check the strength of the generated password
def check_password_strength(password):
    strength = {
        'length': len(password) >= 12,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special': any(c in string.punctuation for c in password)
    }
    return strength

# Generate multiple passwords
def generate_multiple_passwords(count, length, use_upper, use_lower, use_digits, use_special):
    passwords = [generate_password(length, use_upper, use_lower, use_digits, use_special) for _ in range(count)]
    return passwords

 # Display password strength details
def display_password_strength(strength):
    print("\nPassword Strength:")
    for criterion, met in strength.items():
        print(f"{criterion.capitalize()}: {'Met' if met else 'Not met'}")

# Get user input for password generation settings
def get_user_input():
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate (at least 6 characters):"))
            if length < 6:
                print("Password length should be at least 6 characters!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer length")
    
    use_upper = input("Include uppercase letters? (yes/no):").strip().lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no):").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no):").strip().lower() == 'yes'
    
    if not (use_upper or use_lower or use_digits or use_special):
        print("At least one character set must be selected. Defaulting to all sets")
        use_upper, use_lower, use_digits, use_special = True, True, True, True
    
    return length, use_upper, use_lower, use_digits, use_special

# Main function to handle user interaction
def main():
    print("Welcome to the Password Generator!")
    
    length, use_upper, use_lower, use_digits, use_special = get_user_input()

    print("\nGenerated Password:")
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(password)
    
    # Check password strength
    strength = check_password_strength(password)
    display_password_strength(strength)

    while True:
        save = input("\nDo you want to save this password? (yes/no):").strip().lower()
        if save == 'yes':
            save_password(password)
            break
        elif save == 'no':
            break
        else:
            print("Invalid input!. Please enter 'yes' or 'no'")

    while True:
        try:
            generate_more = input("\nDo you want to generate more passwords? (yes/no):").strip().lower()
            if generate_more == 'yes':
                count = int(input("Enter the number of passwords to generate:"))
                passwords = generate_multiple_passwords(count, length, use_upper, use_lower, use_digits, use_special)
                print("\nGenerated Passwords:")
                for i, pwd in enumerate(passwords, 1):
                    print(f"{i}. {pwd}")
                break
            elif generate_more == 'no':
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'")
        except ValueError:
            print("Invalid input! Please enter a valid integer for the number of passwords")

if __name__ == "__main__":
    main()
