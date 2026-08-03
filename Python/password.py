import random
length = int(input("Enter length: "))
password = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", k=length)
print(f"Generated Password:{''.join(password)}")
