'''
Module 7 Lecture Code

'''

#Lists

#my_list = [9, 8, 18, 0, -4, 12, 15] #indexes are from 0 to N - 1
#my_text_list = ["Orange", "Bananas", "Fruits"]
#my_combo_list = ["Orange", 8, 3.45, "Cars"]
#my_tuple = (4, 5, 8, 9) #tuples are the same
#empty_list = []


'''
#empty_tuple = ()
print(my_combo_list)
#indexes are mutable, tuples are immutable
length = len(my_combo_list)
print(length)


for elem in my_combo_list:
    print(elem)


my_list.append(6)

print(my_list)

my_list.insert(2, 10)
#print(my_list)

my_list[2] = 10
print(my_list)

try:
    my_list.remove(5)
    print(my_list)
except ValueError:
    print("That element is not in the list")

my_list.pop(3)
print(my_list)

del my_list[1]
print(my_list)

#this_is_a_list = "I love Python"

#length = len(my_list)
print("\n\n")

#print(my_combo_list[1])
#print(my_combo_list.index("Cars"))

#my_list.reverse()
#print(my_list)

#my_list.sort()
#print(my_list)
#reverse
#my_list.reverse()
#print(my_list)


#greadebook  with 10 grades, 0 -100
#store the grades into a list
grade_book = []
how_many_grades = int(input("How many grades: "))
for i in range(0, how_many_grades):
    grade = int(input("Enter the first 10 grades: "))
    grade_book.append(grade)
    #grade_book[i] = grade

print(grade_book)

total = sum(grade_book)
length = len(grade_book)
print(total / length)
grade_book.remove(70)
#print(grade_book)

grade_book[2] = 100
#print(grade_book)


index = grade_book.index("troubador")
print(index)

grade_book[index] = 75
#print(grade_book)
'''

'''
PART 2

'''
'''
grade_book = []
how_many_grades = int(input("How many grades: "))
for i in range(0, how_many_grades):
    grade = int(input("Enter the first 10 grades: "))
    #grade_book.append(grade)
    grade_book.insert(i, grade) #additional method

print(grade_book)
'''
#converting tuples to lists
my_tuple = (9, 5, 6, 0)
my_list = list(my_tuple)
print(my_list)
my_list.append(14)
print(my_list)

#my_tuple.append(9)

#iterable lists
numbers = list(range(1, 10, 2))
print(numbers)


#list comprehension and the repeition operator
new_numbers = [1, 3, 5, 6, 2, 10]


new_list = [element * 2 for element in new_numbers if element > 5]

#for element in new_numbers:
#    if element > 5:
#        temp = element * 2
#        new_list.append(temp)

print(new_list)

#slicing lists
non_sliced = [0, 1, 2, 3, 4, 5, 6]
sliced = non_sliced[2:4]
print(sliced)
print(non_sliced)

#concatonating lists
list1 = [1, 2, 3, 4]
list2 = [8, 10, 12, 14]
list3 = list1 + list2
print(list3)

#finding items in a list with in operator
names_list = ["John", "Sally", "Mike", "Terrence", "Sophia", "Sandheep"]

if "John" in names_list:
    print(names_list.index("John"))
    
name = "Mike"

if name in names_list:
    print(names_list.index(name))
    
#sorting lists with text and multiple values
my_text_list = ['Orange', 'Bananas', 'Fruits']
my_combo_list = ["Orange", 8, 3.45, "Cars"]

list_sort = sorted(my_text_list) #notice the use of sorted here, instead of .sort()
print(list_sort)

#We cannot sort lists with multiple data types. We can extract them into separate lists though and sort those. 
#list_sort2 = sorted(my_combo_list)
#print(list_sort2)

#The count function
final_list = ["Ted", "Bill", "Adventures", "Ted", "Keanu", "Ted", "Greatest"]
print(final_list.count("Ted"))
    



#Student coding in class program
#   .isalpha()   .isdigit()
'''
Using my_combo_list = ["Orange", 8, 3, 10, "Sam", -2,"Cars"]
extract the strings from the list and sort them.  Print the new list to stdout
'''









my_combo_list = ["Orange", 3, 10, "Sam", -2,"Cars"]
temp_list = []
string_list = []

for item in my_combo_list:
    temp = str(item)
    temp_list.append(temp)
    
for item in temp_list:
    if item.isalpha() :
        string_list.append(item)
        
print(string_list)
print(sorted(string_list))

#This can also be done with type, which is much faster code
last_list = [] 
last_list = [x for x in my_combo_list if type(x)==int]
print(last_list)

first_list = [2, 4, 6, 8]
second_list = [1, 3, 5, 7]
new_list = []


[1, 2, 3, 4][5, 6, 7, 8]

for i in range(0, len(second_list)):
    new_list.append(first_list[i] + second_list[i])
print(new_list)


        
