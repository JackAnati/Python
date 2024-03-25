# Anatomy of a Function
- Functions are composed of a name and parameters, which are denoted by the def statement. you must import math before coding. 
 - Named Parameters - If our function has a lot of these optional keyword parameters, it can become confusing to determine their order. Therefore, it may be more clear and easier to read to explicitly state "operation equals multiply". 
- *ARGS - There is a rule when using keyword arguments in Python i.e. they must come after the positional arguments. The order of the first two arguments is important and cannot be changed. However, after these mandatory arguments, the keyword arguments can be in any order.
- **KWARGS - In order to handle keyword arguments, a method called kwargs can be used. Kwags is short for keyword arguments. Print kwargs to see that the keyword arguments are now stored as a dictionary instead of a tuple. This makes sense because keyword arguments have keys and values and can be passed in any order, so a dictionary is a more appropriate data structure for referencing them.

# Variables and Scope
- Locals - Why is it named locals? These are the variable names that are only accessible locally within the function. Remember, variables can be defined by any name within the function definition, and it will be available anywhere within that function. However, trying to reference a variable outside its scope will result in an error. 
- Globals() - Running the code would result in so many items, some of which are Python's pre-built variables that will come in handy when working with classes and packages. 

# Variables as Functions
Variables and functions both have names and data associated with them. in python a function is represented as an object.

# __code__ 
the "code" attribute of python function can be used to confirm that functions are just variables in python.

# Lambda Fuctions
These are a way to represent a function without giving it a variable name.

you dont use append in tuple. you will get this error AttributeError: 'tuple' object has no attribute 'append'.