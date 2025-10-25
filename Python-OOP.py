# Object-Oriented Programming (OOP) Concepts in Python

# What is OOP?
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods.
# It allows for organizing code in a way that is modular, reusable, and easier to maintain.
# OOP is a paradigm or code organization style that is based on the concept of "objects".

# paradigm => a typical example or pattern of something; a model.
# Methods => functions that are defined inside a class and can operate on the data contained within the class.
# Attributes => variables that are defined inside a class and hold data related to the object.
# Python is a multi-paradigm programming language that supports OOP as well as procedural and functional programming styles.
# Procedural Programming => :a programming paradigm that is based on the concept of procedure calls, where code is organized into procedures or functions.
# or: => Structure app as a recipe of step-by-step instructions to be followed.

# Functional Programming => a programming paradigm that treats computation as the evaluation of mathematical functions.
# ---------------------------------------------------------------------------------------------------------------

# Key Concepts of OOP:

# 1. Classes and Objects: A class is a blueprint for creating objects. An object is an instance of a class.

# 2. Inheritance: A mechanism where a new class can inherit properties and methods from an existing class.

# 3. Polymorphism: The ability to present the same interface for different data types.

# 4. Encapsulation: => Hiding the internal state of an object and requiring all interaction to be performed through an object's methods.
# or:=> Restricting direct access to some of an object's components.
# or:=>keeping data (attributes) and the methods that work on that data together inside a class


# 5. Abstraction:=> The concept of hiding the complex implementation details and showing only the essential features of the object.

# :=>it helps in reducing programming complexity and increasing efficiency by allowing the programmer to focus on interactions at a high level without needing to understand the intricate details of the underlying implementation.

# ---------------------------------------------------------------------------------------------------------------
# Note: The difference between Encapsulation and Abstraction:                                                   |
# Encapsulation is about bundling data and methods together and controlling access to the data (protecting it). |
# Abstraction is about hiding unnecessary details and showing only what’s important (simplifying complexity).   |
# ---------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
# Class

# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# Classes encapsulate data for the object and methods to manipulate that data.
# class is defined using the 'class' keyword .
# class name should follow the PascalCase [UpperCamelCase] convention (each word starts with a capital letter, no underscores).
# When creataing a class, it is common to define an __init__ method to initialize the object's attributes.
# Any method starting with double underscores (__) is known as a dunder method or magic method.
# Self parameter : in method definitions refers to the instance of the class itself and must be the first parameter of any method in the class.
# IN python you don't need to define an object with the keyword 'new' like in other OOP languages.

# Syntax to define a class:
# class ClassName:
#     def __init__(self, other_attributes):
#         self.other_attribute = other_attributes

# Example of a class definition:

class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
     # Method to get full name

    def full_name(self):
        return f"{self.f_name} {self.l_name}"


person_one = Person("Amera", "Mahmoud", 22)
print(person_one.full_name(), person_one.age)  # Output: Amera Mahmoud 22

# -----------------------------------------------------------------------------------------------
# Inheritance
# Inheritance is a mechanism where a new class (child class or subclass) can inherit properties and methods from an existing class (parent class or superclass).
# This allows for code reuse and the creation of hierarchical relationships between classes.
# The child class can override or extend the functionality of the parent class.

# Syntax for inheritance:

# class ChildClass(ParentClass):
#     def __init__(self, other_attributes):


class Student (Person):  # note : person class is created in lines[61-71]
    def __init__(self, f_name, l_name, age, student_id):
        # Call the constructor of the parent class
        super().__init__(f_name, l_name, age)
        self.student_id = student_id

    def get_student_info(self):
        return f"Name: {self.full_name()}, Age: {self.age}, Student ID: {self.student_id}"


student_one = Student("Omar", "Ali", 20, "S12345")
# Output: Name: Omar Ali, Age: 20, Student ID: S12345
print(student_one.get_student_info())


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Quick and Important Questions :                                                                                                           |

# 1- What is the difference between Overriding and Overloading?                                                                                               |
# Overriding:=> is when a subclass provides a specific implementation of a method that is already defined in its superclass.
#           :=> when a child class changes the behavior of a method from its parent class                                                                  |
#
# Overloading:=> is when multiple methods in the same scope have the same name but different parameters (different type or number of parameters).          |
# Note: Python does not support method overloading in the traditional sense, but it can be  achieved using default parameters or variable-length arguments.

# ------------------------------------
# 2- what is the difference between polymorphism and method overloading'?
# Polymorphism:The same method name can work differently for different objects.
# Example: draw() works for both Circle and Square, but each draws differently.

# Method Overloading:The same method name can have different versions with different parameters in the same class .
# Example: add(x, y) and add(x, y, z).
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Polymorphism نفس الميثود بس بتعمل وظايف مختلفة ولكن بنفس الاسم
# Polymorphism is the ability to present the same interface for different data types.
# It allows methods to do different things based on the object it is acting upon, even though they share the same name.
#  The same method name can work differently for different objects.

# Example 1 : add() method with different parameters (method overloading concept)
num1 = 10
num2 = 20


def add(x, y):
    print(x + y)


F_name = "Amera"
L_name = "Mahmoud"


def add(f_name, l_name):
    print(f_name + " " + l_name)


# Example 2 : draw() works for both Circle and Square, but each draws differently.

class Circle:
    def draw(self):
        return "Drawing a Circle"


class Square:
    def draw(self):
        return "Drawing a Square"


def render_shape(shape):
    print(shape.draw())


circle = Circle()
square = Square()
render_shape(circle)  # Output: Drawing a Circle
render_shape(square)  # Output: Drawing a Square

# ---------------------------------------------------------------------------------------------------------------
# Encapsulation
# Encapsulation is the concept of hiding the internal state of an object and requiring all interaction to be performed through an object's methods.
# It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
# In Python, encapsulation is implemented using access modifiers: public, protected, and private.

# Public: Attributes and methods are accessible from anywhere.

# Protected: Attributes and methods are accessible within the class and its subclasses (conventionally prefixed with a single underscore _).
#:  فعليا دى مجرد اتفاقية بين المبرمجين انه لما احط علامه [_] ده كده انا بقولك انه بروتيكتيد بس لو جيت تعدل للاسف هيعدل عادى
# Private: Attributes and methods are accessible only within the class (conventionally prefixed with a double underscore __).

# Note : The default access modifier in Python is public.[no need to explicitly declare it as public]

# Example of Encapsulation with different access modifiers:


class Student:
    def __init__(self, name, age, grade):
        self.name = name              # Public attribute
        self._age = age               # Protected attribute " one underscore  ""ممكن يتعدل
        # Private attribute " two underscores "  " مش هيعدل لو جيت تجرب وهيعمل ايرور "
        self.__grade = grade

    def get_grade(self):             # Public method to access private attribute
        return self.__grade

    def set_grade(self, grade):      # Public method to modify private attribute
        self.__grade = grade


student = Student("Omar", 20, "A")
print(student.name)          # Accessing public attribute
print(student._age)         # Accessing protected attribute (not recommended)
print(student.get_grade())  # Accessing private attribute via public method

# ---------------------------------------------------------------------------------------------------------------
# Getter  and Setter   "Related To Encapsulation"
# Getters and Setters are methods used to access and update the value of private attributes in a class.
# A getter method retrieves the value of a private attribute, while a setter method updates the value of a private attribute.
# They provide a controlled way to access and modify private attributes, ensuring encapsulation.

# Example of Getter and Setter methods:


class Person:
    def __init__(self, name, age):
        self.__name = name    # Private attribute
        self.__age = age      # Private attribute

    def get_name(self):      # Getter method for name
        return self.__name

    def set_name(self, name):  # Setter method for name
        self.__name = name

    def get_age(self):       # Getter method for age
        return self.__age

    def set_age(self, age):  # Setter method for age
        if age >= 0:        # Simple validation
            self.__age = age
        else:
            print("Age cannot be negative.")

# ---------------------------------------------------------------------------------------------------------------
            # Property Decorators        "Related To Encapsulation"
# Property decorators in Python are a way to define getter, setter, and deleter methods for class attributes using the @property decorator.
# They allow you to access methods like attributes, providing a more intuitive and cleaner syntax for getting and setting attribute values.
# Using property decorators helps in encapsulating the attribute access and modification logic while keeping the interface simple.

# Example of Property Decorators:


class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    @property
    def radius(self):         # Getter method    "اى ميثود مش بترجع اى حاجه يعنى بتاخد self وبس تقدر تعتبرها property "
        return self.__radius

    @radius.setter
    def radius(self, radius):  # Setter method
        if radius >= 0:      # Simple validation
            self.__radius = radius
        else:
            print("Radius cannot be negative.")
#---------------------------------------------------------------------------------------------------------------

                                             #ABCs : Abstract Base Classes
# Abstract Base Classes (ABCs) in Python are a way to define abstract classes that cannot be instantiated directly.
# They provide a blueprint for other classes to follow, ensuring that derived classes implement specific methods defined in the abstract base class.
# ABCs are defined using the 'abc' module and the 'ABC' class, along with the '@abstractmethod' decorator to declare abstract methods.
# Abstract methods are methods that are declared in the abstract base class but do not have an implementation.
# Derived classes must implement all abstract methods from the abstract base class to be instantiated.  

# Example of Abstract Base Classes:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod      # طالما بقت ابستراكت معنى كده انها المفروض مش خترجع حاجه فا هستخدم pass 
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height) 
    
rect = Rectangle(5, 10)
print("Area:", rect.area())               # Output: Area: 50

print("Perimeter:", rect.perimeter())     # Output: Perimeter: 30
    
# ---------------------------------------------------------------------------------------------------------------
                                            #Virtual Environment in Python OOP

# Virtual environments are a crucial aspect of Python development, especially when working with object-oriented programming (OOP) and managing dependencies.
# They allow developers to create isolated environments for their projects, ensuring that dependencies are managed effectively and do not interfere with each other.

# Key Points about Virtual Environments:

# 1. Isolation: Virtual environments provide a self-contained directory that contains all the necessary executables and libraries for a specific project.
# This isolation helps prevent conflicts between different projects that may require different versions of the same package.

# 2. Dependency Management: With virtual environments, you can easily manage project-specific dependencies using tools like pip.
# Each virtual environment can have its own set of installed packages, making it easier to maintain and update dependencies without affecting other projects.

# 3. Reproducibility: Virtual environments help ensure that your project can be reproduced on different machines or by other developers.
# By using a requirements.txt file, you can specify the exact versions of packages needed for your project, making it easier to set up the environment elsewhere.

# 4. Easy Setup: Creating and managing virtual environments is straightforward with tools like venv (built into Python) or virtualenv.
# These tools allow you to create, activate, and deactivate virtual environments with simple commands.

# Example of Creating and Using a Virtual Environment:

# 1. Create a Virtual Environment:
# Open a terminal and navigate to your project directory.
# Run the following command to create a virtual environment named "MyEnv":
# python -m venv MyEnv

# 2. Activate the Virtual Environment:
# On Windows:
# MyEnv\Scripts\activate
# On macOS/Linux:
# source MyEnv/bin/activate

# 3. Install Dependencies:
# With the virtual environment activated, you can install packages using pip:
# pip install package_name

# 4. Deactivate the Virtual Environment:
# When you're done working in the virtual environment, you can deactivate it:
# deactivate

# ---------------------------------------------------------------------------------------------------------------------------
                                                  #Modules and Packages in Python OOP
# Modules and packages are essential concepts in Python that help organize and structure code, especially in object-oriented programming (OOP).
# They allow developers to break down complex programs into smaller, manageable, and reusable components.
# Modules: A module is a single Python file that contains definitions of functions, classes, and variables.
# Modules help in organizing code logically and promoting code reuse.

# Packages: A package is a collection of related modules organized in a directory hierarchy.
# Packages allow for a more structured organization of code, making it easier to manage larger projects.

# Example of Creating and Using Modules and Packages:
# 1. Creating a Module:

# Create a file named math_operations.py with the following content:

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
    
# 2. Using the Module:
# In another Python file, you can import and use the math_operations module:


print("Addition:", math_operations.add(5, 3))
print("Subtraction:", math_operations.subtract(5, 3))
print("Multiplication:", math_operations.multiply(5, 3))
print("Division:", math_operations.divide(5, 0))

# 3. Creating a Package:
# Create a directory named geometry with the following structure:
# geometry/
# ├── __init__.py
# ├── shapes.py
# └── calculations.py
# In shapes.py:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
# In calculations.py:
def calculate_area(shape):
    return shape.area()
 
# 4. Using the Package:
from geometry.shapes import Circle, Square
from geometry.calculations import calculate_area

circle = Circle(radius=5)
square = Square(side=4)

print("Circle Area:", calculate_area(circle))
print("Square Area:", calculate_area(square))
# ---------------------------------------------------------------------------------------------------------------

                                     # Modules
                                     