'''

caesar.py is a program that takes user input and encrypts the text using the caesar cipher encryption method using command line arguments.


Created on the 29th of July, 2022
Last edited: 14/09/22

'''

import re
import string
import sys

'''
This function converts user input into a usable variable
It does this by converting everything to uppercase, replacing full stops with the letter X,
and discarding any non-alphabetical characters including spaces
'''

def convert_to_Caesar(message):
    #make string uppercase
    capStr = (message.upper())
    #replace full stops with X
    dotToX = (capStr.replace(".", "X"))
    #discard spaces
    noSpaces = (dotToX.replace(" ", ""))
    #Remove all non-alphabetical characters
    cleanStr = re.sub(r"[^A-Z]+", "", noSpaces)
    #output the cleaned string
    print("Here is the message you are encrypting:",cleanStr)
    #make the clean string a global variable
    global cleanStr_Caesar
    cleanStr_Caesar = cleanStr
    
'''
This function takes the converted string from the previous function and the shift value.
It then ciphers the text using the caesar cipher.
'''

def encrypt_Caesar(shift, text):
    #define a variable for the alphabet in uppercase
    alphabet = string.ascii_uppercase
    #the alphabet is concatenated with itself to allow for looping
    alphabet = alphabet + alphabet.upper()    
    #shifted is the alphabet starting at the shift point and concatenated with the beginning up to the shift point
    shifted = alphabet[shift:] + alphabet[:shift]
    #table is defined as the str.maketrans function using the alphabet and the shifted alphabet
    table = str.maketrans(alphabet, shifted)
    #encrypted is defined as the text translated using the table
    encrypted = text.translate(table)
    #print the encrypted message
    print("Here is your encrypted message:")
    print(encrypted)
    

#check if there are no arguments provided
if len(sys.argv)==1:
    #print error
    print("nope")
    print("Usage: shift value, message to encrypt")
    #close the program
    exit()
else:
    #continue
    ...


#get the shift value and the message to clean and encrypt from command line
shiftValue = (sys.argv[1])

#If the first argument is not an integer: ignore the first argument and make the shift value 1
if shiftValue.isdigit():
    shiftValue = int(sys.argv[1])
else:
    print("Invalid shift value.\nDefaulting shift value to 1")
    shiftValue = int(1)

#get the list of arguments into a variable
wholeArg = sys.argv
#exclude the filename and shift value from the string
noShift = wholeArg[2:]
message = ' '.join(noShift)


#send command line string for conversion
convert_to_Caesar(message)



#Ask for a string to be cleaned
#convert_to_Caesar(input("Please enter a string to be cleaned for ciphering\n>>>  "))

'''
#Get the shift value and make sure the input is a number.
while True:
    try:
        shiftValue = int(input("Please enter the shift value.\n>> "))
        break
    except:
        print("Sorry, that input is invalid. Please enter a number.")
'''

#send the shift value as well as the cleaned string to the encryption function
encrypt_Caesar(shiftValue, cleanStr_Caesar)

