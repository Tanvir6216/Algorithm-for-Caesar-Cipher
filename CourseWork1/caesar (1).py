# Coursework Assessment 1
# Name: Shahrier Ahammed Tanvir
# Student No:2442655
# A Caesar Cipher Program

# Importing required libraries
import os.path

# Defining the alphabet
alphabets = 'abcdefghijklmnopqrstuvwxyz'

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    #return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    # add your code here
    mode = input("Would you like to encrypt (e) or decrypt (d)? : ")
    while True:
        if mode == 'e' or mode== 'd':
            break
        else:
            print("Invalid Mode ")
            mode = input("Would you like to encrypt (e) or decrypt (d)? : ")

    message = ''
    if mode == "e":
     message = input("What message would you like to encrypt: ")
    else:
        message= input("What message would you like to decrypt?: ")
    shift = 0
    try:
        shift= int(input("what is the shift number: "))
    except:
        shift= int(input("What is the shift number: "))
    return (mode, message.upper(), shift)


def encrypt(message,shift):
    # add your code here
    message = message.lower()
    cipher = ''
    for letter in message:
        if letter in alphabets:
            position = (alphabets.index(letter) + shift) % (len(alphabets))
            newLetter = alphabets[position]
            cipher += newLetter
        else:
            cipher += letter


    return  cipher.upper()

    # Main Program Logic
    if __name__ == "__main__":
        welcome()
        mode, message, shift = enter_message()

        if mode == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message:{result}")
        elif mode == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message:{result}")


def decrypt(message,shift):
    # add your code here
    message = message.lower()
    decipher = ""
    for letter in message:
        if letter in alphabets:
            position = (alphabets.index(letter) - shift) % (len(alphabets))
            newLetter = alphabets[position]
            decipher += newLetter
        else:
            decipher += letter



    return decipher.upper()



def process_file(filename, mode,shift):
    list_messages = []
    # add your code here
    file = open(filename,'r')#    #open the file
    data = file.readlines()# read data from file
    file.close()# close the file because we have read the data

    if mode == "e":
        for row in data:
            message = encrypt(row.strip('\n'), shift)# encrypting each row one by one
            #print(message)
            list_messages.append(message)
    else:
        for row in data:
            #print(row.strip('\n'))
            message = decrypt(row.strip('\n'), shift)# decrypting data
            list_messages.append(message)
    return list_messages # list_messages is either contains encrypted or decrypted data



def write_messages(lines):
    # add your code here
    file = open("results.txt" ,"w")
    for line in lines:
        file.write(line)
        file.write("\n")
    file.close()

    return

def is_file(filename):

    return os.path.isfile(filename)



import os

def is_file(filename):
    """Check if a file exists."""
    return os.path.isfile(filename)

def message_or_file():
    mode = ""
    filename = None
    message = None
    shift = 0

    # Input for encryption or decryption mode
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")

    # Input for source of message (file or console)
    choice = input("Would you like to read from a file (f) or the console (c)? ").lower()

    if choice == "f":
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("File does not exist. Please enter a valid filename.")
    elif choice == "c":
        if mode == "e":
            message = input("What message would you like to encrypt? ")
        else:
            message = input("What message would you like to decrypt? ")
    else:
        print("Invalid choice. Defaulting to console input.")
        if mode == "e":
            message = input("What message would you like to encrypt? ")
        else:
            message = input("What message would you like to decrypt? ")

    # Input for shift value with error handling
    while True:
        try:
            shift = int(input("What is the shift number? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift number.")

    return mode, message, filename, shift




def main():
    '''
    # add your code here
    lines = ["HELLO","HELLO WORLD", "WHAT!?","S O S","0 1 2 3 4 5 6 7 8 9","THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.","Goodbte."]
    welcome()
    mode, message, shift = enter_message()
    #print(mode, message, shift)
    if mode == "e":
        print(encrypt(message,shift))
    else:
        print(decrypt(message,shift))
    print(process_file("messages.txt", mode,shift))
    print(is_file("messages.txt"))
    write_messages(lines)
    '''

    welcome()
    Continue = 'y'
    while Continue == 'y':
        mode, message, filename, shift = message_or_file()
        if filename == None:
            if mode == "e":
                print(encrypt(message,shift))
            else:
                print(decrypt(message,shift))
        else:
            lines=process_file(filename, mode,shift)
            write_messages(lines)

        Continue = input("Would you like to encrypt or decrypt another message? (y/n): ")
    return 0




# Program execution begins here
if __name__ == '__main__':
    main()
    print("Thanks for using the program, goodbye! ")



