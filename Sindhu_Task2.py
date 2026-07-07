import random
import string

def generate_password():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            
            if length < 8:
                print("Error: Password length must be at least 8 characters.\n")
                continue
            
            print("\nChoose character types to include:")
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            
            selected_types = sum([use_upper, use_lower, use_digits, use_symbols])
            
            if selected_types < 2:
                print("Error: Please select at least 2 character types.\n")
                continue
            
            char_pool = ""
            if use_upper:
                char_pool += string.ascii_uppercase
            if use_lower:
                char_pool += string.ascii_lowercase
            if use_digits:
                char_pool += string.digits
            if use_symbols:
                char_pool += string.punctuation
            
            password = "".join(random.choice(char_pool) for _ in range(length))
            
            print(f"\nGenerated Password: {password}\n")
            
            again = input("Generate another password? (y/n): ").lower()
            if again != 'y':
                break
            print()
            
        except ValueError:
            print("Error: Please enter a valid number for length.\n")

if __name__ == "__main__":
    print("=== Random Password Generator ===\n")
    generate_password()