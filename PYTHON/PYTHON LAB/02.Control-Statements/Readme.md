# List of contents in control statements

1. IF-ELSE STATEMENTS
2. INDENTATION
3. PYTHON LOOPS

### INDENTATION

For the ease of programming and to achieve simplicity, python doesn't allow the use of parentheses for the block level code.

In Python, indentation is used to declare a block. If two statements are at the same indentation level, then they are the part of the same block.

Generally, four spaces are given to indent the statements which are a typical amount of indentation in python.

Indentation is the most used part of the python language since it declares the block of code. All the statements of one block are intended at the same level indentation. We will see how the actual indentation takes place in decision making and other stuff in python.

### IF-ELSE STATEMENTS

**IF STATEMENT -** if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed.

![Python If-else statements](https://static.javatpoint.com/python/images/python-if-statement.png)

```
SYNTAX:

if expression:
   statement
```

for more examples regarding if statement refer "CONTROL STATEMENTS" folder

**IF-ELSE STATEMENT -** if-else statement is similar to if statement except the fact that, it also provides the block of the code for the false case of the condition to be checked. If the condition provided in the if statement is false, then the else statement will be executed

![Python If-else statements](https://static.javatpoint.com/python/images/python-if-else-statement.png)

```
SYNTAX:

if condition:
    # block of statements
else:
    # another block of statements
```

for more examples regarding if-else statement refer "CONTROL STATEMENTS" folder

**NESTED IF STATEMENT -** Nested if statements enable us to use if ? else statement inside an outer if statement.

**ELIF STATEMENT**

![Python If-else statements](https://static.javatpoint.com/python/images/python-elif-statement.png)

The elif statement enables us to check multiple conditions and execute the specific block of statements depending upon the true condition among them. We can have any number of elif statements in our program depending upon our need. However, using elif is optional.

The elif statement works like an if-else-if ladder statement in C. It must be succeeded by an if statement.

```
SYNTAX:

if expression 1:
    # block of statements
elif expression 2:
    # block of statements
elif expression 3:
    # block of statements
else:
    # block of statements
```

for more examples regarding elif statement refer "CONTROL STATEMENTS" folder

### PYTHON LOOPS

We can run a single statement or set of statements repeatedly using a loop command

**FOR LOOP** - This type of loop executes a code block multiple times and abbreviates the code that manages the loop variable.

**WHILE LOOP** - Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body

**NESTED LOOP** - We can iterate a loop inside another loop.

#### FOR LOOP

Python's for loop is designed to repeatedly execute a code block while iterating through a list, tuple, dictionary, or other iterable objects of Python.

The process of traversing a sequence is known as iteration.

In this case, the variable value is used to hold the value of every item present in the sequence before the iteration begins until this particular iteration is completed.

Loop iterates until the final item of the sequence are reached.

SYNTAX:

```
for value in sequence:
    { code  block }
```

DECISION CONTROL STATEMENTS WITH FOR LOOP

for loop executes the code block until the sequence element is reached. The statement is written right after the for loop is executed after the execution of the for loop is complete.

Only if the execution is complete does the else statement comes into play. It won't be executed if we exit the loop or if an error is thrown.

SYNTAX:

```
# if-else statement with for loop

for value in sequence:
   if condition:
	# condition TRUE then this block of statement will execute
   else:
	# condition FALSE then this block of statement will execute
```

```
# else statement with for loop

for value in sequence:
	# executes these statements until sequences are exhausted
else:
	# executes these statements when for loop is completed
```

**RANGE FUNCTION USING FOR LOOP**

range() function, we may produce a series of numbers. range(10) will produce values between 0 and 9. (10 numbers).

We can give specific start, stop, and step size values in the manner range(start, stop, step size). If the step size is not specified, it defaults to 1.

Since it doesn't create every value it "contains" after we construct it, the range object can be characterized as being "slow." It does provide in, len, and __getitem__ actions, but it is not an iterator.

for more examples regarding for loop refer "CONTROL STATEMENTS" folder

#### WHILE LOOP

The Python while loop iteration of a code block is executed as long as the given condition, i.e., conditional_expression, is true.

If we don't know how many times we'll execute the iteration ahead of time, we can write an indefinite loop.

SYNTAX

```
while conditional_expression:
   code block of while
```

The given condition, i.e., conditional_expression, is evaluated initially in the Python while loop. Then, if the conditional expression gives a boolean value True, the while loop statements are executed. The conditional expression is verified again when the complete code block is executed. This procedure repeatedly occurs until the conditional expression returns the boolean value False.

* The statements of the Python while loop are dictated by indentation.
* The code block begins when a statement is indented & ends with the very first unindented statement.
* Any non-zero number in Python is interpreted as boolean True. False is interpreted as None and 0.

EXAMPLE

```
# Program to print first 5 natural numbers

n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1

```

**CODE EXPLANATION** : 

We have used **i** and **n** in the boolean expression. During the loop, **n** remains constant and **i** kind of changes with every loop iteration. So, for every iteration, **i** increments and reaches a value where the boolean expression becomes `false` and the control comes out to the loop.

Programmer has to take care that the while loop breaks at some point in the execution. Else, it may iterate indefinitely, which may not be desired all the times.

WHILE LOOP USING LIST

Elements of list are ordered. So, we can access the elements using index. We will make use of this property to traverse through items of list using while loop.

SYNTAX

```
index = 0
while index < len(myList):
    element = myList[index]
    # statements
    index = index + 1
```

CODE EXPLANATION:

* **element** contains value of the this element in the list. For each iteration, next element in the list is loaded into this variable with the changing index.
* **myList** is the Python List over which we would like to traverse through.
* **statement(s)** are block are set of statement(s) which execute for each of the element in the list.

WHILE LOOP USING TUPLE

for more examples regarding while loop refer "CONTROL STATEMENTS" folder

### LOOP CONTROL STATEMENTS

Statements used to control loops and change the course of iteration are called control statements. All the objects produced within the local scope of the loop are deleted when execution is completed.

**BREAK STATEMENT** - This command terminates the loop's execution and transfers the program's control to the statement next to the loop.

**CONTINUE STATEMENT** - This command skips the current iteration of the loop. The statements following the continue statement are not executed once the Python interpreter reaches the continue statement.

**PASS STATEMENT** - The pass statement is used when a statement is syntactically necessary, but no code is to be executed.
