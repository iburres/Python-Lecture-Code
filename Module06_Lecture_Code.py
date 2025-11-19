# import for pdf document

'''

Module 06 Lecture Code

r = read
w = write
a = append
r+ = read and write
w+ = write and read
a+ = append and read
rb = read binary
wb = write binary
ab = append binary
rb+ = read and write binary
wb+ = write and read binary
ab+ = append and read binary

open() function = open a file.  You can use this to create a file with the "w" mode. 
close() function = close a file
with open() as file: = Can be used to open a file and automatically close it when the block is done.  This is a good way to handle files. However, you cannot create a new file with the with statement.  The file must already exist!!!!

'''
import random

#Opening a file in sequential mode and reading line by line.
def read_files_by_line():
    
    file = open('/users/burres/desktop/Test.txt', 'r') # in windows, since you have a backslash, you need to use a raw string.  r'c:\users\burres\desktop\Test.txt' or two backslashes 'c:\\users\\burres\\desktop\\Test.txt'
    
    line_one = file.readline()
    print(f'{line_one}')
    line_two = file.readline()
    print(f'{line_two}')
    
    line_three = file.readline()
    print(f'{line_three}')

    file.close()
     
    
    length = len(line_one)
    print(f'The length of the first line is {length}')
    if "a" in line_one:
        # count the number of times the letter a appears in the first line
        count = line_one.count("a")
        print(f"The letter a appears: {count} times in the first line")

   
#opening a file and reading all of it's contents at once
def read_whole_file():
    file = open(r'/users/burres/desktop/Test.txt', 'r')
    
    contents = file.read()
    print(contents)
    file.close()
    
 
#writing to a file that does not exist.  Essentially creating a new file    
def write_to_new_file():
    
    file = open(r"/users/burres/desktop/newFile.txt", "w")


    file.write("Look at me, I can create a file and write to it at the same time.\n")     
    file.write("And look what happens\n")
    
    user_input = input("Enter a line of text: ")
    
    file.write(user_input)
    
    file.close()
    
def another():
    file = open(r"/users/burres/desktop/newFile.txt", "w")
    file.write("Hello")
    
#adding data to a file that does exist    
def append_to_file():
    
    file = open(r"/users/burres/desktop/newFile.txt", "a")
    
    file.write("\nAnd now I can add to the file without overwriting it!")     
    
    file.close()      


def writing_integers_to_files():
    #you will do this one with me
    try:
        outFile = open(r"c:\\users\\iburr\\documents\\write_number.txt", "w" )
        users_digit =int(input("Enter a number: "))
    except (ValueError):
        print("Please enter a digit only, not a letter or special character")
    #outFile.write(str(users_digit)) 
    pass  
  

def reading_int_from_files():
    outFile = open(r"c:\\users\\iburr\\documents\\write_number.txt", "r" )
    line_one = outFile.readline()
    
    #users_digit = int(input("Enter a number: "))
    result = int(line_one) * 2
    print(result)
    
    
#  Letter 1 to 10 people c3po 100

def skipping_line_space():
    
    # the with statement automatically closes the file when the block is done.  Also, you cannot create a new file with the with statement.  The file must already exist!!!!
    with open(r'/users/burres/desktop/nurseryRhyme.txt', 'r') as file:    
        for line in file:
            if not line.isspace():
                print(line, end='') 
                
                

# passing a file to another function
def pass_file():
    file = open(r'c:\\users\\iburr\\documents\\nurseryRhyme.txt', 'r')
    receive_file(file)
    file.close()

# receiving a file name as a parameter
def receive_file(file_name): 
        for line in file_name:
            if not line.isspace():
                print(line, end='')
                

def read_and_write():
    file = open(r'c:\\users\\iburr\\documents\\nurseryRhyme.txt', 'r+')
    for line in file:
        print(line, end='')
    users_info = input("Enter a word: ")
    file.write(f"\n\n{users_info}\n")
    file.close() # Remember to close the file when you are done with it.
    
# dealing with exceptions.  We wrap the code in a try block and then catch the error in the except block.  This is a good way to handle files.
def read_file_with_exceptions():
    file = open(r'/users/burres/desktop/nurseryRhyme.txt', 'r')
    
    try:
        file = open(r'/users/burres/desktop/nurseryRhyme.txt', 'r')
        for line in file:
            print(line, end='')
    except (FileNotFoundError, IOError, OSError, PermissionError): # this is how to do multiple exceptions
        print("File not found")   
        
def loop_with_exceptions():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            print(f"The number you entered is {user_input}")
            break
        except ValueError: # you can have more than one except block
            print("You did not enter an integer number.  Try again.")
            
def using_finaly():
    try:
        file = open(r'/users/burres/desktop/nurseryRhyme.txt', 'r')
        for line in file:
            print(line, end='')
    except IOError:
        print("File not found")
    finally: # finally block will always execute
        file.close()
        
def users_line():
    statement = input("Enter a statement: ")
    write_line(statement)
        
# passing parameters to a function that reads a file
def write_line(sentence):
    file = open(r'c:\\users\\iburr\\documents\\nurseryRhyme.txt', 'w+')
    file.write(sentence)
    file.close()
    #with open(r'users/burres/desktop/user_file.txt', 'w') as file:
    #    file.write(sentence) 
    
def infinite_loop():
    
    #my_num = 5
    
    try:
        my_num = 4
        while(my_num != 5 ):
            print("This loops forevery")
            
    except TimeoutError:
        print("Hey programmer, you made an infinite loop")
    
               
def main():
    #read_files_by_line()
    #read_whole_file()
    #write_to_new_file()
    #another()
    #append_to_file()
    #writing_integers_to_files()
    #reading_int_from_files()
    #skipping_line_space()
    #pass_file()
    #read_and_write()
    #write_line(sentence_1)
    #read_file_with_exceptions()
    #loop_with_exceptions()
    #using_finaly()
    #users_line()
    infinite_loop()
    pass

if __name__ == "__main__":
    main()
