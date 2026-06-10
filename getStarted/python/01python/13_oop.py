# OOP in Python
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for better organization, reusability, and maintainability of code.
#

# Step 1: Basic Class and Object
# Goal:
# Create a Book class with basic details like title and author, then create an object from it.
# Step 3: Inheritance
# Goal:
# Create an EBook class that inherits from Book and adds a file size.
# Step 4: Encapsulation
# Goal:
# Make the author private and give a getter method for it.
# Step 5: Polymorphism

# Goal:
# Create a method called book_type in both Book and EBook, but make them behave differently.



# Step 7: Static Method
# 

# Goal:
# Add a general library rule method.

# Step 9: isinstance() Function
# Check whether an EBook object is also a Book object.






class Book:
    total_books = 0
    def __init__(self, title, author):
        Book.total_books += 1
        self.title = title
        self.__author = author
    def get_author(self):
        return self.__author
    def display_info(self):
        return f"Title: {self.title}, Author: {self.__author}"
    def book_type(self):
        return "This is a physical book."
     @staticmethod
    def library_rule():
        return "Please return books within 2 weeks."


book1 = Book("harry potter", "j.k. rowling")
print(book1.get_author())  # Output: j.k. rowling
print(book1.display_info())

class EBook(Book, Searchable, Downloadable):
    def __init__(self, title ,author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def book_type(self):
        return "This is an electronic book."

ebook1 = EBook("richest man is babaloyn", "robert kiyosaki", "2MB")
print(ebook1.get_author())  # Output: robert kiyosakiss
print(ebook1.file_size)  # Output: 2MB
print(ebook1.display_info())  # Output: Title: richest man is babaloyn, Author: robert kiyosaki
print(ebook1.book_type())  # Output: This is an electronic book.
print(book1.book_type())  # Output: This is a physical book.
ebook1.title = "rich"


print(ebook1.display_info())  # Output: Title: rich, Author: robert kiyosaki

# //changing the value of author
ebook1.__author = "new author"
print(ebook1.get_author()) 
print(Book.total_books)  # Output: 2

# print(ebook1.library_rule())  # Output: Please return books within 2 weeks.
# print(book1.library_rule())  # Output: Please return books within 2 weeks.
print(Book.library_rule())  # Output: Please return books within 2 weeks.
print(isinstance(ebook1, Book))  # Output: True
# Step 10: Multiple Inheritance
# Goal:
# Make the EBook class inherit from two helper classes: Searchable and Downloadable

class Searchable:
    def isSearchable(self):
        return True

class Downloadable:
    def isDownloadable(self):
        return True


print(ebook1.isSearchable())  # Output: True
print(ebook1.isDownloadable())  # Output: True