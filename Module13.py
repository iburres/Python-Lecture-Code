'''
        Module 13 - Regular Expressions
        
        (555)556-7890
        
        List of Regular Expressions:
        1. ^ - Start of string
        2. $ - End of string
        3. . - Any character
        4. [...] - Any character listed between the brackets
        5. [^...] - Any character not listed between the brackets
        6. * - Zero or more of the preceding character
        7. + - One or more of the preceding character
        8. ? - Zero or one of the preceding character
        9. {n} - Exactly n of the preceding character
        10. {n,} - n or more of the preceding character
        11. {n,m} - Between n and m of the preceding character
        
        Special Sequences:
        12. \ - Escape character
        13. \s - Whitespace
        14. \S - Not whitespace
        15. \d - Digit
        16. \D - Not digit
        17. \w - Word character
        18. \W - Not word character
        20. | - Or
        21. (...) - Group
        22. \b - Word boundary
        23. \B - Not word boundary
        24. \A - Start of string
        25. \Z - End of string
        
        and many more...
'''
# (210)555-5555
import re

def regex_email(input_email):
    '''
        Function to validate an email address
    '''
    import re
    if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', input_email):
        return True
    return False

def regex_phone(input_phone):
    '''
        Function to validate a phone number
    '''
    import re
    if re.search(r'^\(?[0-9]{3}\)?[0-9]{3}[-.]?[0-9]{4}$', input_phone):
        return True
    return False

def zero_or_more(input_string):
    '''
        Function to validate zero or more of the preceding character
    '''
    import re
    if re.search(r'ab*', input_string):
        return True
    return False

def abc123(n):
    if re.search(r'^[a-zA-Z]{3}[0-9]{3}$', n):
        return True
    return False

def using_split(n):
    
    # Split the string into a list using regex
    n_list = re.split(r'\s', n)
    print(n_list)
    
# We can use regex to validate user input, to make sure it is in the correct format, and to 
# extract information from a string. 

# find regex in a string
def find_regex():
    '''
        Function to find a regex in a string
    '''
    import re
    string = 'The quick brown fox jumps over the lazy dog'
    regex = r'\b\w{5}\b'
    result = re.findall(regex, string)# we are using the regex declared above to find all the words that are 5 characters long
    print(result)

# using match
def using_match():
    '''
        Function to use match
    '''
    # match checks for a match only at the beginning of the string
    import re
    string = 'Any quick brown fox jumps over the lazy dog'
    regex = r'\b\w{3}\b'
    result = re.match(regex, string)# match returns None if the regex is not found at the beginning of the string and returns the match if it is found based on the index
    print(result)
   
    
#findall() - returns a list containing all matches
def using_findall():
    '''
        Function to use findall
    '''
    import re
    string = 'the quick brown fox jumps over the lazy dog'
    regex = r'\b\w{3}\b'
    result = re.findall(regex, string)
    print(result)

#def using_sub():
#    import re

#    txt = "The rain in Spain"
#    x = re.sub("\s", "9", txt)# replace all the whitespaces with 9
#    print(x)  
    
# forward looking assertion. 
def forward_looking_assertion():
    
    import re
    
    # lookahead example 
    example = re.search(r'geeks(?=[a-z])', "geeksforgeeks") 
    
  
# display output 
    print("Pattern:", example.group()) 
    print("Pattern found from index:", 
      example.start(), "to", 
      example.end())
    
def forward_looking_with_no_match():
    
    import re
    
    example = re.search(r'geeks(?=[a-z])',  
                    "geeks123") 
  
    # output 
    print(example)
    
def not_in_string():
    
    import re
    
    example = re.search(r'^[^y]*$', 'zang')
    print(example)
    

if __name__ == '__main__':
    #print(regex_email('_@utsa.edu'))
    print(regex_phone('(555)555-5555'))
    number = input("Enter your phone number: ")
    result = regex_phone(number)
    print(result)
    #print(zero_or_more('c'))
    #print(abc123('tty677'))
    #using_split("Hello World of Python")
    #find_regex()
    #using_match()
    #using_findall()
    #using_sub()
    #forward_looking_assertion()
    #forward_looking_with_no_match()
    #not_in_string()
    