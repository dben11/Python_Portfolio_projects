import random
import string

while True:
    try:
        
        password_length =  int(input("Enter the desired password length: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")

#define the characters to use in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password_list = []
for i in range(password_length):
    random_character = random.choice(all_characters)
    password_list.append(random_character)


# Convert the list of characters into a single string
generated_password = "".join(password_list)

# Print the final password
print(f"Generated Password Was successful: {generated_password}")






