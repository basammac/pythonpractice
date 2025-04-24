# class Book:
#     pass
# book = Book()
# print(book)
class Book:
     def __init__(self,title,author,genre,pages):
         print("Init methos is called")
         self.title = title
         self.author = author
         self.genre = genre
         self.pages = pages
     def __str__(self):
         return "Title: {}\nAuthor: {}\ngenre: {}\npages: {}".format(self.title,self.author,self.genre,self.pages)
     def __len__(self):
         return self.pages
     def __del__(self):
         print("Book is deleted")

book = Book("Know the truth","gordan","spiritual",240)
print(book)
print(len(book))
book = Book("Know the truth","gordan","spiritual",240)
del book
print(book)

