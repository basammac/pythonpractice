# import math
# print(dir(math))
# print(help(math))
# print(math.factorial(5))
# print(math.factorial(6))
# print(math.pow(2,4))
# print(math.pow(2,5))
# print(math.trunc(2.4))

import math as m
# print(m.sqrt(4))
# from math import *
# print(factorial(4))
# print(floor(3.2))

# from math import factorial, trunc, sqrt
#
# print(factorial(3))
# print(trunc(4.6))
# print(floor(2.3))

def factorial(number):
    print("My factorial function")
    factorial=1
    if (number ==0 or number==1):
        return 1
    else:
        while(number>=1):
            factorial *=number
            number -=1
        return factorial

from math import *
print(factorial(5))
print(factorial(5))

