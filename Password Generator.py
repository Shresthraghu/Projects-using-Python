import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits     
    if use_specials:
        characters += string.punctuation  

    if not characters:
        return "Error: No characters available to generate password."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    length = int(input("Enter desired password length: "))
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    specials = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, digits, specials)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number for password length.")
