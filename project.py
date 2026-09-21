import names
from cacao_password_generator.core import generate
from random_username.generate import generate_username

name = names.get_full_name()
username = generate_username(1)
password = generate(length=20)

while True:

    print("DO YOU WANT TO GENERATE AN IDENTITY? (Y/N)")

    choice = input("Y/N: ")

    if choice == "Y" or choice == "y":
        print("Name: " + name)
        print("Password: " + password)
        print("Username: " + username[0])
        break

    elif choice == "N" or choice == "n":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter Y or N.")