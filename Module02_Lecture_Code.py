'''
    This is called block-comments.  We can use 
    either apostrphes ' or quotes "
'''
# This is a single comment line. 

# Pseudo code is written language that has some some code-like structure but is not perfect syntax
# Example:   
'''
    print welcome message
    Ask the user their name
    Ask the user for the year they were born
    convert string from input to integer
    Subtract year they were born from current year
    print the difference, which is a rough estimate of the user's age 
'''

#Declaring and Initializing variables

#strings
students_name = "Alice"  # This is a variable of type string, since it contains only characters
students_ID = "784564"   # This is also a string.  The nunbers in the string are just symbols. Can't do math!!

#integers
num_of_students = 40
median_age = 24
big_number = 78939449875345 # don't use commas, or it will think they are multiple values

#floating point values (floats)
average_age = 23.456
interest_rate = 4.35567 # floating point values have 32-bit representation
double = 5.6666777897349754 # doubles are 64-bit values (so they can be much longer)

#processing data (= means assign,  == means equal)
num_1 = 55
num_2 = 66
result = num_1 + num_2 # this line adds the two numbers on the right and then stores the sum into variable result

# doing math with different data types is fine, as long as they are numbers (int, float, double, etc)
# However, if we add a number with a string using + then we are actually concatenating the values.  This means
# chaining together.
my_string = "789 Happy Days" 
my_num = 45
# The line of code below will cause an error. Go ahead and remove the # on line 45 to see this for yourself
# mush_together = my_string + my_num

#correct way to concatenate
mush_together = my_string + str(my_num) # this is called type-conversion or casting. 
print(mush_together) 

# Output - goes to STDOUT, or standard out.  This will pop up in the terminal below.  We will eventually get
# to programming using GUIs
print("Hello World")
print("Welcome student")
print("This is how we use multiple values in a print statment", mush_together) # use commas to separate values. 

#input - default to string values. That means if I enter 8, it will treat it as the character 8, not int 8
first_name = input("Please enter your first name: ") # try using your name then a number
print("Hello ", first_name, " it's nice to meet you")

#input using integers and floats
year_born = int(input("What year were you born? "))
percentage = float(input("What is the percentage, in decimal, of students who will stop programming after this course? "))

print(percentage * 100, "%")


                         
