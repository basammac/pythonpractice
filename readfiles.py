# file=open("D:\Documents\test1.txt","r",encoding = "utf-8")
#
# file.close()
# try:
#       file=open("testbasu","r")
#
# except FileNotFoundError:
#       print("file not found")

# file=open("D:/Documents/test1.txt","r",encoding = "utf-8")
# content=file.read()
# print(content)

# file=open("D:/Documents/test1.txt","r",encoding = "utf-8")
# print(file.readline())
# file.close()

# file=open("D:/Documents/test1.txt","r",encoding = "utf-8")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# with open("D:/Documents/test1.txt","r",encoding = "utf-8") as file:
#     mylist=file.readlines()
#     print(mylist)


# file=open("D:/Documents/test1.txt","r",encoding = "utf-8")
# for i in file:
#     print(i)
# file.close()
# with open("D:/Documents/test1.txt","r",encoding = "utf-8") as file:
#     for i in file:
#         print(i,end="")

# with open("D:/Documents/stulist.txt","r",encoding = "utf-8") as file:
#     print(file.tell())

 # with open("D:/Documents/stulist.txt","r",encoding = "utf-8") as file:
 #     print(file.tell())
 #     file.seek(15)
 #     print(file.tell())


# with open("D:/Documents/stulist.txt","w",encoding = "utf-8") as file:
#      file.write("hi dear basu")

# with open("D:/Documents/stulist.txt", "a+", encoding="utf-8") as file:
#      file.write("\nhi dear sharabu")
#      print(file.read())

with open("D:/Documents/stulist.txt", "r+", encoding="utf-8") as file:
     file.seek(10)
     file.write("hey naayi")
with open("D:/Documents/stulist.txt", "r+", encoding="utf-8") as file:
     print(file.read())