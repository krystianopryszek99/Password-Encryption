from cryptography.fernet import Fernet

# Password Generator Program

def addPwd():
    name = input("Enter Your Name: ")
    pwd = input("Enter Your Password: ")

    with open('passwords.txt', 'a') as f:
        # Encrpts the password into bytes
        f.write(name + ", " + fer.encrypt(pwd.encode()).decode() + "\n")

def viewPwd():
    with open('passwords.txt', 'r') as f:#
        print("List of Names and Passwords")
        # Get all of the lines
        for line in f.readlines():
            # rstrip removes trailing spaces
            data = line.rstrip()
            user, password = data.split(",")
            print("Name: ", user, ", Password:", fer.decrypt(password.encode()).decode() + "\n")

def get_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key

key = get_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

print("__________________________________________________________\nPython password generator\n__________________________________________________________")

while True:
    userChoice = input("\nPlease choose 1 to add ,2 to view a password or 3 to exit:\n ")
    # choose option 
    if userChoice == "1":
        addPwd()
    elif userChoice == "2":
        viewPwd()
    elif userChoice == "3":
        # print exit message to screen and exit the application 
        print("\nExiting the program!") 
        break
    else:
        # when user enters invalid option, this will be printed to screen
        print("\nNot valid! Try again! Pick option 1,2 or 3") 
        continue