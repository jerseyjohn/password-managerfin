# John DeHuff
# 05/03/2023
# Password Manager

import random
import string


# Main function
def main():
    try:
        with open('passwords.txt', 'r') as infile:
            password_list = infile.readlines()
            infile.close()
            # Create a blank dictionary
            passwords = {}
            for line in password_list:
                website, password = line.strip('\n').split(', ')
                passwords[website] = password
    # If the passwords.txt file is not found, it will create a blank dictionary and continue running.
    except FileNotFoundError:
        passwords = {}
    # This creates the menu
    while True:
        print("")
        print("         ~Password Manager by John DeHuff~          ")
        print("<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>")
        print("<<>> 1. View passwords                          <<>>")
        print("<<>> 2. Lookup existing password                <<>>")
        print("<<>> 3. Add a new password                      <<>>")
        print("<<>> 4. Update an existing password             <<>>")
        print("<<>> 5. Delete an existing password             <<>>")
        print("<<>> 6. Exit program                            <<>>")
        print("<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>")
        # Get the users choice
        choice = input("Enter your choice: ")

        # View passwords menu choice
        if choice == '1':
            if not passwords:
                print("You do not have any passwords stored")
            else:
                for website, password in passwords.items():
                    print(f"{website}: {password}")
        # Lookup passwords menu choice
        elif choice == '2':
            website = input("Enter the website to find the password for: ")
            lookupPW(passwords, website)
        # Add password menu choice
        elif choice == '3':
            website = input("Enter the website to add a password for: ")
            addPW(passwords, website)
        # Add Password menu choice
        elif choice == '4':
            website = input("Enter the website to update the password for: ")
            updatePW(passwords, website)
        # Delete password menu choice
        elif choice == '5':
            website = input("Enter the website to delete the password for: ")
            deletePW(passwords, website)
        # Exit menu choice
        elif choice == '6':
            with open('passwords.txt', 'w') as file:
                for website, password in passwords.items():
                    # Upon exiting the program, it writes the website and password to the passwords.txt file
                    file.write(f"{website}, {password}\n")
                print("Thank you for using my application!")
            break
        # Easter egg
        elif choice.lower() == 'secret' or 'credits':
            with open('passwords.txt', 'w') as file:
                for website, password in passwords.items():
                    file.write(f"{website}, {password}\n")
            secret()
            break


# This function generates a random password
def generatePW():
    # This variable defines the characters to use in the randomly generated password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ask the user how long they want the password to be
    length = int(input("Enter the desired password length (minimum 10): "))
    # if the user inputs a password length lower than 10, it defaults to 10
    if length < 10:
        print("Invalid input, defaulted to a password length of 10")
        length = 10
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# This function lets you search for a website in the passwords dictionary and displays the password
def lookupPW(passwords, website):
    if website in passwords:
        print(f"The password for {website} is {passwords[website]}")
    else:
        print(f"No password is stored for {website}")


# This function lets you add an account and password to the list
def addPW(passwords, website):
    if website not in passwords:
        password = generatePW()
        passwords[website] = password
        print(f"Password for {website} added")
    else:
        update = input(f"A password for {website} already exists, would you like to update it? (y/n) ")
        if update.lower() == 'y':
            updatePW(passwords, website)


# This lets you update a password that is stored in the list
def updatePW(passwords, website):
    if website in passwords:
        password = generatePW()
        passwords[website] = password
        print(f"Password for {website} updated.")
    else:
        print(f"No password is stored for {website}.")


# This format lets you delete an entry
def deletePW(passwords, website):
    if website in passwords:
        delconfirm = input(f"Are you sure you want to delete the password for {website}? (y/n) ")
        # if the user inputs Y or y, it deletes the password from the dictionary
        if delconfirm.lower() == 'y':
            del passwords[website]
            print(f"Password for {website} deleted.")
    elif website not in passwords:
        print(f"No password is stored for {website}.")


# I was bored so I added this easter egg
def secret():
    # Changes the color of the text in a print statement
    class TextColors:
        RED = '\033[31m'  # Red
        ENDC = '\033[m'  # Ends a color
        BLUE = '\033[34m'  # Blue
    pwmgr = '''
             ░██▓███  ▄▄▄       ██████  ██████ █     █░▒█████  ██▀███ ▓█████▄     ███▄ ▄███▓▄▄▄      ███▄    █ ▄▄▄       ▄████▓█████ ██▀███
             ▓██░  ██▒████▄   ▒██    ▒▒██    ▒▓█░ █ ░█▒██▒  ██▓██ ▒ ██▒██▀ ██▌   ▓██▒▀█▀ ██▒████▄    ██ ▀█   █▒████▄    ██▒ ▀█▓█   ▀▓██ ▒ ██▒
             ▓██░ ██▓▒██  ▀█▄ ░ ▓██▄  ░ ▓██▄  ▒█░ █ ░█▒██░  ██▓██ ░▄█ ░██   █▌   ▓██    ▓██▒██  ▀█▄ ▓██  ▀█ ██▒██  ▀█▄ ▒██░▄▄▄▒███  ▓██ ░▄█ ▒
             ▒██▄█▓▒ ░██▄▄▄▄██  ▒   ██▒ ▒   ██░█░ █ ░█▒██   ██▒██▀▀█▄ ░▓█▄   ▌   ▒██    ▒██░██▄▄▄▄██▓██▒  ▐▌██░██▄▄▄▄██░▓█  ██▒▓█  ▄▒██▀▀█▄
             ▒██▒ ░  ░▓█   ▓██▒██████▒▒██████▒░░██▒██▓░ ████▓▒░██▓ ▒██░▒████▓    ▒██▒   ░██▒▓█   ▓██▒██░   ▓██░▓█   ▓██░▒▓███▀░▒████░██▓ ▒██▒
             ▒▓▒░ ░  ░▒▒   ▓▒█▒ ▒▓▒ ▒ ▒ ▒▓▒ ▒ ░ ▓░▒ ▒ ░ ▒░▒░▒░░ ▒▓ ░▒▓░▒▒▓  ▒    ░ ▒░   ░  ░▒▒   ▓▒█░ ▒░   ▒ ▒ ▒▒   ▓▒█░░▒   ▒░░ ▒░ ░ ▒▓ ░▒▓░
             ░▒ ░      ▒   ▒▒ ░ ░▒  ░ ░ ░▒  ░ ░ ▒ ░ ░   ░ ▒ ▒░  ░▒ ░ ▒░░ ▒  ▒    ░  ░      ░ ▒   ▒▒ ░ ░░   ░ ▒░ ▒   ▒▒ ░ ░   ░ ░ ░  ░ ░▒ ░ ▒░
             ░░        ░   ▒  ░  ░  ░ ░  ░  ░   ░   ░ ░ ░ ░ ▒   ░░   ░ ░ ░  ░    ░      ░    ░   ▒     ░   ░ ░  ░   ▒  ░ ░   ░   ░    ░░   ░
                           ░  ░     ░       ░     ░       ░ ░    ░       ░              ░        ░  ░        ░      ░  ░     ░   ░  ░  ░'''
    jdeh = '''
              ▄▄▄██▀▀▒█████  ██░ ██ ███▄    █    ▓█████▄▓█████ ██░ ██ █░   ██  █████▒█████▒
                ▒██ ▒██▒  ██▓██░ ██▒██ ▀█   █    ▒██▀ ██▓█   ▀▓██░ ██▒██  ▓██▓██   ▓██   ▒
                ░██ ▒██░  ██▒██▀▀██▓██  ▀█ ██▒   ░██   █▒███  ▒██▀▀██▓██  ▒██▒████ ▒████ ░
             ▓██▄██▓▒██   ██░▓█ ░██▓██▒  ▐▌██▒   ░▓█▄   ▒▓█  ▄░▓█ ░██▓▓█  ░██░▓█▒  ░▓█▒  ░
              ▓███▒ ░ ████▓▒░▓█▒░██▒██░   ▓██░   ░▒████▓░▒████░▓█▒░██▒▒█████▓░▒█░  ░▒█░
              ▒▓▒▒░ ░ ▒░▒░▒░ ▒ ░░▒░░ ▒░   ▒ ▒     ▒▒▓  ▒░░ ▒░ ░▒ ░░▒░░▒▓▒ ▒ ▒ ▒ ░   ▒ ░
              ▒ ░▒░   ░ ▒ ▒░ ▒ ░▒░ ░ ░░   ░ ▒░    ░ ▒  ▒ ░ ░  ░▒ ░▒░ ░░▒░ ░ ░ ░     ░
              ░ ░ ░ ░ ░ ░ ▒  ░  ░░ ░  ░   ░ ░     ░ ░  ░   ░   ░  ░░ ░░░░ ░ ░ ░ ░   ░ ░
              ░   ░     ░ ░  ░  ░  ░        ░       ░      ░  ░░  ░  ░  ░  '''

    print(TextColors.RED + pwmgr + TextColors.ENDC)  # Prints ascii art "Password Manager" in red
    print(TextColors.BLUE + jdeh + TextColors.ENDC)  # Prints ascii art "John DeHuff" in blue


# Call the main function
if __name__ == '__main__':
    main()
