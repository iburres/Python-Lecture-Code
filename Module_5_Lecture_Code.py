
'''
Module 5 Lecture Code

All about Functions

'''


#This function accepts a single argument in its parameter field and adds that number with a declared integer
def addition(a):
    
    #a = 4
    b = 5
    total = a + b
    
    return total    

def subtraction():
    
    a = 6
    b = 10
    total = a - b
    print(total)
    
def multiplication():
    a = 6
    b = 10
    total = a * b
    print(total)
    
def division():
    a = 10
    b = 6
    total = a // b
    print(total)
    
def compute(received_data):
    count = 0
    #received_data.strip(" ")
    #print(received_data)
    for char in received_data:
        if (not char.isspace()):
            count += 1
    length = len(received_data)
    print(length)
    return count

def sendMultipleBack(food, number):
    
    first = food
    second = number
    
    return first, second

def gui():
    
    operation = int(input("Enter 1. Addition  2. Subtraction  3. Multiplication  4. Division "))
    num_of_characters = 0
    if(operation == 1):
        num = int(input("Enter a number from 1 - 10: "))
        add_return = addition(num)
        print(add_return)
    if(operation == 2):
        subtraction()
    if(operation == 3):
        multiplication()
    if(operation == 4):
        division()
    if(operation == 5):
        fav_book = input("What is your favorite book? ")
        num_of_characters = compute(fav_book)
        print(f"The number of characters in the title of you book is: {num_of_characters}")
    if(operation == 6):
        result = sendMultipleBack("Orange", 13)
        print(result)
        print(*result)

if __name__ == "__main__":
    
    gui()
        
        
   
    