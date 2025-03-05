# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:25:38 2022

Module 8 - Lecture Code

@author: iburr
"""

#I love programming 99. That's a 1 number 0


#searching for a value in the string
letters = "owjefoiaAIFoefooewfj"
char = input("What letter would you like to search for? ")


if char in letters:
    print(f"the letter {char} was found in the string")

else:
    print("The letter was not found in the string")
    

#accessing a specific index value in the string
while True:
    
    try:
    #element = letters[5] #value
        index = letters.index(char)  #number associated with the value
        print(f'The element {char} is located at index {index}')
        break
    except:
        print("That letter is not in the string and would have caused a Traceback error.")
        char = input("What letter would you like to search for? ")
    

#concatenating strings
numbers = '123456'

combined = numbers + letters
print(f"{numbers}{letters}")

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#slicing strings
first_half = letters[0:13] 
second_half = letters[13:27]
print(first_half, second_half)


#letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters2 = 'abcDefghijklmnoPqrstuVxyz'
#the FIND method
phrase = "Red balloons" 
lower = phrase.lower()
print(lower)


position = phrase.find("tim")

if position != -1:
    
    print(f"The word was contained at position {position}")

else:
    print("The word was not found")
    
#determining the type of file by using the endswith substring
filename = input("")

# loop through all files in a directory
if filename.endswith('.txt'):
    print("The file you are looking for is a text file")

else:
    print("The file is not a text file")
    
#replacing values
newPhrase = phrase.replace("balloons", "apples")
print(newPhrase)

#converting the letters above into all lower case letters
result = letters.lower()
print(result)

result2 = letters.upper()
print(result2)

#string testing methods
#import random 

#random.randint()

def isSpecial(passPhrase):
    
    special_characters = ["!", "@", "$", "#", "%"]
    for elem in passPhrase:
        if elem in special_characters:
            return True
        else:
            continue
                    
    
def menu():
    passPhrase = input("Please enter a passphrase: ")
    length = len(passPhrase)
    if length >= 8:
        print("The password has the correct length")
    if passPhrase.isalnum(): 
        print("The string is alphanumeric")
        
    if passPhrase.isdigit(): 
        print("The string contains only numbers")
        
    if passPhrase.isalpha(): 
        print("The string contains only letters")
        
    if passPhrase.islower(): 
        print("the string contains only lowercase letters")
        
    if passPhrase.isupper():
        print("The string has all upper case letters")
    
    if (isSpecial(passPhrase)):
        print("The string also contains a special character and is alphanumeric")
        
if __name__ == "__main__":
    menu()
    
#LOOK AT THE BOTTOM OF PAGE 454.  WRITE THAT PROGRAM AND EXPLAIN TO ME WHAT IT'S DOING

#Programming Exercise in-class
#Use the instructions in Program 8-12 to calculate the average of each score using the StudentGradeBook.txt file I uploaded to Lab 2 on Blackoard
