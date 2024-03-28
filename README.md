- *Shortcut to open a new Cell is SHIFT + ENTER in jupyter*
- *Append means to add any new number*

# Variables
- Are containers for stroring data values.
- Type a if a variable names begins with number.

*EXAMPLES OF VARIABLES:-*
- x = 5
- y = "Anati"

- If we pass A zero value to bool() construtor, it will treat as a boolean False
- Any non-zero value is boolean True

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
- The append() method appends an item to the end of the list. therefore, we cannot pass the index number to it.

 # Tuples and Sets
 A set is defined using curly brackets like this {}. mySet = list(set(myList)) is used to remove duplicates from a list. Tuple are similar to lists, but they're declared with parentheses() instead of square brackets.
 - When we access a tuple using the subscript atuple[start : end] operator, it will always return a tuple. We also call it tuple slicing. (taking a subset of a tuple using the range of indexes).
 The union() method returns a new set with all items from both sets by removing duplicates
- Difference_update() method removes the items that exist in both sets
- .discard method remove item that doen't exist
- set does not allow duplicate items
- issubset() method returns True if all items in the set exists in the specified set, otherwise it return false. use the <= operator
- issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. use the >= operator
- symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets. Meaning: The returned set contains a mix of items that are not present in both sets. use the ^ operator
- The isdisjoint() method returns True if none of the items are present in both sets, otherwise, it returns False.
- The remove() and discard() method removes the specified item from a set.


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

# Notes
- We cannot add strings and numbers together using the + operator. Either we can use the + operator to concatenate strings or add numbers.
- We cannot use float numbers in range() function.
- We can use the else block after the end of for loop and while loop. The else block is used to check the successful execution of a loop. If the loop executed successfully without any issues, the else block executes.
- We can do simultaneous assignments to more than one variable.
- The set is an unordered data structure. Therefore, we cannot access/add/remove its elements by index number.
- The == (Equal To) operator used to compare the values of two objects and The is operator compares the identity of two objects.
- Immutable - means string cannot be changed after  they are created.
- Strings in Python are surrounded by either single quotation marks or double quotation marks. Also, You can create a multiline string using three      quotation marks.
- math.ceil - round a number up to the nearest number. Method returns the smallest integer not less than x.
- math.floor - round a number down ti the nearest number. Method returns the largest not greater than x.
- Nested loop - is a loop within a loop, an inner loop within the body of an outer one.
- In Python, the pass is a null operation. The pass statement is useful when you want to write the pseudo code that you want to implement in the future.
- In Python, any non-zero value or nonempty container is considered TRUE.
- The title() function capitalize() the first letter of every word of the String.
- The capitalize() function converts only a first character to a capital letter and all remaining characters to lowercase.
