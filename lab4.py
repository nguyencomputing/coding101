# Name:        James
# Program:     RPS

import random
import matplotlib.pyplot as plt

matrix = [[0,2,1],[1,0,2],[2,1,0]]
resultTable = ["Tie","You win!","Computer wins!"]
results = []
choices = {0:"Rock", 1:"Paper", 2:"Scissors"}

while True:
    print("Please enter 0 for Rock, 1 for Paper and 2 for Scissors")
    userChoice = int(input("Please enter your choice: "))
    computerChoice = random.randint(0,2)
    result = matrix[userChoice][computerChoice]
    print("You chose {} and the computer chose {}".format(choices[userChoice],choices[computerChoice]))
    print(resultTable[result])
    results.append(result)
    if input("Please type 'exit' here if you would like to stop playing: ").lower() == "exit":
        resultCounts = [results.count(2),results.count(0),results.count(1)]
        plt.bar(["Loss","Tie","Win"],resultCounts,color=['red','blue','green'])
        plt.title("Your game history")
        print("\n")
        print("You lost {} games, tied {} games and won {} games.".format(resultCounts[0],resultCounts[1],resultCounts[2]))
        break
    print("\n")
