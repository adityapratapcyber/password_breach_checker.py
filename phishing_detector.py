common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin123",
    "welcome",
    "letmein"
]

password = input("Enter Password: ")

if password in common_passwords:
    print("Warning!")
    print("This password is commonly used and may be unsafe.")
else:
    print("Good News!")
    print("Password not found in the common password list.")
