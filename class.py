# Base Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Derived Class (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def describe(self):
        return f"E-Book: '{self.title}' by {self.author}, {self.pages} pages, {self.file_size}MB file size"

# Example Usage
book1 = Book("Python 101", "John Doe", 300)
ebook1 = EBook("Advanced Python", "Jane Smith", 450, 5)

print(book1.describe())
print(ebook1.describe())











# polymorhism assignment


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example of Polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
