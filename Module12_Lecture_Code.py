'''
     Module 12 - Recursion
        
        Important information:
        
        Recursion is a technique in programming where a function calls itself.
        
        Anything that can be done with recursion can also be done iteratively and vice versa.
        
        Recursion is often used to solve problems that can be broken down into smaller, repetitive problems.
        
        Recursion can be slow and use a lot of memory, so it is not always the best solution. (Iterative solutions are often faster and use less memory.)
        
        Recursion uses a base case to stop the recursion.
        
        Recursion uses the call stack to keep track of function calls.
        
'''




#4! = 4 * 3 * 2 * 1 = 24


# Pseudo code Iterative solution for factorial of 4:
# accum = 4, and n = accum - 1
# now reduce n by 1 for pass through the loop
# accum * (n) = 12
# accum = 12
# accum * (n)
# Take the number and multiply by 1 less than the number.
# Store that value into accumulator

'''
                
          fac(1)       return 1                
n        fac(2)            2               n = 1
n       fac(3)               6               n
n     fac(4)                    24             n
n    fac(5)                        120           n
'''

'''
n = 4
n = 3

'''


def factorial(n):
    
    # Base case
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1) # Recursive call, meaning the function calls itself.

# Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.

def isPowerOfTwo(n):
    # We can have two base cases, such as: n == 1 and n % 2 != 0 or n == 0
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0: 
        return False
    else:
        return isPowerOfTwo(n // 2)
    
# Let's see how this looks on the call stack:
# isPowerOfTwo(16)
# isPowerOfTwo(8)
# isPowerOfTwo(4)
# isPowerOfTwo(2)
# isPowerOfTwo(1) -> True
# isPowerOfTwo(0) -> False


'''
1_  2_  3_   _5  _8  13_  _21  34_  _55  89_ 
1   2    3   4    5  6    7    8    9    10
'''

def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
  
if __name__ == "__main__":
    #print(factorial(4))
    print(isPowerOfTwo(17))
    #print(fibonacci(10))
  
