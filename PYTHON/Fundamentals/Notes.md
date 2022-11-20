# List of Contents in Python Fundamentals

* MODULES
* COMMENTS
* VARIABLE
* IDENTIFIERS
* KEYWORD
* DATA TYPES
* OPERATORS

### MODULES

A module is a file containing code written by someone else which can be imported and used in our programs

**PIP**  -  It is the package manager for python. you can use pip to install a module on your system

**Types of Modules**

There are two types of modules in python.

1. Build in modules - pre-installed in python
2. External modules - Need to install using pip

### COMMENTS

Comments are used to write something the programmer does not want to execute

Types of comments

There are two types of comments in python

1. Single-Line Comments  - written using [#comment]()
2. Multi-line Comments - written using [&#34;comment&#34;]()

### VARIABLE

A variable is the name given to a memory location in a program or A variable is container to store values

Example

a = 143 b = "Love" c = 90.3

where a,b,c are the variables that store respective data

**Rules of Defining a variable name**

* A variable name contains alphabets, digits, underscores.
* A variable name can only start with alphabet or with an underscore.
* A variable name can't start with a digit
* No whitespaces is allowed to be used-inside a variable name

### IDENTIFIERS

An identifier can denote various entities like variable type, subroutines, labels, functions, packges and so on

Example

a = "Deepak Kumar"

where, a is an identifier or a variable

### KEYWORD

Reserved words in the are known as keywords. They can't be used as variable names as their meaning is already reserved

Code to sell all keywords

`Import keyword #we learn about import fn later

print(keyword.kwlist)`

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

### DATA TYPES

Python is the Dynamic typed language that automatically identifies the type of data for us

Primarily , below are the following data types in python

1. Integers
2. Floating-point numbers
3. String
4. Boolean
5. None

**Integer and Floating-point numbers**

Integers and floating-points are separated by the presence or absence of a decimal point

For instance, 5 is an integer whereas 5.0 is a floating point number

**String**

* Strings are array of bytes representing unicode characters
* A string is a collection of one or more characters put in a single quote, double-quote or triple quote
* In python there is no character data type, a character is a string of length 1 and it is represented by the "str" class

**Boolean**

It is used to store two values i.e, TRUE or FALSE. it is used to test whether the result of an expression is TRUE or FALSE

**None**

It is used to define a null variable

### OPERATORS

Operator is a symbol that performs certain operations

Example : a + b

a, b are the operands and + is an operator

There are seven operations in python

1. **Arithmetic Operators**
   * Unary Plus (+)
   * Unary Subtract (-)
   * Multiplication (*)
   * Division (/) - divide left operator withe the right operator and the result is in float
   * Power(**) - Left operator raised to the power of right operand
   * Floor division(//) - division that results in the whole number
   * Modulus (%) - Remainder of the division of left operand by the right

     Note : Floor division can perform both floating and integral aithmetic. if the arguments are in int type then result in int type, if atleast one argument is float type then result is float type
2. **Assignment and Compound Assignment Operators**
   * Assignement Operator

     The equal(=) is used to assign a value to a variable
   * Compound Assignment Operator

     Combination of Arithmetic and assignment operator is known as compound assignment operator

     Example:

     ```
     x = 5

     '/='

     x /= 5
     print(x)
     ```
3. **Comparison Operators**
   * Comparison Operator always return the boolean value(TRUE/FALSE)
   * (==) is equal to
   * (>) is greater than
   * (<) is less than
   * (!=) is not equal to
   * (>=) greater than or equal to
   * (<=) less than or equal to
4. **Logical Operators**
   * Logical AND - 'and' is used to get two boolean and check whether they are both TRUE. if either or both are not TRUE, then the resultant expression is FALSE
   * Logical OR - 'or' is used to get two boolean and check whether any one of the value is TRUE or FALSE. if either both values are either TRUE or FALSE, then the resultant expression is FALSE
   * Logical NOT - 'Not' is used to invert the boolean, and gets the opposite value
5. **Bitwise Operators**
   * Bitwise AND (&)
   * Bitwise OR (|)
   * Bitwise NOT (^)  or Bitwise compliment(~)
   * Bitwsie left shift operator
   * Bitwsie right shift operator
6. **Identity Operators**
   * These operators are used to check if two values are located on the same part of the memory
   * Two variables that are equal does not implement that they are identical
     1. 'is' - TRUE if operands are equal
     2. 'is not' - TRUE if operands are not equal
7. **Membership Operators**
   We can use membership operators to check the given object is present in the given collection
   * 'IN' - TRUE if the given object is present in the specified location
   * 'NOT IN' - TRUE if the given object is not present in the specified location

**Operator Precedence**

If multiple operators present then which operator will be evaluated first is decided by operator precedence

The following list describes the operator precendence in the python

Priority order

1. ()
2. **
3. _,~
4. *,/,%,//
5. +,-
6. <<,>>
7. &
8. ^
9. !
10. ==,!=,>,<,>=,<=
11. =,+=,-=,*=
12. is, not is
13. in, not in
14. not
15. and
16. or

**Type Casting**
