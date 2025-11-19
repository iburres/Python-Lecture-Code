
def toUpperCaseList():
    
    my_string = "abdFEabcvdgetRGETFfo982734oe@$&e"
    
    length = len(my_string)
    
    
    if "e" in my_string:
        
        result = my_string.find("e")
        print(f'The index location of the first e is: {result}')
        if(result < length):
            my_string_2 = my_string.replace("e", "0", 1)
            print(my_string_2)
        
        result2 = my_string_2.find("e")
        
        print(f'The index location of the second string is: {result2}')
        my_string_3 = my_string.replace("e", "E", 2)
        print(my_string_3)
    
        my_string_4 = my_string.replace("e", "9")
        print(my_string_4)
        
        my_list = list(my_string)
        my_list[27] = "Q"
        print("".join(my_list))
       
       
    

    
    


if __name__ == "__main__":
    
    toUpperCaseList()
