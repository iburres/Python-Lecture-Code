#import random

'''
Repetition Structures

'''
#choice = input("Do you want to play a game? ")
#loop = 11
#user_choice = int(input("How many times should my loop run? "))   
 
#a_ran_num = random.randint(1, 3)
#print(a_ran_num)
#while loop (condition-controlled T/F)
'''
while(choice.lower() == "yes"):
    print("Welcome to my game.")
    users_number = int(input("Guess a number from 1 - 10:  "))
    if(users_number != a_ran_num):
        print("That is not the same number")
        choice = input("Do you want to play again? ")
    else:
        print(f"That is the same number {a_ran_num}")
        break
#    loop -= 1
    # 40 lines of code
 '''   

#print("Goodbye")
#number_made = random.randint(0,101)
#if(number_made == 100):
#    pass
'''
while True:
    choice = input("Do you want to play a game? ")
    if(choice.lower() == "no"):
        print("Goodbye again")
        break
    else:
        continue
'''    
#for-loop  (count-controlled)

#programmer controlled
#start = int(input("What number should i start at: "))
#test = int(input("What number should we exit the loop: "))
#increment = int(input("What number should we increment by:  "))
#for i in range(0, 11 ):
#    print(i)

'''
print("\n-------------------")
for num in [1,2,3,4]:
    print(num)
'''

'''
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

while(hours_worked < 0 or hourly_pay < 0):
    print("ERROR: You cannot work negative hours or be paid negative dollars.")
    hours_worked = int(input("Enter the number of hours worked"))
    hourly_pay = int(input("Enter your hourly pay rate: "))
income_total = hours_worked * hourly_pay
print(f"Your gross pay for the week is: ${income_total:,} US Dollars")

#Using the walrus operator to place it on one line
'''
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
