# Count the no of occurences:

# def count_frequency(list1):
#     my_dic={}
#     for i in list1:
#         my_dic[i]=my_dic.get(i,0)+1
#     print(my_dic)


# result = count_frequency(['a','b','a','c','b'])
# print(result)


# merge two dictionaries:

# dict1={'a':1,'b':2}
# dict2={'b':3,'c':4}
# dict1.update(dict2)
# print(dict1)


# Key exists:
# def key_values(dictinary):
#     if 'a' in dictinary:
#         print("True")
#     else:
#         print("False")


# result={'a':1,'b':2}
# key_values(result)


# #Maximum values:
# result={'a':2,'b':25,'c':5}
# my_dic=max(result,key=result.get)
# print(my_dic)


# frequency list of element:
# def frequency_dic(list1):
#     my_dic={}
#     for i in list1:
#         my_dic[i]=(my_dic.get(i,0)+1)
#     return(my_dic)


# my_list=['apple','banana','apple','orange','banana','apple']
# result=frequency_dic(my_list)
# print(result)


# Max key:

# def max_key(dic1):
#     my_dic=max(dic1,key=dic1.get)
#     return (my_dic)


# my_list={'apple':3,'banana':5,'orange':7}
# result=max_key(my_list)
# print(result)

# palindrome or not:
# def is_palindrome(string1):
#     # return string1 == string1[::-1]
#         #[OR]

#     string2=''
#     for i in string1:
#         string2=i+string2
#     if string2 == string1:
#         print(f'The given string {string1} is palindrome')
#     else:
#         print(f'The given string {string1} is not a palindrome')


# result=is_palindrome('racecar')
# print(result)


# Factorial:

# def factorial_series(number):
#     if number<0:
#         return
#     if number==0:
#         return 1
#     return (number*factorial_series(number-1))


# result=factorial_series(6)
# print(result)


# fibonacci:

def fibonacci_series(number):
    list1 = [0, 1]
    for i in range(2, number + 1):
        list1.append(list1[-2] + list1[-1])
    print(list1)


result = fibonacci_series(5)