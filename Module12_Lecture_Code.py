'''
     Module 12 - Recursion
        
        Important information:
        
        Recursion is a technique in programming where a function calls itself.
        
        Anything that can be done with recursion can also be done iteratively and vice versa.
        
        Recursion is often used to solve problems that can be broken down into smaller, repetitive problems.
        
        Recursion "can" be slow and typically uses more memory (due to the overhead of maintaining the stack), so it is not always the best solution. (Iterative solutions are often faster and typically use less memory.)
        
        Recursion uses a base case to stop the recursion.
        
        Recursion uses the call stack to keep track of function calls.
        
'''
<<<<<<< HEAD



=======
def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
>>>>>>> acaac07c44df8eaed46eaca1b6a039abfb21bd6b

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
    
#To compare and contrast, here is the iterative solution:   
'''
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
        
'''

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


<<<<<<< HEAD
'''
1_  2_  3_   _5  _8  13_  _21  34_  _55  89_ 
1   2    3   4    5  6    7    8    9    10
'''

def fibonacci(n):
    if n <= 2:
        return n
=======
# This function demonstrates the use of dynamic programming to solve the Fibonacci sequence. The difference between this function and the previous one is that this function uses a list to store the values of the Fibonacci sequence as they are calculated, which allows the result to be retrieved in constant time. This is an example of memoization, which is a technique used to store the results of expensive function calls so that they can be retrieved later without having to recalculate them.
cons_mem_ret = []   
def dyn_fibonacci(n):
    if n in cons_mem_ret:
        return cons_mem_ret[n]
>>>>>>> acaac07c44df8eaed46eaca1b6a039abfb21bd6b
    else:
        if n <= 2:
            return n
        else:
            cons_mem_ret[n] = dyn_fibonacci(n - 1) + dyn_fibonacci(n - 2)
            return cons_mem_ret[n]
    
    
  
if __name__ == "__main__":
<<<<<<< HEAD
    #print(factorial(4))
    print(isPowerOfTwo(17))
    #print(fibonacci(10))
  
=======
    #print(fibonacci(6))
    print(factorial(5))
    #print(isPowerOfTwo(8))
    #print(dyn_fibonacci(6))
    
   
>>>>>>> acaac07c44df8eaed46eaca1b6a039abfb21bd6b
