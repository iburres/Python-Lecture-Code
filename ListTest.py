'''

Solution code for in-class question regarding calling a function from the appends() method. 

'''

#Example 1:  Solution from in-class question. This is NOT how I would solve the problem, but it IS a solution to what was asked in class. 
def loopingFunc(t):

    #This entire function is really useless, since the same thing can be achieved in the appending method by adding another loop. So, my suggestion is to only use the append() method to add an element to a list, not to call a function as an argument from the append() method. 
    for i in range(0, 11):
        
        return t  


def appending():
    my_empty_list = []
    
    #take out this loop and you will see we only get back 10. 
    for i in range(10, 21):    
        my_empty_list.append((loopingFunc(i))) #calling the function in the append method.  
    
    print(my_empty_list) 
    

#Example 2: This is how I would solve the problem.  Uncomment the 'my_results' function call in main() and place a comment in front of the 'appending()' function.
def appending_to_list(x, y):
    
    appended_list = []
    
    for i in range(x, y + 1):
        appended_list.append(i)# i will start at the value of x and end at the value of y
        
    return appended_list
    

def my_results():
    
    print(appending_to_list(10, 20))# we can make the values anything we want now. We can pass variables that stored values from a user too.    

if __name__ == "__main__":
    appending()
    #my_results()
   


 