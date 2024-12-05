# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print(self.name, "says woof")
        
# dog_1 = Dog("Roxy")

# =============================================================================

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

#     def speak(self):
#         print(self.name, "says woof")
        
# dog_1 = Dog("Roxy", "Red")
# print(dog_1.name, dog_1.color)
# dog_1.speak()

# ===================================================================================================

# 1)
# your task is create basic library management system using inheritance implement following classes

# Base class :- LibraryItem
# attributes:- title(String),author(String),publication_year(int)
# methods:- display_info()   :-print the details of the items

# 2)

# derive class:- Book
# inherit from LibraryItem
# addition all attributes:- genre,isbn

# override:- display_info

# print the detail including genre and isbn 

# 3)
# derived class:- Magazine
# inherit from LibraryItem
# addition attributes:-issue(String)   :- the issue number or date in the magazine
# override: display_info
# print the detail including the issue
# task:- create instances of each class(Book,Magazine) with appropriate values for their attributes

# call the display_info method  for each instance to test inheritance and method overriding

class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

class Book(LibraryItem):
    def __init__(self, title, author, publication_year, genre, isbn):
        super().__init__(title, author, publication_year)
        self.genre = genre
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print("Genre", self.genre)
        print("ISBN:", self.isbn)

class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

    def display_info(self):
        super().display_info()
        print("Issus", self.issue)

new_book = Book("RodinHood", "John", 2000, "Novel", 34422)
new_book.display_info()
new_mag = Magazine("CEC", "Elon", 2023, "No damages")
new_mag.display_info()
