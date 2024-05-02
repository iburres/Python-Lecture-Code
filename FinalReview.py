''' Final exam review'''




def reversingLists():

    song_array = ["Red", "99", "Balloons"]
    
    # Solution 1:
    song_array.reverse()
    
    reversed_array = reversed(song_array)
    
    print(song_array)
    
    #Solution 2:
    empty_list = []
    length = len(song_array)
    
    for i in range(length - 1, -1, -1):
        
        empty_list.append(song_array[i])
            
    print(empty_list)
        

def determineCharInList():
    
    song_array = ["Red", "99", "Balloons"]
    
    for elem in song_array:
        if elem.isdigit():
            print(f"index location: {song_array.index(elem)} is an integer")
    
# if __name__ == "__main__": is used to execute some code only if the file was run directly, and not imported. If you import this script as a module in another script, the code under if __name__ == "__main__": will not be executed. In that case you should use the def main() function and call it from the other script.
if __name__ == "__main__":
    reversingLists()
    determineCharInList()