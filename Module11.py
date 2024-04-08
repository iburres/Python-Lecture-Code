'''
     Module 11 - Inheritance
'''
# three advantages to writing code in OOP:  Modular, Code reuse, more secure
# Player class -> wizards, fighters, thieves.
# Enemy class -> dragons, orcs, (Alyssas) Titan....

# Inheritance: A way to form new classes using classes that have already been defined.
# Some keywords to know:
#   - base class: The class that is being inherited from (also called parent class or superclass).
#   - derived class: The class that is inheriting from another class (also called child class or subclass).

# Banking Class - Superclass ->  routing number checking number
# Checking Class - subclass of Banking Class, direct deposit
# Savings Class - subclass of Banking Class, transfer
# Zelle - subclass of Banking Class, send money over the wire retrieve the remote routing number and checking number via telephone number associated with the remote account

# Syntax:
#   class BaseClass:
#       Body of base class
#   class DerivedClass(BaseClass):

# Example:
class Animal:
    def __init__(self, name, age):
        self.name = name #public or non-hidden attribute
        self.age = age

    def speak(self):
        print(f'{self.name} is speaking')
        
class Dog(Animal): #subclass inherits from superclass
    def __init__(self, name, age, breed):
        super().__init__(name, age) # super() is used to call the __init__ method of the base class.  
        self.breed = breed

    #overriding
    def speak(self):
        print(f'{self.name} is barking')
        
    
        
class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        
    def setMake(self, make):
        self.__make = make
    
    def setModel(self, model):
        self.__model = model
        
    def setYear(self, year):
        self.__year = year
        
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getYear(self):
        return self.__year
        
    def display_info(self):
        print(f'{self.__year} {self.__make} {self.__model}')
        
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.__doors = doors
        
    def display_info(self):
        print(f'{self._Vehicle__year} {self._Vehicle__make} {self._Vehicle__model} with {self.__doors} doors')
        
        
if __name__ == '__main__':
    animal = Animal('Animal', 10)
    animal.speak()
    
    dog = Dog('Max', 5, 'German Shepherd')
    dog.speak()
    
    #creating an object of the Car class
    vehicle = Vehicle('Ford', 'F-250', 2021) #try putting a 4 here and you'll see the error code that is generated.
    vehicle.display_info()
    car = Car('Toyota', 'Corolla', 2015, 4)
    car.display_info()
    car.setMake('Honda') # this will change the make of the car
    car.display_info()
    
    #multiple inheritance means a class can inherit from more than one class. There is no limit on the number of classes a class can inherit from.
    
    #The four pillars of OOP are:
    #1. Encapsulation - contained within, like a cube.  Contains the class the object was derived from, it's attributes, and contructors/init methodds, and any methods. 
    #2. Abstraction - We hide the underlying parts that are not necessary to use the product/program.
    #3. Polymorphism - poly means multiple and morph - to change.  Multiple forms. 
    # Inheritance - extending the base attributes and methods of the supercalss to the subclass, with the addition of unique attributes associated with the subclass.
    
    
    