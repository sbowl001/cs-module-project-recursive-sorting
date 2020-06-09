# goal: code a factorial function 

#  n * (n - 1)  ... 1 


# recursive 

# define base case 

# return if we are at n = 1
# move towards the base case 
# Call itself

def factorial(n):
    if n == 1: 
        return 1

    return n * factorial(n - 1)




print(factorial(3) == 6)
print(factorial(4) == 24)


# make a tracker: total 
# make a while loop and decrement n as we go 
# multiply our tracker at every step 
# return tracker 

def iter_factorial(n):
    total = 1 
    while n != 1: 
        total *= n 
        n -= 1 
    return total 



    # Space complexityL  iterative 
    # Time complexity: O(n) for both 