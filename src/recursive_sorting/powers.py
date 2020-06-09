# given a and b , return a ** b, wihout using inpult operator 


# valid and invalid inputs 

# invalid: letters
# valid numbers
# no negative numbers for b

# 1/ ( 2 ** 2)

# square root with a power : raise to 1/2 , 0.5


# let's not handle decimal numbers for b


# Iterative pseudo code 
# have a counter == a

# while loop: while b isn't 0

# multiply a by itself
# decrement b to approach 0


def iter_power(a , b):
    if b == 0: 
        return 1

    product = a
    while b != 1: 
        product *= a 
        b -= 1 
    return product 



print(iter_power(2, 3) == (2 ** 3))
print(iter_power(10, 2) == (10 ** 2))
print(iter_power(10, 0) == (10 ** 0))

print(iter_power(2, -2) == (2 ** -2))

print(iter_power(2, 1) == (2))
print(iter_power(100, 1) == (1))


# iterative pseudocode 
def iter_power2(a, b):
    # check if b is an integer, otherwise return message
    if type(b) is not int: 
        return "Sorry we don't handle decimals"

    # check if b == 0 , is so return 1 
    if b == 0: 
        return 1

    # check if b < 0: if so, multiply by -1, set invert to true 
    invert = False 
    if b < 0: 
        b*= -1
        invert = True

    # have a counter == a 
        product = a 

    # while loop while b isnt' 1 
    while b != 1: 
        # multiply by the counter a
        product *= a
        # decrement b to approach 1
        b -= 1

        # return counter 
        if invert: 
            return 1 / product 
        else: 
            return product 