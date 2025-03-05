'''

Module 4:  Repetition Structures and Random Number Generation
Author: Ian Burres
Date: 9/20/2021

'''
import random
#import statistics
import math
import os   #operating system
#import pandas as pd


'''
Random Number Generation

'''
rand_number = random.randint(0, 100) #generates a random number between 0 and 100
print(rand_number)
result = pow(2, 3)


'''

Repetition Structures, For loops and While loops

'''
#for-loop  (count-controlled)
#can be programmed controlled or user controlled
#Example of programmer controlled:
#for num in range(0, 11):
#    squared = num * num
#    print(squared)
#start = int(input("What number should i start at: "))
#end = int(input("What number should we exit the loop: "))
#increment/decrement = int(input("What number should we increment or decrement by:  "))
#for i in range(start, end , 2):
#    print(i)

# Example 1:
choice = input("Do you want to play a game? ")
   

if choice.lower() == "yes":
    user_choice = int(input("How many times should my loop run? "))
    
    # user-controlled for loop
    #user_choice = 7
    for i in range(0, user_choice + 1, 1):  #(start, end, increment/decrement)
        print(f"Welcome to my game. This is loop number: {i}")

for i in range(1, 3):
    #do something here 11 times
    #placeholder for code to be added later
    pass

n = int(input("Enter a number: "))
while n < 20:
    print(n)
    n += 1 # n = n + 1
# while loop (condition-controlled T/F)

while(choice.lower() == "yes"):
    print("Welcome to my game.")
    
    users_number = int(input("Guess a number from 1 - 100:  "))
    if(users_number != rand_number):
        print("That is not the same number")
        
    else:
        print(f"That is the same number {rand_number}")
        #choice = input("Do you want to play again? ")
        break
    choice = input("Do you want to play again? ") 
       # break
#    loop -= 1
    # 40 lines of code
shots_made = 0
for shots in range(1, 101):
    _3_pointers = random.randint(0, 100)
    if _3_pointers >= 0 and _3_pointers <=30:
        shots_made += 1

print(shots_made)
    
while shots_made <= 100:
    _3_pointers = random.randint(0, 100)
    if _3_pointers >= 0 and _3_pointers <=30:
        shots_made += 1
        
print(shots_made)
         

#print("Goodbye")
#number_made = random.randint(0,101)
#if(number_made == 100):
#    pass

my_boolean = True



while True:
    choice = input("Do you want to play a game? ")
    if(choice.lower() == "no"):
        print("Goodbye again")
        break
        #my_boolean = False
    else:
        continue

my_list = [-2, 4, 0, 8, 1]

#bubble sort     
my_list.sort()
#Nested Loops.  A loop within a loop.  When i is 0 the inner loop will run 9 times.  When i is 1 the inner loop will run 9 times.  When i is 2 the inner loop will run 9 times.  When i is 3 the inner loop will run 9 times.  4 * 9 = 36.  Total number of iterations.
for i in range(0, 100): #outer loop. 
    print(f"The value of i is: {i}")
    for j in range(1, 100): #inner loop.  
        print(f"The value of j is: {j} \n")
        for k in range(10, 200):
            print(k)
            
for outer in range(0, 4):
    print(f"outer value: {outer}")
    for inner in range(0, 4):
        print(f"inner value: {inner}")
        for inner_inner in range(0, 4):
            print(f"inner_inner value: {inner_inner}")
            
            
        


print("\n-------------------")
for num in [1,2,3,4]:
    print(num)

movie_title = "The Last of the Mohicans"

for letter in movie_title:
    print(letter)

length = len(movie_title)
print(length)




#Sentinel Values
patients_weight = int(input("Enter the first patients weight: "))
num_of_patients = 1
total = 0
while (patients_weight != 0): 
    total = total + patients_weight
    print(f"The average of the patients' weight is: {total / num_of_patients}")
    num_of_patients += 1
    patients_weight = int(input("Please enter the weight of the next patient or 0 for no more patients: "))
    
#using loops for input validation



hours_worked = int(input("Enter the number of hours worked: "))
hourly_pay = int(input("Enter your hourly pay rate: "))

counter = 0
while(hours_worked < 0 or hourly_pay < 0):
    print("ERROR: You cannot work negative hours or be paid negative dollars.")
    hours_worked = int(input("Enter the number of hours worked"))
    hourly_pay = int(input("Enter your hourly pay rate: "))
    counter += 1
    
    if counter > 1:
        print("You aren't very good at following directions.")
        continue
        
income_total = hours_worked * hourly_pay
print(f"Your gross pay for the week is: ${income_total:,} US Dollars")

#Using the walrus operator to place it on one line

'''
while (score := int(input("Enter you score from 0 - 100: "))) < 0:
    print("A score cannot be negative.")

if(score >= 70):
    print("You passed!")
else:
    print("You failed!")    
    
#nested Loops

'''
'''
for i in range(0, 4):
    print(f"The value of i is: {i}")
    for j in range(1, 10):
        print(f"The value of j is: {j} \n")
        for k in range(10, 20):
            print(k)
'''
     
holiday = "Christmas"
length = len(holiday)
counter = 0
for char in holiday:
    print(char)
    counter += 1
    print(counter)
    
print(f"the length of the Christmas is: {counter}")
print(length)
    
    

'''






'''   
# Enter number of terms needed                   #0,1,1,2,3,5....
a = int(input("Enter the terms"))
f = 0                                         #first element of series
s = 1                                         #second element of series
if a <= 0:
    print("The requested series is",f)
else:
    print(f, s, end = " ")
    for x in range(2,a):
        next = f + s                           
        print(next, end = " ")
        f = s
        s = next
