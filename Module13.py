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
        12. \ - Escape character
        13. \s - Whitespace
        
        and many more...
'''
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
    if re.search(r'^\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$', input_phone):
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



if __name__ == '__main__':
    print(regex_email('john.smith@utsa.edu'))
    print(regex_phone('210-45S-4433'))
    print(zero_or_more(''))
    print(abc123('tty677'))
    