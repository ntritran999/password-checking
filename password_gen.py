import random

def password_generator():
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345679!@#$%^&*()"
    password = []

    for i in range(16): # You can use whathever range you like.
        rand = random.choice(charset)
        password.append(rand)
    return "".join(password)
