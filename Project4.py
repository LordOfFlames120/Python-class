input_from_user="Password1"
password=input("Enter a password: ")
while input_from_user!=password:
    print("Wrong password")
    password=input("Enter a password: ")
print("The password is correct, welcome")