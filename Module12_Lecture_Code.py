'''
     Module 12 - Recursion
        
        Important information:
        
        Recursion is a technique in programming where a function calls itself.
        
        Anything that can be done with recursion can also be done iteratively.
        
        Recursion is often used to solve problems that can be broken down into smaller, repetitive problems.
        
        Recursion can be slow and use a lot of memory, so it is not always the best solution. (Iterative solutions are often faster and use less memory.)
        
        Recursion uses a base case to stop the recursion.
        
        Recursion uses the call stack to keep track of function calls.
'''

def factorial(n):
    
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # Recursive call, meaning the function calls itself.

# Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.

def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0:
        return False
    else:
        return isPowerOfTwo(n // 2)

   
if __name__ == "__main__":
    factorial(5)
    isPowerOfTwo(16)