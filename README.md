# 1. Basic Functions 
# *Anatomy of a Function*
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

you dont use append in tuple. you will get this error AttributeError: 'tuple' object has no attribute 'append'.

# 2. Clases and Objects Fundamentals
# *Anatomy of a Class*

# Instance and Static Methods

One of your favorite things to do in Python may be string parsing. To demonstrate, create a class called Word Set that contains a set of words. 

- Start with an empty set and add to it by passing in big blocks of text, punctuation and all. 
- Add text using the method add text, which first calls the method clean text to remove the punctuation and make everything lowercase. 
- Then use the split function to turn the sentence into a list of words, which can be added to the set. 
- Finally, print the set of words. 

*what is super() used for inside a class?* is to get an instance of the parrent class
you dont use append in tuple. you will get this error AttributeError: 'tuple' object has no attribute 'append'.

*why is the self variable used inside a class?* - It's the conventional variable name to refer to the class instance


# 3.Error Handling Fundamentals
# *Handling Error and Exceptions*
Remember that thing that occurs when something is divided by zero? it results in zero division error. *Note* Additionally, it's important to write clear code and pay attention to your program's structure to avoid excessive debugging difficulties.
- Try/Except - The try block lets you test a block of code for errors. The except block lets you handle the error.
- finally - Finally statements can be useful because they will always execute no matter what happens inside this try block.
- Catching Exceptions by Type -  
- Custom Decorators - allows you to modify or extend the behavior of functions or methods without changing their actual code. *custom decoratiors cannot change the name of a function*
- Raising Exception -  

# 4. Threads and Processes Fundamentals
# *Multithreading*
For instance, waiting to fetch data from a remote server, the code is just sitting around doing nothing, waiting for that data to come back, and this is where threads are so handy. You can do all that waiting in parallel rather than one at a time. 

To demonstrate this, make two threads:

- t1 is threading.thread and nd 
- t2 is threading.thread. 
Pass in two keyword arguments. The first one is called target, and that's the name of the target function, longSquare. The second is called args. That's going to be the arguments we pass to the function. Copy this and put it there followed by a comma just to show Python that it is a tuple and not a random variable with parentheses around it. If you only have one value in the tuple, sometimes that is necessary. 
- threads shares the same space in memory.

# Multiprocessing
From multiprocessing import Process. Before you run this, there is a small hitch with using the official Python multiprocessing module. The multiprocess module has all of the same functions and is used exactly the same as multiprocessing but it does not have the bug with pickiness about where the function is defined. So play around with it, and use either of them for these examples, but we are going to use multiprocess and also import the time module. 
- Processes can contain multiple threads.
- good way to collect output from multiple processes by writing the results to a file.

# 5. Fundamentals of Wrking with Files
- *Reading Files* - 
- *Writing files* - 
- *Appending Files* -
- *CSV* -  

