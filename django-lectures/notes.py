# class Circle():
#     pi = 3.14
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius**2*Circle.pi
#
#
#
# myc = Circle(3)
# myc.radius = 100
# print(myc.area())

##Inheritance##

# class Animal():
#     def __init__(self):
#         print("Animal Born!")
#
#     def whoAmI(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         #Animal.__init__(self)
#         print("A Dog is Born!")
#     def eat(self):
#         print("Dog Eating")
#
#     def bark(self):
#         print("woof")
#
# mya = Dog()
# mya.whoAmI()
# mya.eat()
# mya.bark()

##Special Methods

# class Book():
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
#
#     def __del__(self):
#         print("A book is destroyed")
#
# b = Book("Python", "Dharmendra Rathod", 200)
# print(b)
# del b
# try:
#     f = open("simple.txt", 'r')
#     f.write("Test write to simple text!")
# # except IOError:
# except:
#     print("Error: Could not open the file")
# finally:
#     print("I always run!")
#     f.close()
import re
# patterns = ['term1', 'term2']
#
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")
text = 'This is a string with term1, not the other term'

match = re.search('term1', text)
print(type(match))
print(match.start())
print(text[22:27])
