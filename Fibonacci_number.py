# Time Complexity O(2^n)

def fibonacci(n):
    if n<0:
        print("Incorrect input")

    elif n==0:
        return 0

    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(30))

#####################################################################################################

# Time Complexity of O(n)
# Memoization technique is used
fibonacci_cache = {}
def fibonacci(n):

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    elif n==1 :
        value = 1
    
    elif n==2 :
        value =1

    elif n >2 : 
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value
    fibonacci_cache[n] = value
    return value

for i in range(1,100):
    print(fibonacci(i))

#################################################################################################################

# Time Complexity of O(n)
# Memoization technique using lru_cache
# RecursionError: maximum recursion depth exceeded at 500

from functools import lru_cache

@lru_cache(maxsize= 1000)
def fibonacci(n):
    if type(n) != int :
        raise TypeError("n must be positive integer")
    if n<0:
        raise ValueError("n must be positive integer")

    elif n==0:
        return 0

    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(499))

######################################################################################################################

# Time Complexity of O(1)
# Previous two values are stored in variables 
# Space Optimisataion

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
        return b
 
print(fibonacci(50000))