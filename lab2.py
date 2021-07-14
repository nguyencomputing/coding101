''''
Lab #2: Python Basics pt. 2 - booleans & conditionals

Assigned: 7/13/21
Due:      7/14/21 10:30AM EST

To complete this lab, look for any "TO DO:" statements in this file and follow the instructions. Please ask the CAs for help when needed. Submit your file through replit when you are done.

If working in groups, feel free to check your answers with your classmates. However, do not simply tell someone the answer to any part of the labs! If you are unsure about anything regarding the lab or short answer questions, please talk to to a CA to get clarification.
'''

##################################################################
# Begin part 1 of Lab 1
##################################################################
'''
TO DO: Answer the short answer questions. When you're done with the short answer questions, check your answers with your classmates and/or the CAs.

1. Type in 'not True', without the apostrophes, into the shell. What does the output say?
ANSWER: False

2. Type in 'not False', without the apostrophes, into the shell. What does the output say?
ANSWER: True

3. What do you think the keyword 'not' does in Python?
ANSWER: It reverses a boolean value when placed before one -> i.e: not True => False, not False => True

4. Type in 'True and True', without the apostrophes, into the shell. What does the output say?
ANSWER: True

5. Type in 'True and False', without the apostrophes, into the shell. What does the output say?
ANSWER: False

6. Type in 'False and False', without the apostrophes, into the shell. What does the output say?
ANSWER: False

7. Why do you think your answers to 4, 5, and 6 are different?
ANSWER: Because they are logical operations with different boolean values

8. Type in 'True or True', without the apostrophes, into the shell. What does the output say?
ANSWER: True

9. Type in 'True or False', without the apostrophes, into the shell. What does the output say?
ANSWER: True

10. Type in 'False or False', without the apostrophes, into the shell. What does the output say?
ANSWER: False

11. Why do you think your answers to 8, 9, and 10 are different?
ANSWER: Because they are logical operations with different boolean values but now with OR instead of AND

12. Based on your answers to 7 and 11, what do you think the difference is between the keyword 'and' and the keyword 'or'? Check your answer with the CAs.
ANSWER: AND follows the following logic (where x is the first input and y is the second): 

if not x:
  print(x)
else:
  print(y)

This is captured in the truth table below:

False(1) AND False(1) would result in False(1)
False(1) AND True(0) would result in False(1)
True(0) AND False(1) would result in False(1)
True(0) AND True(0) would result in True(0)

-------------------------------------------------------

Whereas OR follows the logic of: 

if not x:
  print(y)
else:
  print(x)

This is captured in the truth table below:

False(1) OR False(1) would result in False(1)
False(1) OR True(0) would result in True(0)
True(0) OR False(1) would result in True(0)
True(0) OR True(0) would result in True(0)
'''

##################################################################
# Begin part 2 of Lab 2
##################################################################

import random

print("Welcome to the number guessing game!\n")
print('''Select your difficulty: 
        1. Easy mode
        2. Medium mode 
        3. Hard mode\n''')

difficultyLevel = int(input("Enter a difficulty choice, 1-3: "))

if (difficultyLevel == 1):
  secretNumber = random.randint(1, 5)
  print("\nI'm thinking of a number between 1 and 5.")

elif (difficultyLevel == 2):
  secretNumber = random.randint(1, 10)
  print("\nI'm thinking of a number between 1 and 10.")

else:
  secretNumber = random.randint(1, 20)
  print("\nI'm thinking of a number between 1 and 20.")

''' TO DO: In plain English, explain what the code is doing above using the if, elif, and else statements.
ANSWER: The code is performing logical operations on the user input on which difficulty level they want to play at where 1 is the easiest (as they would have to guess a number between 1 and 5), 2 is harder (as they would have to guess a number between 1 and 10) and 3 is the hardest (as they would have to guess a number between 1 and 20).
'''

print("What do you think the number is?")
guess = int(input())

if guess > secretNumber:
  print("Your guess is too high! The correct answer was {}".format(secretNumber))

if guess < secretNumber:
  print("Your guess is too low! The correct answer was {}".format(secretNumber))

if guess == secretNumber:
  print("You guessed correctly!")

''' TO DO: Once you have finished completing the if-statements above, update your code so the program will tell the user what the secretNumber was whenever the user guesses the wrong number, like so:

"Your guess is too low! The correct answer was 4."

When the user guesses the correct number, the program should not tell the user what the correct answer was, as they already know!'''


''' TO DO: Once you have finished updating your code, answer the following question: 

Notice how the if-statements you wrote check if the number is greater than, less than, or equal to. However, you could write the same code using an if, elif, and else statements like I did earlier when checking what the difficultyLevel was that the user chose. How would you modify your code to use an if, elif, and else instead of 3 if-statements? Type your answer here, then check if you're correct with the CAs if you have time:

ANSWER:
if guess > secretNumber:
  print("Your guess is too high! The correct answer was {}".format(secretNumber))

elif guess < secretNumber:
  print("Your guess is too low! The correct answer was {}".format(secretNumber))
else:
  print("You guessed correctly!")
'''
