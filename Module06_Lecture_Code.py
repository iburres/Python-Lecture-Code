'''

Module 06 Lecture Code

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
    outFile = open(r"/users/burres/desktop/write_number.txt", "w" )
    users_digit = int(input("Enter a number: "))
    outFile.write(str(users_digit))
    pass  
  

def reading_int_from_files():
    outFile = open(r"/users/burres/desktop/write_number.txt", "r" )
    line_one = outFile.readline()
    
    users_digit = int(input("Enter a number: "))
    result = int(line_one) + users_digit
    print(result)
    

def skipping_line_space():
    
    with open(r'/users/burres/desktop/nurseryRhyme.txt', 'r') as file:
        for line in file:
            if not line.isspace():
                print(line, end='')
                
                
def main():
    read_files_by_line()
    #read_whole_file()
    #write_to_new_file()
    #another()
    #append_to_file()
    #writing_integers_to_files()
    #reading_int_from_files()
    #skipping_line_space()

if __name__ == "__main__":
    main()
