import random
import string
def generate_password():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be at least 1.")
        elif length > 100: 
            print("Please keep password under 100 characters.")
        else:
            password = ''.join(random.choices(all_chars, k=length))
            print(f"Generated Password: {password}")
            
    except ValueError:
        print("Error: Please enter a valid whole number for the length.")

if __name__ == "__main__":
    generate_password()
  