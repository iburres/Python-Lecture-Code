
'''
Module 5 Lecture Code

All about Functions

'''

# global variable
my_global = 5 # this variable can be called from any function in the module, unlike a local variable declared inside a function which can only be called from that function. Also, we cannot modify a global variable from inside a function unless we use the global keyword.**

# constants in Python are declared using all capital letters. Technically, Python does not have constants, but the convention is to declare a variable as a constant by using all capital letters.
PI = 3.14159 # 

PHRASE = "Hello, World!" # This is a constant. The value of a constant cannot be changed once it is declared.

counter = 0

def playing_with_constants():
    #global PI # NEVER EVER EVER DO THIS. This is a bad practice. It is better to declare the constant as a global variable at the top of the module.
    #PI = 2.14
    print(PI)
    print(PHRASE)
    print(PI)
    print(9 * PI)
    
def local_constant():
    #global PI
    PI = 2.14
    print(PI)
    print(PHRASE)
    PI = 3.14
    print(PI)
    
    
def increment():
    global counter
    counter += 1
    print(counter)

#This function accepts a single argument in its parameter field and adds that number with a declared integer
def addition(num_1):
    #a = 4
    x = 5
    total = num_1 + x - my_global # The global variable my_global is used in the function now.
    #multiplication(total)
    return total 

def subtraction():
    
    a = 6
    b = 10
    total = a - b - my_global # The global variable my_global is used in the function now.
    print(total)
    
    
def multiplication(c):
    #a = 6
    #b = 10
    #total = a * b * c
    
    d = int(input("Enter a number: "))
    return c * d

    
def division():
    a = 10
    b = 6
    total = a // b # The double forward slash is used to perform integer division. The result of the division is an integer. If you want the result of the division to be a float, you can use a single forward slash.
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

# The forwared slash in the parameter field makes the parameters positional only
def positional_arguments(a, b, c):
    print(a, b, c)
    

# The asterisk in the parameter field makes the parameters keyword only
def keyword_arguments(*, a, b, c):
    print(a, b, c)

# only the values after the asterisk are keyword only   
def keyword_in_middle(a, *, b, c):
    print(a, b, c)
    
# passing a function as an argument to another function
def function_as_argument(func, *, x, y):
   
    return func(x, y)

# chaging the order of the parameters in the function call
def changed_order(a, b, c):
    print(a, b, c)
    
# The double asterisk in the parameter field makes the parameters keyword only
def keyword_arguments(**kwargs):
    print(kwargs) # kwargs is a dictionary that holds the keyword arguments passed to the function. We will learn more about dictionaries in a later module.

# assigning values to the parameters in the function definition
def default_arguments(a = 1, b = 2, c = 3):
    print(a, b, c)

      
def change_global():
    global my_global # The global keyword is used to modify the value of a global variable from inside a function.
    my_global = 10
    print(my_global)

def change_global_without_keyword():
    my_global = 14 
    print(my_global)   
    
def try_to_change_constant():
    PI = 2.7 # This will work because Python does not support true constants. 
    print(PI)



if __name__ == "__main__":  
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))
    #result = addition(x, y)
    #def gui():
    #    print("hello world")   Can do this, but alternate method is preferred. 
    #product = multiplication(result)
    #print(product)
    gui()
    #playing_with_constants()
    local_constant()
    positional_arguments(1, 2, 3)
    keyword_arguments(a = 1, b = 2, c = 3) # keyword arguments must be used when calling the function. A keyword argument is a name-value pair that you pass to a function.
    compute(7)
    changed_order(c = 3, a = 1, b = 2)
    keyword_arguments(name = "John", age = 25, city = "New York")
    total = function_as_argument(addition, x=5, y=6)
    print(total)
    
    # changed the order of the arguments in the function call
    default_arguments(5, 6, 7) #The default values are overridden by the values passed in the function call
    
    keyword_in_middle(1, b = 2, c = 3)# The value of a is positional only, while the values of b and c are keyword only
    
    #calling a function from print
    print(addition(4, 5))
    
    #calling a function from another function
    addition(multiplication(5), 7) # The result of the multiplication function is passed as an argument to the first positional argument in the addition function. The numbe 7 is passed as the second positional argument in the addition function.
    #The use of end parameter in the print function
    
    global_result = change_global_without_keyword()
    print(global_result)
    
    try_to_change_constant()
    change_global()
    #try_to_change_constant()
    
    # calling the random.randint function from an f-string
    import random
    print(f"The random number is: {random.randint(1, 10)}")
    
    print("Hello", end = " ") # The end parameter is used to specify the character that will be printed at the end of the string. By default, the end parameter is set to "\n" which means that a new line will be printed at the end of the string. In this case, we are changing the end parameter to a space character. 
    
    increment()  
    
  
    
    
        
   



 
 