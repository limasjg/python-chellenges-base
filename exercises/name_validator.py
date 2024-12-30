username = input("Enter with your user name: ")

if len(username) > 12:
    print("Your username can't be greater than 12 characters")
elif not username.find(" ") == -1:
    print("You can't use spaces.")
elif not username.isalpha():
    print("You can't use number.")
else:
    print(f"Welcome {username}")
