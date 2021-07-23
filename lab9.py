import time
import random

global blackboard

blackboard = {
    "BATTERY_LEVEL": 100,
    "PLAY_FETCH": 1,
    "FETCH_COUNT": -1,
    "HAPPY": random.randint(0,1)
}

def print_info():
    print("")
    print("**********BLACKBOARD**********")
    for key, value in blackboard.items():
      print("{}: {}".format(key, value))
    print("**********BLACKBOARD**********")
    print("")

class task_status(object):
    FAILURE = 0
    SUCCESS = 1
    RUNNING = 2

class node:
    pass

class task(node):
    pass

class condition(node):
    pass

class composite(node):
    def __init__(self, children):
        self.children = children

class sequence(composite):
    def run(self):
        for n in self.children:
            result = n.run()
            if result == task_status.FAILURE:
                return task_status.FAILURE
            elif result == task_status.RUNNING:
                return task_status.RUNNING
        print("\n")
        return task_status.SUCCESS

class selection(composite):
    def run(self):
        for n in self.children:
            result = n.run()
            if result == task_status.RUNNING:
                return task_status.RUNNING
            elif result == task_status.SUCCESS:
                return task_status.SUCCESS
        print("\n")
        return task_status.FAILURE

class check_battery(condition):
    def run(self):
        if blackboard["BATTERY_LEVEL"] < 30:
            print ("LOW BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")

            return task_status.SUCCESS
        else:
            print ("ENOUGH BATTERY_LEVEL: ", blackboard["BATTERY_LEVEL"], "%")
            return task_status.FAILURE

class check_mood(condition):
    def run(self):
        checkHappiness()
        if blackboard["HAPPY"] == 0 :
            return task_status.SUCCESS
        else:
            return task_status.FAILURE

class play_fetch(condition):
    def run(self):
        if blackboard["PLAY_FETCH"] == 1:
            return task_status.SUCCESS
        else:
            return task_status.FAILURE

class go_home(task):
    def run(self): 
        print("Starting to go home")
        time.sleep(1)
        return task_status.SUCCESS

class rest(task):
    def run(self):
        print("Starting rest")
        time.sleep(3)
        blackboard["BATTERY_LEVEL"] = 100
        print("Battery is now at {} %".format(blackboard["BATTERY_LEVEL"]))
        return task_status.SUCCESS

class askForRubs(task):
    def run(self):
        print("Asking for rubs")
        while blackboard["HAPPY"] == 0:
          if random.randint(0,100) < 75:
            print("Rubs given, robot is happy again :)")
            blackboard["HAPPY"] = 1
          else:
            print("Rubs weren't given :(")
        return task_status.SUCCESS

class done_fetch(task):
    def run(self):
        blackboard["PLAY_FETCH"] = 0
        print("Fetching done")
        return task_status.SUCCESS
    
class fetch(task):
    def __init__(self, cycle):
      self.cycle = cycle

    def run(self):
        print("Fetching...")
        time.sleep(1)
        if blackboard["FETCH_COUNT"] == -1:
            blackboard["FETCH_COUNT"] = self.cycle 
        if blackboard["FETCH_COUNT"] == 0:
            blackboard["PLAY_FETCH"] == 0
            return task_status.SUCCESS
        else:
            print("Played fetch {} times".format(21-(blackboard["FETCH_COUNT"])))
            blackboard["FETCH_COUNT"] -= 1
            time.sleep(1)
            blackboard["BATTERY_LEVEL"] -= 1
            blackboard["HAPPY"] = random.randint(0,1)
            return task_status.RUNNING

class do_nothing(task):
    def run(self):
        print("Doing nothing")
        time.sleep(1)
        return task_status.SUCCESS

def checkHappiness():
  if blackboard["HAPPY"] == 1:
    print("ROBOT IS HAPPY :)")
  else:
    print("ROBOT IS UNHAPPY :(")

root = selection(children = [sequence(children = [check_battery(),
                                                 go_home(),
                                                 rest()]),
                            sequence(children = [check_mood(),
                                                 go_home(),
                                                 askForRubs()]),
                            selection(children = [sequence(children = [play_fetch(),
                                                                       fetch(20),
                                                                       done_fetch()
                                                                       ]),
                                                  do_nothing()]),
                            do_nothing()])

def main():
    CONTINUE_RUNNING = 0
    BATTERY_LEVEL = 0
    PLAY_FETCH = 0

    CONTINUE_RUNNING = int(input("Start the stimulation? (0 = no, 1 = yes)"))

    while (CONTINUE_RUNNING == 1):
        BATTERY_LEVEL = int(input("Current battery level: "))
        PLAY_FETCH = int(input("Play fetch? (0 = no, 1 = yes)"))

        blackboard["BATTERY_LEVEL"] = BATTERY_LEVEL
        blackboard["PLAY_FETCH"] = PLAY_FETCH
        blackboard["FETCH_COUNT"] = -1

        print_info()

        running_success = root.run()

        while (running_success != 1 or blackboard["PLAY_FETCH"] == 1):
            running_success = root.run()

        if (running_success == 1):
            print("All tasks complete!")
            CONTINUE_RUNNING = 0

    print_info()
    print("Thank you")

# run main
if __name__ == "__main__":
	main()


'''
Some questions to answer:
1. Explain in your words, how class inheritance works.
ANSWER: Class inheritance allows the creation of a class or classes that 'inherits' all of the methods and properties of another class (the parent class).

2. Explain in your words, how behavior tree works? How does it relay information between nodes? What information is being passed between nodes?
ANSWER: A behaviour tree is composed of multiple nodes and in this case, the three main types of nodes are task nodes, condition nodes and composite nodes. Task nodes enable the agent to perform a task and return the task status and condition nodes evaluate logical operations and return the boolean results of the operations whereas composite nodes connect different nodes together. One example of a composite node is the sequence node which will return failure as soon as one of its children nodes return failure, another example is the selection node which returns success as soon as one of its children returns success. As demonstrated, only the task state is being passed between nodes. 

3. What does the second while loop in main function do?
ANSWER: It runs the program until the 'main' node returns 1 - indicating a success or PLAY_FETCH is not 1. 

4. What does the "blackboard" do?
ANSWER: It stores all of the global values that the agent can write to and read from. 

5. What is the difference between sequence and selection nodes?
ANSWER: A sequence node will return failure as soon as one of its children nodes return failure whereas a selection node returns success as soon as one of its children returns success.

6. EXTRA CREDIT: be creative and build on top of the finished tree with at least 2 new tasks or condition nodes. 
'''
