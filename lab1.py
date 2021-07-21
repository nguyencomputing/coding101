''''
Lab #1: Python Basics pt.1 
'''

##################################################################
# Begin part 1 of Lab 1
##################################################################

''' TO DO: Answer the short answer questions.

1. Type in 'type(5)', without the apostrophes, into the shell. What does the output say?
ANSWER: <class 'int'> 

2. Type in 'type(3.14)', without the apostrophes, into the shell. What does the output say?
ANSWER: <class 'float'>

3. Type in 'type("Hello World!")', without the outside apostrophes, into the shell. What does the output say?
ANSWER: <class 'string'>

4. What do you think 'type(10)' would output? Check your answer in the shell.
ANSWER: 'type(10)'

5. What do you think 'type("5.1")' would output? Check your answer in the shell.
ANSWER: 'type("5.1")'

6. Why do you think the output is different when you type 'type(...)' into the console, depending on what the '...' is inside of the parentheses? 
ANSWER: This is because Python automatically assume the data type of the '...' and will print that.

7. Type in 'type(int)', 'type(float)', 'type(str)', each on a new line without the apostrophes, into the shell. What do the outputs say?
ANSWER: <class 'type'>

8. Consider your answers to questions 6 and 7. What do you think 'type(...)' does in Python?
ANSWER: <class 'ellipsis'>

9. Type in the following line into the Python shell, like so:
    >>> "Welcome to Coding " + 101
When you hit enter, you will get an error:
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate str (not "int") to str
Based on the above error, plus your answer to #8, what do you think a "TypeError" is?
ANSWER: This is when a function or operation is unable perform because one of the input values are of an incompatible data type.

10. Type in the following line into the Python shell, like so:
    >>> "Welcome to Coding " + str(101)
When you hit enter, the Python shell will output the following:
    'Welcome to Coding 101'
Now, type in the following line into the Python shell, like so:
    >>> type(str(101))
Notice what the output says. Why do you think the code works now, without any errors?
ANSWER: This is because the value 101 is now a string and can be added to the other string.

'''

##################################################################
# Begin part 2 of Lab 1
##################################################################

print("CALCULATOR MENU - Here are your options: ")
print('''
          1. Add two numbers: (x + y)
          2. Subtract two numbers: (x - y)
          3. Multiply two numbers: (x * y)
          4. Divide two numbers: (x / y)
          5. Raise to a power: (x ^ y)
          6. Modulo: (x % y)
''')
print("Choose a number to proceed, 1-6:")
userChoice = input()
userChoice = int(userChoice)

print("You chose choice number {}".format(userChoice))

print("Enter a whole number for x: ")
x = input()
print("Enter a whole number for y: ")
y = input()

print(f"You chose the value {x} for x.")
print("You chose the value {} for y.".format(y))

x = float(x)
y = float(y)

if (userChoice == 1):
  z = x + y
  print("Adding {} and {} results in {}".format(x,y,z))

if (userChoice == 2):
  z = x - y
  print("Subtracting {} from {} results in {}".format(y,x,z))

if (userChoice == 3):
  z = x * y
  print("Multiplying {} and {} results in {}".format(x,y,z))

if (userChoice == 4):
  z = x / y
  print("Dividing {} by {} results in {}".format(x,y,z))

if (userChoice == 5):
  z = x ** y
  print("Raising {} to the power of {} results in {}".format(x,y,z))

if (userChoice == 6):
  z = x % y
  print("{} modulo {} results in {}".format(x,y,z))

print("Thank you for using the calculator! Goodbye.")


'''
TO DO: Answer the following free-response questions, once you have finished:

9. Notice the repeated lines "if (userChoice == "1")", "if (userChoice == "2")", etc. What do you think this line of code is doing?
ANSWER: It is performing logical operations on the userChoice variable and redirecting the program accordingly; however, as only one choice be picked at a time, there's no need for multiple if statements, this can just be replaced by if,elif,elif,..., else :)

10. Notice how when we ask the user for their inputs to x and y, we ask them for whole numbers. Then, we convert the values for x and y into ints, like so: "int(x)", "int(y)". Recall from the beginning of this file that when we ran "type(3.14)" into the Python shell, that there was a specific type that was outputted. If we wanted our calculator to accept decimal numbers, similar to 3.14, what type do you think we would need to convert x and y to? 
ANSWER: Floats
'''

#######################################
# EXTRA CREDIT (if you finish early)
#
# 11. Try updating the code to reflect the suggested change from short answer response #10. What changes in the output to your code?
#ANSWER: It is also of the float data type.
#
# 12. Add another choice (#6) to the menu - "Modulo two numbers: (x % y)"
#
# 13. Implement code for when the user selects choice #6
#       - This will require another "if (userChoice...)" line
#       - Be careful with indentations. Any code inside of an 'if' statement needs a 'tab' first
#
# 14. Try changing the variable "userChoice" to an int after it's been declared, like so: 
#       - userChoice = input()
#       - userChoice = int(userChoice)
#    When you run the code again, you will get an error. Read the error and think about why you might be having that problem. Explain what you think the problem might be, and speculate as to how you might fix the problem. If you think you know the answer, try fixing it in the code! The CAs will be happy to help you with this too!
#ANSWER: No errors would arise, instead, the program would just completely skip the calculation phase as the new userChoice variable is now an int and does not satisfy any of the if statements.
#######################################
