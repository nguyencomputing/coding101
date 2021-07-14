''''
Lab #3: Python Basics pt. 3 - Lists

Assigned: 7/14/21
Due:      7/15/21 10:30AM EST
'''

##################################################################
# Begin part 1 of Lab 3
# To answer the questions for part 1, you may need to run 
# code that uses if-statements or while loops in the Python shell. 
# Note that when you try typing in code that requires multiple 
# lines, like while loops, the shell will do the following
# when you type in a while loop, like so: 
# >>> while True:
# ...  
# The '...' means the shell is waiting for you to enter the next 
# line. To do so, hit "Tab", which will indent your code for you,
# and type the line you wish to enter, like so:
# >>> while True:
# ...   print("Loop")
# Hit enter when you've finished coding the line. If you need to
# write another line of code, then do so by hitting 'Tab' again.
# If you're done, hit enter again (as in, twice) to tell the
# Python shell to execute the code. 
# If you get stuck in an infite loop due to your loop never ending,
# hit ctrl+C to break the execution. 
#
# Record your responses below next to "ANSWER:" for each question.
##################################################################
'''
TO DO: Answer the short answer questions. Check your answers with the CAs.
1. Consider the following code:
-------------------------
myList = [1, "one", 2, "two", 3, "three"]
-------------------------
What is the type for myList? If you aren't sure, try using 'type(myList)' in the shell once you have declared and assigned myList with the appropriate elements.
ANSWER: list

2. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.append(5)
-------------------------
What will the code do?
ANSWER: It will add the number 5 to the list at the very end, making it [1, 2, 3, 4, 5]

3. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.pop()
-------------------------
What will the code do?
ANSWER: pop() normally removes the element with the index provided as a parameter to the method but without one, it will just remove the last element from the list

4. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
print(myList[0])
-------------------------
What will the code do?
ANSWER: It will print out the element with the index of 0, ie the integer 1. 

5. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
print(myList[4])
-------------------------
What will the code do? Check the output in your shell.
ANSWER: As the list only has 4 elements, there is no element with the index of 4, this will raise a index error

6. Consider the following code:
-------------------------
myList = [1, "Hello World!", 4.567, False, True]
-------------------------
Is 'myList' a valid list? Why or why not?
ANSWER: It is because a list can contain elements of various data types.

7. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.remove(5)
print(myList)
-------------------------
What does the code do? Will the list print? Please explain what has happened.
ANSWER: A value error would first be raised as the integer 5 does not exist in the list and therefore can not be removed with the remove() method. Then, as the third line is executed, the same exact list will be printed as nothing has been removed. 

8. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.insert(0, 1)
print(myList)
-------------------------
What will the code do? Please provide the output.
ANSWER: It will firstly reasign the list [1, 2, 3, 4] to the variable myList, then insert the integer 1 into position/index 0 in the list and will then print the new myList variable which is [1, 1, 2, 3, 4]

9. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.insert(3, 3.5)
print(myList)
-------------------------
What does the code do? Please provide the output.
ANSWER: It will firstly reasign the list [1, 2, 3, 4] to the variable myList, then insert the float 3.5 into position/index 3 in the list and will then print the new myList variable which is [1, 2, 3, 3.5, 4]

10. Consider the following code output from the shell:
-------------------------
>>> myList = [1, 2, 3, 4]
>>> print(myList[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
-------------------------
Why did we get an error? Explain in your own words.
ANSWER: This is because the list only has a length of 4 and therefore does not contain an element with index 5

11. Note the error in question 9, where we could not access the element at index 5 in our list because our list can only be accessed with an index between 0-3. Now, consider the following code:
-------------------------
myList = [1, 2, 3, 4]
myList.insert(6, 10)
print(myList)
-------------------------
Will this code run, or will we get another error like in question 9? Try explaining in your own words why this code runs or gives an error. 
ANSWER: This code will still run as any number given as the first parameter to the insert() method that is larger than the actual size of the list will just be interpreted as inserting the number provided as the second parameter at the end of the list. 

12. Consider the following code:
-------------------------
myList = [1, 2, 3, 4]
if "1" in myList:
  print("Yes")
else:
  print("No")
-------------------------
What is the output? Why do you think that is the output?
ANSWER: This will output "No" as the string "1" does not exist in the variable myList but rather the integer 1.

'''

##################################################################
# Begin part 2 of Lab 3
# Shopping cart program
# Our program will allow users to create and edit a shopping cart from a given list of grocery items. They can also add or remove items from their list.
#
# Follow the instructions in the comments (look for the TO DO's), 
# and try running your code using the [ Run > ] button at the top 
# of this page. The output to the code you write here will appear 
# in the "Console" tab on the right of the page.
#
# Note that you may need to look for resources on "Python 
# lists" online if you aren't sure where to start. 
##################################################################

print("This program will help you create and modify a shopping cart.")

# Boolean to break out of the menu when the user is done with their list
userIsShopping = True

# List for storing user's shopping list items
shoppingCart = []

# While loop allows us to keep asking the user for their menu choice until they quit
while userIsShopping:
  print("\nShopping cart menu: \n" +
        "(1) Print your shopping cart\n" +
        "(2) Add an item to your shopping cart\n" +
        "(3) Remove an item from your shopping cart\n" +
        "(4) Quit\n" +
        "(5) Print a specific item from your shopping cart")

  userInput = int(input("Enter your choice, 1-4: "))
  print("\n")

  if userInput == 1:
    if len(shoppingCart) == 0:
      print("Your shopping cart is empty")
    else:
      print("Your shopping cart contains:")
      [print("Item #{} - {}".format(shoppingCart.index(item),item)) for item in shoppingCart]
    

  elif userInput == 2:
    print("Enter an item to add to your shopping cart: ")
    item = input().lower()
    shoppingCart.insert(int(input("What number should {} be in your cart? (Please enter a whole number)".format(item))),item)
    print("Added the item {} to your shopping cart.".format(item))

  elif userInput == 3:
    print("Enter an item to remove it from your shopping cart: ")
    item = input().lower()
    if item in shoppingCart:
      shoppingCart.remove(item)
      print("Successfully removed the item {} from your shopping cart!".format(item))
    else:
      print("Couldn't remove the item {} because it's not in your shopping cart!".format(item))
    
  elif userInput == 5:
    while True:
        print("Enter a number from your shopping cart to print the item: ")
        itemPos = int(input())
        if itemPos >= len(shoppingCart):
          print("Sorry, your shopping cart is small than that!")
          print("Please try again")
        else:
          print("Item #{} in your shopping cart is {}".format(itemPos, shoppingCart[itemPos]))
          break
  else:
    userIsShopping = False
  
print("Thank you for using this program.")



###########################
# Extra credit
###########################

'''

Extra credit:

1. Modify your code so the user can specify WHERE (as in, the index) they want to add their new item to their shopping cart, like so:

Your current shopping cart: ["Potatoes", "Carrots", "Juice"]
Type an item to add to your shopping cart:
Apples
What number should this item be in your cart? Enter a whole number:
0
Your new shopping list: ["Apples", "Potatoes", "Carrots", "Juice"]

2. Add another menu option where users can print an individual item from their cart, like so:
MENU
(1) Print your shopping cart
(2) Add an item to your shopping cart
(3) Remove an item from your shopping cart
(4) Quit
(5) Print a specific item from your shopping cart

Then, when users select this option, let them enter an integer value so they can access the element from their shopping cart. If the element is not in the range of the list, tell them. Here's an example:

### Given the cart ["Apples", "Potatoes", "Carrots"], here are potential outputs:

# WHEN THE USER ENTERS AN INCORRECT VALUE:
-----------------------------------------------------------
Enter a number from your shopping cart to print the item: 
5
Sorry, you do not have 5 items in your shopping cart yet.
-----------------------------------------------------------

# WHEN THE USER ENTERS A CORRECT VALUE:
-----------------------------------------------------------
Enter a number from your shopping cart to print the item:
1
Item #1 in your shopping cart is Potatoes
-----------------------------------------------------------


HINT: There is an easy way to write the conditional if you use the function 'len(list)', where 'list' is the name of the your list variable (aka your shopping cart). Look up "Python len() for lists" if you do not know what this function does.
'''
