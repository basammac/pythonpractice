#print(a)
#int("xxuu5567")
#3/0
# for i in range(10)
#     print(i)

# a=int("xyz123")
# try:
#     a = int("xyz123")
#     print("the program is here")
# except ValueError:
#     print("an error occured")
# print("program finished")

# try:
#     a = int("124abc")
#     print("the program is here")
# except ValueError:
#     print("Entered invalid value for th conversion Please check the value")
# print("program finished")

# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Any number can not be divided by zero, Please enter correct number")
# except ValueError:
#     print("Entered invalid value for the conversion, Please check your value")
# print("Program has finished")

# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)
# except (ZeroDivisionError,ValueError):
#     print("Zerodivision error or value error occured")
# print("Program has finished")

# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Any number can not be divided by zero, Please enter correct number")
# except ValueError:
#     print("Entered invalid value for the conversion, Please check your value")
# else:
#     if (num1 < 0 or num2<0):
#         print("Negetive number is entered")
# print("Program has finished")

# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Any number can not be divided by zero, Please enter correct number")
# except ValueError:
#     print("Entered invalid value for the conversion, Please check your value")
# else:
#     if (num1 < 0 or num2<0):
#         print("Negetive number is entered")
# finally:
#     print("this statement will alway be executed")
# print("Program has finished")

# try:
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Any number can not be divided by zero, Please enter correct number")
# except ValueError:
#     print("Entered invalid value for the conversion, Please check your value")
# else:
#     if (num1 < 0 or num2<0):
#         print("Negetive number is entered")
# finally:
#     print("this statement will alway be executed")
# print("Program has finished")


#Raising exception

# def sqrt(num):
#     if (num <=0):
#         raise ValueError("you shoudl enter positive number to calculate square root of a number")
#     else:
#         return num ** 0.5
# print(sqrt(-4))

def sqrt(num):
     if (num <=0):
         raise ValueError("you shoudl enter positive number to calculate square root of a number")
     else:
        return num ** 0.5
try:
    print(sqrt(-4))
except ValueError:
    print("An error occured in the function")
