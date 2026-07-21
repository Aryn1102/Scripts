class Student:
    def __init__(self, name: str, age:int, marks:int, location:str, DL:bool, college:str):
        self.name = name
        self.age = age
        self.marks = marks
        self.location = location
        self.DL = DL
        self.college = college
    def introduce(self) -> None:
        print(f"My name is {self.name}")
    def greet(self) -> None:
        print(self.name)
    def report(self) -> None:
        print(self.marks)
    def address(self) -> None:
        print(self.location)
    def license(self) -> None:
        print(self.DL)
    def campus(self) -> None:
        print(self.college)

student1 = Student("Raj", 22)
student1.introduce()
student1.greet()
student1.report()
student1.address()
student1.license()
student1.campus()
student2 = Student("Aryan", 21)
student3 = Student("Sishir", 23)
student4 = Student("Aakash", 19)
student5  = Student("Aisha", 18)
student6 = Student("Ash", 20)
student7 = Student("Rohan", 21)
student8 = Student("Mohan", 22)
student9 = Student("Yamin", 24)
student10 = Student("Mathew", 25)

student1.greet()
student2.greet()
student3.greet()
student4.greet()
student5.greet()
student6.greet()
student7.greet()
student8.greet()
student9.greet()
student10.greet()

class Book():
    def __init__(self, title:str, author:str, pages:int):
        self.title = title
        self.author = author
        self.pages = pages

bookk1 = Book("Much ado about nothing", "Shakespeare", 300)
book2 = Book("The tempest", "Shalkespeare", 200)
book3 = Book("To Kill a mocking bird", "harper lee", 450)
book4 = Book("The Great Gatsby", "F. Scott", 250)
book5 = Book("Harry Potter", "J.K. Rowling", 300)

class Car:
    def __init__(self, brand:str, model:str, year:int):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print(f"The {self.brand} {self.model} started in year {self.year}.")

car1 = Car("Ford", "Figo", 2014)
car1.start()
car2 = Car("Renalt", "Duster", 2015)

class Laptop:
    def __init__(self, brand:str):
        self.brand = brand
laptop1 = Laptop("Lenovo")
laptop2 = Laptop("Asus")

class employee:
    def __init__(self, name:str, salary:float):
        self.name = name
        self.salary = salary

class phone:
    def __init__(self, brand:str, storage: str):
        self.brand = brand
        self.storage = storage

class calculator:
    def __init__(self, no1:int, no2:int):
        self.no1 = no1
        self.no2 = no2
    def add(self) -> float:
        return self.no1 + self.no2

calculator1  = calculator(4, 8)
print(calculator1.add())

class BankAccount:
    def __init__(self, balance:float):
        self.balance = balance
    def deposit(self, amount:float) -> None:
        self.balance += amount

class Animal:
    def speak(self):
        print("Sound")
    
class Dog(Animal):
    pass

dog = Dog()
dog.speak()

class Employee:
    def __init__(self, salary:int):
        self.salary  = salary

class Manager(Employee):
    pass

class Intern(Employee):
    pass

intern = Intern(25000)
print(intern.salary)

manager = Manager(50000)
print(manager.salary)

class BankAccount:
    def __init__(self, _balance:float, _owner:str, _account_number:int):
        self._balance = _balance
        self._owner = _owner
        self._account_number = _account_number

    def deposit(self, amount:float):
        self._balance += amount

    def withdraw(self, amount:float):
        self._balance += amount
    
    def transfer(self, account:str, amount:float):
        if self._balance >= amount:
            self._balance -= amount    
            account._balance += amount
    
    def check_balance(self):
        return self._balance
    
account1 = BankAccount("Raj", "12345", 1000)
account2 = BankAccount("Aryan", "67890", 500)

account1.deposit(200)
account1.withdraw(100)
account1.transfer(account2, 300)

account1.check_balance()
account2.check_balance()

class Vehicle:
    def __init__(self, brand:str) -> None:
        self.brand = brand
    
    def start(self) -> None:
        print(f"{self.brand} started")

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk opened")

class Bike(Vehicle):
    pass

car = Car("Ford")
bike = Bike("Yamaha")

car.start()
car.open_trunk()
bike.start()

class Animal:
    def __init__(self, name:str):
        self.name = name
    
    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print("f{self.name} sleeps")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Horse(Animal):
    pass

dog = Dog()

cat = Cat()

horse = Horse()

class Employee:
    def __init__(self, name:str, salary:float):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} works")

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Intern(Employee):
    pass

manager = Manager()

developer = Developer()

intern = Intern()

class Shape:
    def __init__(self, color:str):
        self.color = color

    def display(self):
        print(f"{self.color}")

class circle(Shape):
    pass

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass

class Vehicle:
    def __init__(self, brand:str, year:int):
        self.brand = brand
        self.year = year
    
    def start(self) -> None:
        print(f"{self.brand} starts")

class Car(Vehicle):
    def __init__(self, brand:str, year:int, door:int):
        super().__init__(brand, year)
        self.door = door

class Bike(Vehicle):
    def __init__(self, engine_cc:int):
        self.engine_cc = engine_cc

car = Car("Ford", 2020, 4)

bike = Bike("Yamaha", 2022, 155)

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}")

class Student(Person):
    def __init__(self, name, age, college:str):
        super().__init__(name, age)
        self.college = college
    
    def study(self):
        print(f"I study in {self.college}")

class Teacher(Person):
    def __init__(self, name, age, subject:str):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"teaches {self.subject}")

student = Student("Raj", 22, "JSS")
teacher = Teacher("Sharma", 45, "Python")

student.introduce()
student.study()

teacher.introduce()
teacher.teach()

import math
class Shape:
    def __init__(self):
        pass

    def area(self) -> float:
        print("area not defined")

class Rectangle(Shape):
    def __init__(self, length:float, width:float):
        self.length = length
        self.width = width
    
    def area(self) -> float:
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius

    def area(self) -> float:
        return math.pi*self.radius**2

rectangle = Rectangle(45.0, 25.0)
circle = Circle(22.0)

print(rectangle.area())
print(circle.area())

from abc import ABC, abstractmethod
import pandas as pd

class FileLoader(ABC):

    @abstractmethod
    def open(self) -> str:
        pass

class TextLoader(FileLoader):
    def open(self) -> str:
        return "opening text file..."

class PDFLoader(FileLoader):
    def open(self) -> str:
        return "opening pdf file..."

text = TextLoader()
pdf = PDFLoader()

print(text.open())
print(pdf.open())