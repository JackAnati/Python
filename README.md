- *Shortcut to open a new Cell is SHIFT + ENTER in jupyter*
- *Append means to add any new number*

# Variables
- Are containers for stroring data values.
- Type a if a variable names begins with number.

*EXAMPLES OF VARIABLES:-*
- x = 5
- y = "Anati"


# Data Structures
- Are containers for different kinds of data. 
- Allows for the storage of a list of values in a single variable.

# Operators
Operators are symbols or special tokens that are used to perform operations on operands. Operands can be variable, value, and expressions. python supports variours types of operators that allow you to carry out arithmethic, logical, comparison,bitwse, and other operations. 
- They are used to manipulate and perform on data.
- Most familiar type of operator is the arithmentic operator, which is used for mathematical calucation.

TO Concastinate a string in python - you must you '+' operator to add strings together for example '2' + '222' = 2222

# Control Flow
They use If/Else, for loop and while loop statement to control flow in programming. Also allows you to execute a block of code only if a certain condition is met.
- while loop - repeatedly executes a block of code until the condition is satisfied. *For example it check if count is less than or equal to 5*.
- for loop -  is used to repeatedly execute a group of statements as long as the condition is satisfied. *For example used to iterate over a sequence*
- If/Else -  used to execute both the true part and the false part of a given condition. 

# Functions
Is like a machine that  takes inputs and produces outputs. It can be defined using *def* keyword follwed by the function name and arguments in paranthesis.

# Classes and Objects
when you have this error *TypeError:Object() take no arguments*. This error is raised when you do not declare method called __init__ in a class that accepts arguments.


# Ints & Floats
given:  round(14/3,2) comma 2 means the how many numbers must be after the comma.

*Factorial Challenge*
- Given 5!
- Solution 
- 5! = 5*4*3*2*1 = 120
- factorial are only defined for positive integers(including 0). When its a negative integers or 1,2(number with comma) words it will return None.

# Alternative number Types
Example:
- Int(‘100’)		  |	int(‘100’,2)
- = 100				  |   =4
 
- Int(‘101’,2)		                        |		int(‘333’,4)		                         |      int(‘1ab’,16)
- =1*(2**2) + 0*(2**1) + 1*(2**0)           |	    =3*(4**2) + 3(4**1) + 3*(4**0)	             |  	=1*(16**2) + 10*(16**1) +11*(16**1)
- =(1*4) + (0*2) + (1*1)			        |       =(3*16) + (3*4) + (3*1)		                 |      = (1*256) + (10*16) + (11*1)
- = 4+0+1			                        |     	= 48+12+3			                         |     	= 256 + 160 + 11
- =5				                        |       =63                                          |      = 427


# List slicing 
If index says start only it print everithing e.g print myList[1::]. You dont print the end of the index you only print  a number before the end index e.g end-1. pop to remove items from a list

# List
There are two ways to remove items from a list. the first method is called remove(), which removes an item based on its value, not its index. For instance, if we want to remove the value 5 from myList, we can type *myList.remove(5)* and then print myList. The second method to remove items from a list is to use pop(). this method removes and returns the item at the end of the list.

 # Tuples and Sets
 A set is defined using curly brackets like this {}. mySet = list(set(myList)) is used to remove duplicates from a list. Tuple are similar to lists, but they're declared with parentheses() instead of square brackets.

 # Dictionaries
trailing comma - are found at the end of the last key value pair. 
Default dict - you must ipmort defaultdict from collections package.

# list comprehension
A list comprehension allows you to create a for loop in one line while also returning a copy of the list you're iterating over. It also enables you to filter or apply functions to every item in a list. A list comprehension allows you to create a for loop in one line while also returning a copy of the list you're iterating over. It also enables you to filter or apply functions to every item in a list. Introduce you to a new string function called "split". This function allows you to split a string based on a given character or string. For example, let's take the string "myString" which reads "my name is Ryan Mitchell, I live in Boston." If we apply the "split" function to it, we can split the string into two sentences using the period as the delimiter. Now, let's apply the "cleanWord" function to our string using a list comprehension. This will result in a clean list of all the words in the text. If we wanted to filter this list to only include small words, such as those with one or two letters, we could add a condition using the "len" function.

# Basic Control Flow
1, 2, fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16

for n in range(1, 101):
    if n%15 ==0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fuzz')
else:
    if n % 5 == 0:
        print('Buzz')
    else:
        print(n)
