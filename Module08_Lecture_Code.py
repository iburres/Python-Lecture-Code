# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:25:38 2022

Module 8 - Lecture Code

@author: iburr
"""



'''
#searching for a value in the string
char = input("What letter would you like to search for? ")

if char in letters:
    print(f"the letter {char} was found in the string")

else:
    print("The letter was not found in the string")
    

#accessing a specific index value in the string
element = letters[5] #value
index = letters.index(char)  #numbe associated with the value
print(f'The element {element} is located at index {index}')

#concatenating strings
numbers = '123456'

combined = numbers + letters
print(f"{numbers} {letters}")

#slicing strings
first_half = letters[0:13] 
second_half = letters[13:]
print(first_half, second_half)


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters2 = 'abcDefghijklmnoPqrstuVxyz'
#the FIND method
phrase = "Red ballons"
lower = phrase.lower()
print(lower)
position = phrase.find(lower)

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
newPhrase = phrase.replace("ballons", "apples")
print(newPhrase)

#converting the letters above into all lower case letters
result = letters.lower()
print(result)

result2 = letters.upper()
print(result2)
'''
#string testing methods
import random 

random.randint()

def isSpecial(passPhrase):
    
    special_characters = ["!", "@", "$", "#", "%"]
    for elem in passPhrase:
        if elem in special_characters:
            return True
        else:
            continue
                
        
        
    
    
def menu():
    user_choice = input("Please enter a passphrase: ")
    #user_choice = isSpecial(phrase)
    if user_choice.isalnum():
        print("The string is alphanumeric")
        
    if user_choice.isdigit():
        print("The string contains only numbers")
        
    if user_choice.isalpha():
        print("The string contains only letters")
        
    if user_choice.islower():
        print("the string contains only lowercase letters")
        
    if user_choice.isupper():
        
        print("The string has all upper case letters")
    
    if isSpecial(user_choice):
        print("The string also contains a special character")
        
if __name__ == "__main__":
    menu()
    
#LOOK AT THE BOTTOM OF PAGE 454.  WRITE THAT PROGRAM AND EXPLAIN TO ME WHAT IT'S DOING

#Programming Exercise in-class
#Use the instructions in Program 8-12 to calculate the average of each score using the StudentGradeBook.txt file I uploaded to Lab 2 on Blackoard
