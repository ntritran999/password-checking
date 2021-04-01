from password_gen import password_generator

while True:
    user_password = input("Enter a password: ")
    if len(user_password)<6:
        print("\n")
        print("Password must contain at least 6 digits!")
        print("Your password can be like this:", password_generator())
    elif len(user_password)>=6 and (user_password.isalpha() or user_password.isnumeric()):
        print("\n")
        print("Password must contain both words and numbers!")
        print("Your password can be like this:", password_generator())
    else:
        print("\n")
        print("This is your password:", user_password)
        break
