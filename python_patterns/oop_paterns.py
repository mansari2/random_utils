"""
This script provides common Object-Oriented Programming (OOP) patterns in Python.

Patterns Covered:
- Encapsulation (Classes & Attributes)
- Inheritance (Parent & Child Classes)
- Polymorphism (Method Overriding)
- Abstraction (ABC - Abstract Base Classes)
- Composition (Using Objects Inside Other Objects)
- Singleton Pattern (Ensuring a Single Instance)
"""

from abc import ABC, abstractmethod

# 1. Encapsulation (Defining a Class with Private and Public Attributes)
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public Attribute
        self.__balance = balance  # Private Attribute (Encapsulation)
    
    def deposit(self, amount):
        """Public method to deposit money."""
        self.__balance += amount
    
    def get_balance(self):
        """Public method to access private balance."""
        return self.__balance

# 2. Inheritance (Parent & Child Classes)
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# 3. Polymorphism (Method Overriding)
def make_animal_speak(animal):
    return animal.speak()

# 4. Abstraction (Using Abstract Base Classes)
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is moving"

# 5. Composition (Using Objects Inside Other Objects)
class Engine:
    def start(self):
        return "Engine started"

class CarComposition:
    def __init__(self):
        self.engine = Engine()
    
    def start_car(self):
        return self.engine.start()

# 6. Singleton Pattern (Ensuring a Single Instance)
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example Usage (Uncomment to Test)
# account = BankAccount("12345", 1000)
# account.deposit(500)
# print(account.get_balance())  # 1500

# dog = Dog()
# print(make_animal_speak(dog))  # "Woof!"

# car = Car()
# print(car.move())  # "Car is moving"

# my_car = CarComposition()
# print(my_car.start_car())  # "Engine started"

# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)  # True (Same instance)

