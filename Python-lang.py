# -----------------------------------------------------------------------------------------------------------
                                       # Basic programming terminology
                                       
# Program : a set of instructions that a computer can execute to perform a specific task
# Programming language : a formal language used to write programs (e.g., Python, Java, C++, etc.)
# Source code : the code you write "the original code"
# Bytecode : the code that python interpreter understands
# Machine code : the code that the machine understands (binary code)
# Interpreter : a program that translates source code to bytecode and executes it line by line
# Compiler : a program that translates source code to machine code and executes it all at once
# IDE : Integrated Development Environment (e.g., PyCharm, VSCode, Jupyter Notebook, etc.)
# REPL : Read-Eval-Print Loop (e.g., Python shell, IPython shell, etc.)
# Execution time : the time it takes to execute a program
# Syntax error : an error in the syntax of the code (e.g., missing colon, parentheses, etc.)
# Runtime error : an error that occurs during the execution of the program (e.g., division by zero, file not found, etc.)
# Logical error : an error in the logic of the code (e.g., using the wrong operator, incorrect algorithm, etc.)
# Debugging : the process of finding and fixing errors in the code
# Commenting : the process of adding comments to the code to explain what the code does
# Documentation : the process of creating documentation for the code to explain how to use it and what it does
# Version control : the process of managing changes to the code over time (e.g., Git, SVN, etc.)
# Collaboration : the process of working with others to develop code (e.g., pair programming, code reviews, etc.)
# Testing : the process of verifying that the code works as expected (e.g., unit testing, integration testing, etc.)
# Deployment : the process of making the code available for use (e.g., deploying to a server, publishing to a package manager, etc.)
# Maintenance : the process of updating and improving the code over time (e.g., fixing bugs, adding new features, etc.)
# Refactoring : the process of improving the structure and readability of the code without changing its functionality
# Optimization : the process of improving the performance of the code (e.g., reducing execution time, memory usage, etc.)
# Code review : the process of reviewing code written by others to ensure it meets quality standards and best practices
# Best practices : a set of guidelines and recommendations for writing high-quality code (e.g., PEP 8 for Python)
# Design patterns : reusable solutions to common problems in software design (e.g., Singleton, Factory, Observer, etc.)
# Algorithms : a set of steps to solve a specific problem (e.g., sorting algorithms, search algorithms, etc.)
# Data structures : a way of organizing and storing data (e.g., lists, dictionaries, sets, etc.)
# Libraries : a collection of pre-written code that can be used to perform specific tasks (e.g., NumPy, Pandas, Matplotlib, etc.)
# Frameworks : a collection of libraries and tools that provide a structure for developing applications (e.g., Django, Flask, React, etc.)
# APIs : Application Programming Interfaces, a set of rules and protocols for building software applications and enabling communication between different software systems
# IDE : Integrated Development Environment, a software application that provides comprehensive facilities to computer programmers for software development (e.g., PyCharm, VSCode, Jupyter Notebook, etc.)

# Dynamically typed language : a programming language that does not require explicit declaration of variable types (e.g., Python, JavaScript, Ruby, etc.)
# Statically typed language : a programming language that requires explicit declaration of variable types (e.g., Java, C++, etc.)
# Strongly typed language : a programming language that enforces strict type rules and does not allow implicit type conversion (e.g., Python, Java, etc.)
# Weakly typed language : a programming language that allows implicit type conversion and does not enforce strict type rules (e.g., JavaScript, PHP, etc.)

# -----------------------------------------------------------------------------------------------------------

# no need for (;) in python statements unless when writing more than statement in one line

print(" I love "); print("python") # => output: I love python
                                                           
#it's equal to : 
print (" I love") 
print ("python")

# -----------------------------------------------------------------------------------------------------------

                                              # Indentation test
                                              
# Python uses indentation to define blocks of code. Indentation is typically done using 4 spaces.
# Consistent indentation is crucial in Python, as it determines the structure and flow of the code

if True:
    print("true")

# -----------------------------------------------------------------------------------------------------------

                                           # Type () function testing
print(type(10))     # <class 'int'>
print(type(10.5))   # <class 'float'>
print(type("10"))   # <class 'str'>
print(type(True))  # <class 'bool'>
print(type([1, 2, 3, 4]))     # <class 'list'>
print(type((1, 2, 3, 4)))     # <class 'tuple'>
print(type({"one": 1, "two": 2}))  # <class 'dict'>
print(type({1, 2, 3, 4}))     # <class 'set'>
print(type(None))  # <class 'NoneType'>
print(type(print))  # <class 'builtin_function_or_method'>

# -----------------------------------------------------------------------------------------------------------
                                             # Constants                    
# Constants are variables that cannot be changed
# Constants are usually defined at the beginning of a program   
# Constants are usually written in uppercase letters with underscores separating words
# Example:
PI = 3.14
GRAVITY = 9.8   
SPEED_OF_LIGHT = 299792458  # in meters per second
# -----------------------------------------------------------------------------------------------------------

                                             # Variables        
                            # Variable assignment and printing
a = 10
print(a)   # 10

# -----------------------------------------------------------------------------------------------------------


                             # Variable naming conventions
                             
# 1. Variable names must start with a letter (a-z, A-Z) or underscore (_)
# 2. The rest of the name can contain letters, numbers (0-9), or underscores (_)
# 3. Variable names are case-sensitive (myVar, myvar, and MYVAR are different variables)
# 4. Variable names cannot be a reserved keyword (e.g., if, else, while, for, etc.)
# 5. Variable names should not contain spaces or special characters (e.g., !, @, #, $, %, etc.)
# 6. Variable names should be descriptive and meaningful
# 7. Variable names should follow a consistent naming convention (e.g., camelCase, snake_case, PascalCase)
name = " Amera Mahmoud "   # single word => normal case
My_name = "Amera Mahmoud"  # multiple words => camel case
my_name = "Amera Mahmoud"  # multiple words => snake case
myName = "Amera Mahmoud"   # multiple words => pascal case

# -----------------------------------------------------------------------------------------------------------


                                          #Escape Sequence characters
# \n : new line
print("Hello\nWorld")  # output : Hello (new line) World
# \t : tab
print("Hello\tWorld")  # output : Hello (tab) World
# \\ : backslash
print("Hello\\World")  # output : Hello \ World
# \' : single quote
print("Hello\'World")  # output : Hello ' World
# \" : double quote
print("Hello\"World")  # output : Hello " World
# \r : carriage return
print("Hello\rWorld")  # output : World (overtakes Hello)
# \b : backspace
print("Hello\bWorld")  # output : HellWorld (overtakes o)    remove the character before \b
# \f : form feed
print("Hello\fWorld")  # output  : Hello (form feed) World
# \v : vertical tab
print("Hello\vWorld")  # output  : Hello (vertical tab) World

#-----------------------------------------------------------------------------------------------------------

                                                # Concatenation
first_name = "Amera"
last_name = "Mahmoud"
full_name = first_name + " " + last_name
print(full_name)  # output : Amera Mahmoud

#note : you can only concatenate strings with strings, not strings with numbers
print("Hello " + 10)  # TypeError: can only concatenate str (not "int") to str
print("Hello " + str(10))  # output : Hello 10

# -----------------------------------------------------------------------------------------------------------

                                                    # Lists 
# A list is a collection of items that are ordered and changeable. Lists are written with square brackets.
# Lists can contain items of different types (e.g., strings, integers, floats, etc.)
# Lists can be nested (i.e., a list can contain other lists as items)
# Lists are mutable (i.e., you can change, add, and remove items from a list)
# Lists allow duplicate items
# Lists are indexed (i.e., each item in a list has a unique index number)
# Lists are zero-indexed (i.e., the first item in a list has an index of 0)
# Lists support slicing (i.e., you can access a range of items in a list)
# Lists support various methods (e.g., append(), remove(), pop(), sort(), etc.)
# Lists can be iterated (i.e., you can loop through the items in a list)
# Lists can be concatenated (i.e., you can combine two or more lists into one list)
my_list = [1, 2, 3, 4, 5]
print(my_list)  # output : [1, 2, 3, 4, 5]

mixed_list = [1, "two", 3.0, True, [5, 6, 7]]
print(mixed_list)  # output : [1, 'two', 3.0, True, [5, 6, 7]]

# Accessing list items
print(my_list[0])  # output : 1 (first item)    
print(my_list[1])  # output : 2 (second item)
print(my_list[-1])  # output : 5 (last item)
print(my_list[-2])  # output : 4 (second last item)
print(my_list[1:4])  # output : [2, 3, 4] (items from index 1 to index 3)
print(my_list[:3])  # output : [1, 2, 3] (items from index 0 to index 2)
print(my_list[2:])  # output : [3, 4, 5] (items from index 2 to the end)
print(my_list[:])  # output : [1, 2, 3, 4, 5] (all items)   
print(my_list[::2])  # output : [1, 3, 5] (every second item)
print(my_list[1::2])  # output : [2, 4] (every second item starting from index 1)
print(my_list[::-1])  # output : [5, 4, 3, 2, 1] (reversed list)
print(my_list[4:1:-1])  # output : [5, 4, 3] (items from index 4 to index 2 in reverse order)
print(my_list[4:0:-1])  # output : [5, 4, 3, 2] (items from index 4 to index 1 in reverse order)
print(my_list[4::-1])  # output : [5, 4, 3, 2, 1] (items from index 4 to index 0 in reverse order)
print(my_list[-1:-4:-1])  # output : [5, 4, 3] (items from index -1 to index -3 in reverse order)
print(my_list[-1:-5:-1])  # output : [5, 4, 3, 2] (items from index -1 to index -4 in reverse order)
print(my_list[-1::-1])  # output : [5, 4, 3, 2, 1] (items from index -1 to index 0 in reverse order)
print(my_list[-3:-1])  # output : [3, 4] (items from index -3 to index -2)

                                             # list methods
# remember my_list = [1, 2, 3, 4, 5]

#Append : adds an item to the end of the list
my_list.append(6)  # adds 6 to the end of the list
print(my_list)  # output : [1, 2, 3, 4, 5, 6]

#Insert : adds an item at the specified index
my_list.insert(0, 0)  # adds 0 to the beginning of the list
print(my_list)  # output : [0, 1, 2, 3, 4, 5, 6]

#Remove : removes the first occurrence of the specified item from the list
my_list.remove(3)  # removes the first occurrence of 3 from the list
print(my_list)  # output : [0, 1, 2, 4, 5, 6]

#Pop : removes and returns the last item from the list
popped_item = my_list.pop()  # removes and returns the last item from the list
print(popped_item)  # output : 6
print(my_list)  # output : [0, 1, 2, 4, 5]

#Pop with index : removes and returns the item at the specified index
my_list.pop(0)  # removes and returns the item at index 0
print(my_list)  # output : [1, 2, 4, 5]

#Sort : sorts the list in ascending order
my_list.sort()  # sorts the list in ascending order
print(my_list)  # output : [1, 2, 4, 5, 6  ]  (note: 6 was added back for sorting demonstration)

#Sort with reverse order
my_list.reverse()  # reverses the order of the list
print(my_list)  # output : [6, 5, 4, 2, 1]  

#Length : returns the number of items in the list
print(len(my_list))  # output : 5 (number of items in the list)

# min : returns the minimum value in the list
print(min(my_list))  # output : 1 (minimum value in the list)

# max : returns the maximum value in the list
print(max(my_list))  # output : 6 (maximum value in the list)

# sum : sums all the items in the list
print(sum(my_list))  # output : 18 (sum of all items in the list)

# count : counts the number of occurrences of a specific item in the list
print(my_list.count(2))  # output : 1 (number of occurrences of 2 in the list)

# clear : # removes all items from the list
my_list.clear()  
print(my_list)  # output : [] (empty list)

# -----------------------------------------------------------------------------------------------------------

                                                      # Tuples
# A tuple is a collection of items that are ordered and unchangeable. Tuples are written with round brackets.
# Tuples can contain items of different types (e.g., strings, integers, floats, etc.)
# Tuples can be nested (i.e., a tuple can contain other tuples as items)
# Tuples are immutable (i.e., you cannot change, add, or remove items from a tuple)
# Tuples allow duplicate items
# Tuples are indexed (i.e., each item in a tuple has a unique index number)
# Tuples are zero-indexed (i.e., the first item in a tuple has an index of 0)
# Tuples support slicing (i.e., you can access a range of items in a tuple)
# Tuples support various methods (e.g., count(), index(), etc.)
# Tuples can be iterated (i.e., you can loop through the items in a tuple)
# Tuples can be concatenated (i.e., you can combine two or more tuples into one tuple)

# Moral : use lists when you need a mutable collection of items and tuples when you need an immutable collection of items.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # output : (1, 2, 3, 4, 5)

mixed_tuple = (1, "two", 3.0, True, (5, 6, 7))
print(mixed_tuple)  # output : (1, 'two', 3.0, True, (5, 6, 7))

# Accessing tuple items
print(my_tuple[0])  # output : 1 (first item)    
print(my_tuple[1])  # output : 2 (second item)
print(my_tuple[-1])  # output : 5 (last item)


                                             # Tuple methods
# remember my_tuple = (1, 2, 3, 4, 5)

# count : counts the number of occurrences of a specific item in the tuple
print(my_tuple.count(2))  # output : 1 (number of occurrences of 2 in the tuple)

# index : returns the index of the first occurrence of a specific item in the tuple
print(my_tuple.index(3))  # output : 2 (index of the first occurrence of 3 in the tuple)

#-----------------------------------------------------------------------------------------------------------

                                            # Dictionaries
# A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are written with curly brackets.
# Dictionaries can contain items of different types (e.g., strings, integers, floats, etc.)
# Dictionaries are mutable (i.e., you can change, add, and remove items from a dictionary)
# Dictionaries do not allow duplicate keys (i.e., each key in a dictionary must be unique)
# Dictionaries are indexed (i.e., each item in a dictionary has a unique key)   
# Dictionaries are unordered (i.e., the items in a dictionary do not have a specific order)
# Dictionaries support various methods (e.g., keys(), values(), items(), get(), etc.)

my_dict = {"one": 1, "two": 2, "three": 3}
print(my_dict)  # output : {'one': 1, 'two': 2, 'three': 3}

mixed_dict = {"one": 1, "two": "two", "three": 3.0, "four": True, "five": [5, 6, 7]}
print(mixed_dict)  # output : {'one': 1, 'two': 'two', 'three': 3.0, 'four': True, 'five': [5, 6, 7]}

# Accessing dictionary items : by key name or with get() method
print(my_dict["one"])  # output : 1 (value of the key "one")
print(my_dict.get("two"))  # output : 2 (value of the key "two")

# Accessing all keys in the dictionary
print(my_dict.keys())  # output : dict_keys(['one', 'two', 'three'])

# Accessing all values in the dictionary
print(my_dict.values())  # output : dict_values([1, 2, 3])

# Accessing all key-value pairs in the dictionary
print(my_dict.items())  # output : dict_items([('one', 1), ('two', 2), ('three', 3)])


                                       # Dictionary methods
# remember my_dict = {"one": 1, "two": 2, "three": 3}

# get : returns the value of a specific key in the dictionary
print(my_dict.get("two"))  # output : 2 (value of the key "two")
print(my_dict.get("four"))  # output : None (key "four" does not exist in the dictionary)

# update : updates the value of a specific key in the dictionary
my_dict.update({"two": 22})  # updates the value of the key "two" to 22
print(my_dict)  # output : {'one': 1, 'two': 22, 'three': 3}

# pop : removes and returns the value of a specific key in the dictionary
popped_value = my_dict.pop("three")  # removes and returns the value of the key "three"
print(popped_value)  # output : 3
print(my_dict)  # output : {'one': 1, 'two': 22}

# clear : removes all items from the dictionary
my_dict.clear()    
print(my_dict)  # output : {} (empty dictionary)

# -----------------------------------------------------------------------------------------------------------

                                                # Sets
# A set is a collection of items that are unordered, unchangeable (immutable), and unindexed. Sets are written with curly brackets.
# Sets can contain items of different types (e.g., strings, integers, floats, etc.)
# Sets are mutable (i.e., you can add and remove items from a set)
# Sets do not allow duplicate items (i.e., each item in a set must be unique)
# Sets are unordered (i.e., the items in a set do not have a specific order)
# Sets support various methods (e.g., add(), remove(), pop(), clear(), union(), intersection(), difference(), etc.) 

my_set = {1, 2, 3, 4, 5}
print(my_set)  # output : {1, 2, 3, 4, 5}

mixed_set = {1, "two", 3.0, True, (5, 6, 7)}
print(mixed_set)  # output : {1, 3.0, (5, 6, 7), 'two'}  (note: True is considered as 1 in set)

# Accessing set items
# Sets are unordered and unindexed, so you cannot access items in a set by index.
# However, you can check if an item exists in a set using the 'in' keyword.

print(1 in my_set)  # output : True
print(6 in my_set)  # output : False

# You can also iterate through the items in a set using a for loop.
for item in mixed_set:
    print(item) # output : 1 3.0 (5, 6, 7) 'two' (order may vary)
    
                                            # Set methods
# remember my_set = {1, 2, 3, 4, 5}

# add : adds an item to the set
my_set.add(6)
print(my_set)  # output : {1, 2, 3, 4, 5, 6}

# remove : removes a specific item from the set
my_set.remove(6)
print(my_set)  # output : {1, 2, 3, 4, 5}
# note : if the item does not exist in the set, it will raise a KeyError

# discard : removes a specific item from the set
my_set.discard(5)
print(my_set)  # output : {1, 2, 3, 4}
# note : if the item does not exist in the set, it will not raise an error

# pop : removes and returns a random item from the set
popped_item = my_set.pop()
print(popped_item)  # output : 4 (or any other item)
print(my_set)  # output : {1, 2, 3} (or any other combination)
# note : since sets are unordered, you cannot predict which item will be popped

# clear : removes all items from the set
my_set.clear()
print(my_set)  # output : set() (empty set)
# note : the output is 'set()' and not '{}' because '{}' represents an empty dictionary in Python

#union : returns a new set that contains all items from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # output : {1, 2, 3, 4, 5}

# or you can use the '|' operator
union_set = set1 | set2
print(union_set)  # output : {1, 2, 3, 4, 5}

# intersection : returns a new set that contains only the items that are present in both sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # output : {3}
# or you can use the '&' operator
intersection_set = set1 & set2
print(intersection_set)  # output : {3}

# difference : returns a new set that contains only the items that are present in the first set but not in the second set
difference_set = set1.difference(set2)  
print(difference_set)  # output : {1, 2}
# or you can use the '-' operator   
difference_set = set1 - set2
print(difference_set)  # output : {1, 2}

# symmetric_difference : returns a new set that contains only the items that are present in either set, but not in both sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # output : {1, 2, 4, 5}
# or you can use the '^' operator
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # output : {1, 2, 4, 5}

# ------------------------------------------------------------------------------------------------------------------------
# The Moral |                                                                                                             |
#------------                                                                                                             |
#1- Use lists when you need a mutable collection of items and tuples when you need an immutable collection of items.      |
#2- Use dictionaries when you need a collection of key-value pairs and sets when you need a collection of unique items.   |
#3- Use sets when you need to perform mathematical set operations (e.g., union, intersection, difference, etc.)           |  
#4- Use lists when you need to maintain the order of items and sets when the order does not matter.                       |
# -------------------------------------------------------------------------------------------------------------------------


                                                  #loops
                                                  
# you can loop through the items in a set using a for loop or a while loop or do while loop
# loops are used to iterate through a block of code multiple times until a certain condition is met
# loops are used to perform repetitive tasks
# loops can be nested (i.e., a loop can contain another loop)
# loops can be controlled using break and continue statements
# break : exits the loop
# continue : skips the current iteration and moves to the next iteration 
                             
                             #for loop
# for loop : used to iterate through a sequence (e.g., list, tuple, set, string, etc.)
#for loop does not require an index variable
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)  # output : 1 2 3 4 5
# note : the order of the items may vary since sets are unordered

                     #**********************************************
                                 # While loop
# while loop : used to iterate through a block of code as long as a certain condition is met
# while loop requires an index variable
# example : print numbers from 0 to 4
i = 0
while i < 5:
    print(i)  # output : 0 1 2 3 4
    i += 1  
# note : make sure to increment the index variable to avoid infinite loop
                        #********************************************
                               # While loop with else [like do while loop]
# do while loop : used to iterate through a block of code at least once and then as long as a certain condition is met
# do while loop is not available in Python, but you can simulate it using a while loop

# example : print numbers from 0 to 4
i = 0
while True:
    print(i)  # output : 0 1 2 3 4
    i += 1
    if i >= 5:
        break
# note : make sure to include a break statement to avoid infinite loop
                        #********************************************
                                    #Nested loops
# nested loops : a loop inside another loop
# example : print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()
# output :
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20
# 5	10	15	20	25

                        #********************************************

                                          # User input
# input() function is used to take input from the user
name = input("Enter your name: ")
print("Hello, " + name + "!")  # output : Hello, <name>!

age = input("Enter your age: ")
print("You are " + age + " years old.")  # output : You are <age> years old.

# note : input() function always returns a string, so you may need to convert it to the desired type (e.g., int, float, etc.)
age = int(input("Enter your age: "))  # convert input to int
print("You are " + str(age) + " years old.")  # output : You are <age> years old.
# -----------------------------------------------------------------------------------------------------------

                                          # Type conversion
                                          
# Type conversion is the process of converting a value from one type to another
# Python has several built-in functions for type conversion
# common type conversion functions are:
# int() : converts a value to an integer
# float() : converts a value to a float
# str() : converts a value to a string
# bool() : converts a value to a boolean
# list() : converts a value to a list
# tuple() : converts a value to a tuple
# set() : converts a value to a set
# dict() : converts a value to a dictionary
# complex() : converts a value to a complex number
# ord() : converts a character to its ASCII value
# chr() : converts an ASCII value to its corresponding character


#Examples:
print(int(10.5))  # output : 10
print(float(10))  # output : 10.0
print(str(10))  # output : '10'
print(bool(1))  # output : True 
print(bool(0))  # output : False
print(list("hello"))  # output : ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))  # output : (1, 2, 3)
print(set([1, 2, 2, 3]))  # output : {1, 2, 3}
print(dict([("one", 1), ("two", 2)]))  # output : {'one': 1, 'two': 2}
print(complex(1, 2))  # output : (1+2j) 
print(ord('A'))  # output : 65
print(chr(65))  # output : 'A'
# -----------------------------------------------------------------------------------------------------------
                                                       #Conditions
                                                       
# Conditions are used to perform different actions based on different conditions
# Conditions are written using if, elif, and else statements
# if statement : used to test a specific condition
# elif statement : used to test multiple conditions
# else statement : used to execute a block of code if all previous conditions are false
# Conditions can be combined using logical operators (and, or, not)
# and operator : returns True if both conditions are true
# or operator : returns True if at least one condition is true
# not operator : reverses the result of a condition
# Conditions can be nested (i.e., a condition can contain another condition)
# Conditions can be written in a single line using the ternary operator (if-else)
# Ternary operator : a shorthand way of writing an if-else statement
# Syntax of ternary operator: <expression1> if <condition> else <expression2>
# If the condition is true, expression1 is returned, otherwise expression2 is returned

#Exaples:
x = 10
if x > 0:
    print("x is positive")  # output : x is positive
elif x < 0:
    print("x is negative")  # output : x is negative
else:
    print("x is zero")  # output : x is zero
    
    
# Example of logical operators
x = 10  
y = 5
#and operator
if x > 0 and y > 0:
    print("x and y are positive")  # output : x and y are positive
    
#or operator
if x > 0 or y < 0:
    print("x is positive or y is negative")  # output : x is positive or y is negative

#not operator
if not (x > 0):
    print("x is not positive")  # output : x is not positive
else:
    print("x is positive")  # output : x is positive


# Example of nested conditions
x = 10
y = 5
if x > 0:
    if y > 0:
        print("x and y are positive")  # output : x and y are positive
    else:
        print("x is positive and y is not positive")  # output : x is positive and y is not positive    
else:
    print("x is not positive")  # output : x is not positive
    
# Example of ternary operator
x = 10
result = "x is positive" if x > 0 else "x is not positive"
print(result)  # output : x is positive

# -----------------------------------------------------------------------------------------------------------
                                   
                                   # Functions
                                   
# A function is a block of code that performs a specific task
# Functions are defined using the def keyword

def greet(name):
    print("Hello, " + name + "!")
 #calling the function   
greet("Amera")  # output : Hello, Amera!
 
 # Functions can take multiple parameters
def add(a, b):
    return a + b
result = add(10, 5)
print(result)  # output : 15

# Functions can return multiple values
def get_name_and_age():
    name = "Amera"
    age = 25
    return name, age
name, age = get_name_and_age()
print(name)  # output : Amera
print(age)  # output : 25

# Functions can have default parameter values
def greet(name="Guest"):
    print("Hello, " + name + "!")
greet()  # output : Hello, Guest!
greet("Amera")  # output : Hello, Amera!

# Functions can take variable number of arguments using *args and **kwargs
def add(*args):
    return sum(args)
result = add(1, 2, 3, 4, 5)
print(result)  # output : 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))
print_info(name="Amera", age=22, city="Cairo")
# output :
# name: Amera
# age: 22
# city: Cairo

# Functions can be nested (i.e., a function can contain another function)
def outer_function():
    def inner_function():
        print("Hello from inner function!")
    inner_function()
outer_function()  # output : Hello from inner function!

# Functions can be assigned to variables and passed as arguments to other functions
def greet(name):
    print("Hello, " + name + "!")

greet("Amera")  # output : Hello, Amera!
greet_function = greet    # assign function to variable
greet_function("Mahmoud")  # output : Hello, Mahmoud!
def call_function(func, name):
    func(name)
call_function(greet, "Ali")  # output : Hello, Ali!

#Function Packing and Unpacking 
# Packing : the process of collecting multiple arguments into a single variable using *args and **kwargs
def pack_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

pack_arguments(1, 2, 3, name="Amera", age=22)
# output :
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Amera', 'age': 22}

# Unpacking : the process of splitting a single variable into multiple arguments using * and **
def unpack_arguments(a, b, c, name, age):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("name:", name)
    print("age:", age)  
args = (1, 2, 3)
kwargs = {"name": "Amera", "age": 22}
unpack_arguments(*args, **kwargs)
# output :
# a: 1
# b: 2
# c: 3
# name: Amera
# age: 22


#-----------------------------------------------------------------------------------------------------------------------
                                                        # Lambda Function 
                     
 # A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression
 # Lambda functions are defined using the lambda keyword
# Lambda functions are often used as a shorthand way of defining simple functions
# Syntax of lambda function: lambda <arguments>: <expression>   
# Lambda functions are often used in combination with other functions, such as map(), filter(), and reduce()

# Example of a lambda function that adds two numbers                    
add = lambda x, y: x + y
result = add(10, 5)
print(result)  # output : 15

# Example of a lambda function that squares a number
square = lambda x: x ** 2
result = square(5)
print(result)  # output : 25

# Example of a lambda function that checks if a number is even or odd
is_even = lambda x: x % 2 == 0
print(is_even(4))  # output : True
print(is_even(5))  # output : False

#------------------------------------------------------------------------------------------------------------------------
# Practice: Write a script to calculate the sum of numbers 1–100

total = 0
for i in range(1 , 101):
    total += i
print("The sum of numbers from 1 to 100 is:", total)  # output : The sum of numbers from 1 to 100 is: 5050

#----------------------------------------------------------------------------------------------------------------------
