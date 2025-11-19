# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:20:35 2022

Module 9 - Dictionaries

@author: iburr
"""
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
              '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


#we will use this import to write dictionaries to files
import json
'''

#Here is the gradebook expressed concisely as a dictionary

#We use a list to pair each grade with the key (which is each student's name)

grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82], 'Jake': {'Sub-grades': [0, 1, 2]}, 10: 'Mustang'}
simple_dictionary = {'JK Rowling': ["Harry Potter and the Sorcers Stone", "Chamber of Secrets"], "J.R.R. Tolkein": "Lord of the Rings"}

#FINDING A VALUE IN A DICTIONARY 
student_name = input("Enter the students name to see their respective grades: ")

if student_name in grade_book:
    
    #print(grade_book[key])
    print(*grade_book[student_name]) # The ord character * will remove the brackets from the list. 

#works like ELSE, but actually searches through the dictionary    
if student_name not in grade_book:
    print("The student does not exist in the grade book.")
    
#CHANGING A VALUE IN GRADEBOOK
#Since we have mutliple values, we still need to find the index of the list 
#associated with each student
if student_name in grade_book:
    
    grade_change = int(input("Which grade do you want to change? "))
    grade_change = grade_change - 1
    new_value = int(input("Enter the new grade: "))
    
    for key in grade_book:
        #remember, it follows key:value pairs, so we reference the key then the value as grade_change
       
        #grade_book['Tina'][1]
        grade_book[student_name][grade_change] = new_value
    
    print(grade_book)
    
mylist = [1,2,3]
mystring = str(mylist)
print(mystring)

#WRITING THE GRADE_BOOK TO A TEXT FILE USING JSON, FOR LOOPS, AND STRING CONVERSION

with open(r'NewGradeBooks.txt', 'w') as file:
    
    #USING A FOR LOOP TO ITERATE OVER THE DICTIONARY
    for key, value in grade_book.items():
        
        file.write('%s:%s\n' % (key, value))        
        
    file.write(json.dumps(grade_book))
    
    #without json and dumps
    #file.write(str(grade_book))
      
file.close()


#----------------------------------------------------------------------------------------------------

phonebook = {'Karl': '555-9832', 'Tim': '754-3220', 'Nelly': '954-8774'}
print(phonebook)

#ADDING AN ELEMENT TO THE DICTIONARY
#dictionary[key]
phonebook['Karl'] = '954-8998'
phonebook['Terrence'] = '305-5565'
#notice how it replaced the value associated with Karl but adds Terrence 
print(phonebook)

#DELETING A KEY:VALUE PAIR
del phonebook['Terrence']
print(phonebook)

#GETTING THE NUMBER OF ITEMS IN A DICTIONARY USING LEN
length = len(phonebook)
print(length)

#CREATING AN EMPTY DICTIONARY
empty_dictionary = {}

empty_dictionary['Car'] = 'Ford Mustang'
print(empty_dictionary)

#USING A FOR LOOP TO ITERATE OVER THE DICTIONARY

for key in phonebook:
    
    print(key, phonebook[key])


#USING THE CLEAR() METHOD
phonebook.clear()
print(phonebook)

#USING THE GET() METHOD.  This takes the key and a default statement if it's not found
number1 = phonebook.get('Karl', 'number not found')
print(number1)

phonebook = {'Johnny': '999-9999'}
number2 = phonebook.get('Johnny')
print(number2)

#PRINTING OUT ALL OF THE ITEM IN A DICTIONARY
print(phonebook.items())  
new_phonebook = {'John': '754-8765', 'Turqouise': '555-5555'} 

for name in new_phonebook.items():
    
    print(name, value)

print(new_phonebook.keys())

#USING THE POP METHOD, which, which removes a single key:value pair
new_phonebook.pop('Turqouise', 'Number not found')
print(new_phonebook)

#POPITEM METHOD.  IN 3.7 + of Python popitem() removes last item added to dict
grade_book.popitem()
print(grade_book)

#USING THE VALUES METHOD()
for val in grade_book.values():
    
    print(val)
    
#DICTIONARY COMPREHENSIONS

#in this line of code we will create a nnumber and its corresponding square using
#one line of code for the squares dictionary
numbers = [1,2,3,4]
#item:item**2 == result expression.  for item in numbers == iteration expression
squares = {item:item**2 for item in numbers}

print(squares)
'''
#LOOK AT PAGE 492, Using if Clauses

#-------------------------------------------------------------------------------

#SETS

mySet = set()
mySet = 'abc'
print(mySet)

myListSet = set([3, 2, 4, 4])
print(myListSet)

length = len(myListSet)
print(length)
myListSet.add('b')
myListSet.add('a')
myListSet.add('a')
myListSet.add(3.4)
myListSet.add(5.5)
length2 = len(myListSet)
print(myListSet)
print(length2)

myListSet.update([9, 6, 10, 'b'], [0, 10])
print(myListSet)


myListSet.remove(10)  #also .discard()
print(myListSet)
a_new_set = set('a')
print(f"----------This is an empty set: {a_new_set}-------------")
myListSet.clear() #removes everything

a_new_set.clear()

print(f"----------This is an empty set: {a_new_set}-------------")
#for loops, in operator, not in operator
#YOU WILL DO THIS

#Union of sets - the real reason to use them
set1 = set([1,5,19,8])
set2 = set([7,6,19,4,1,11])
set3 = set1.union(set2)
print(set3)  # can use the or operation | as well   set3 = set1 | set2

#intersection of sets
set4 = set1.intersection(set2)

print(set4) # like above but use the & operator,  set3 = set1 & set2

#difference of sets
set5 = set1.difference(set2)
print(set5)

set5a = set2.difference(set1)
print(set5a)

set6 = set2.symmetric_difference(set1)
print(set6)



