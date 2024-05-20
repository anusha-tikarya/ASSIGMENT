print("Task5:")
print("Its time to make your account more secure")
print("Lets create a password for your account")
while True:
    password = input("Enter password: ")
    if len(password) < 8:
        print("Invalid Password! Must have at least 8 characters long")
    elif not any (character.isupper() for character in password):
        print("Invalid Password! Must have at least one uppercase letter")
    elif not any (character.isdigit() for character in password):
        print("Invalid Password! Must have at least one digit!")
    else:
        print("Yay, your password is valid!")
        break
