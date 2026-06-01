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







class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    def get_author(self):
        return self.__author
    def display_info(self):
        return f"Title: {self.title}, Author: {self.__author}"


book1 = Book("harry potter", "j.k. rowling")
print(book1.get_author())  # Output: j.k. rowling
print(book1.display_info())

class EBook(Book):
    def __init__(self, title ,author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        

ebook1 = EBook("richest man is babaloyn", "robert kiyosaki", "2MB")
print(ebook1.get_author())  # Output: robert kiyosakiss
print(ebook1.file_size)  # Output: 2MB
print(ebook1.display_info())  # Output: Title: richest man is babaloyn, Author: robert kiyosaki

