import timeit

binaryComps = 0

def getData():
  infile = open("states.txt", 'r')

  stateList = []
  popList = []

  line = infile.readline()
  while line != "":
      line = line.strip()
      states, pop = line.split(',')
      stateList = stateList + [states]
      popList = popList + [pop]
      line = infile.readline()

  infile.close()
  return stateList, popList

def getPopLinear(stateList, popList, state):
  comps = 0
  population = -1

  for stateName in stateList:
    comps += 1
    if stateName == state:
      population = popList[stateList.index(stateName)]
      break

  print("Linear Search: comps = {}".format(comps))
  return population

def getPopBinary(stateList, popList, state, top, bottom):
  global binaryComps
  population = -1
  pos = top - bottom // 2
  binaryComps += 1

  if stateList[pos] == state:
    print("Binary Search: comps = {}".format(binaryComps))
    return popList[pos]
  elif stateList[pos] > state:
    return getPopBinary(stateList, popList, state, pos-1, bottom)
  elif stateList[pos] < state:
    return getPopBinary(stateList, popList, state, top, pos+1)
  else:
    return population

  print("Binary Search: comps = {}".format(binaryComps))
  return population

def getPopFaster(statelist, popList, state):
  comps = 0
  population = -1
  statePopDict = {}

  for i in range(len(statelist)):
    statePopDict[statelist[i]] = popList[i]

  population = statePopDict[state]
  print("Faster Search: comps = {}".format(comps))
  return population

def main():
  stateList, popList = getData()

  state = input("Enter a state abbreviation: ")
  
  start = timeit.default_timer()
  populationBinary = int(getPopBinary(stateList, popList, state, len(stateList)-1,0))
  stop = timeit.default_timer()
  binaryTime = stop - start

  startL = timeit.default_timer()
  populationLinear = int(getPopLinear(stateList, popList, state))
  stopL = timeit.default_timer()
  linearTime = stopL - startL

  startF = timeit.default_timer()
  populationFaster = int(getPopFaster(stateList, popList, state))
  stopF = timeit.default_timer()
  fasterTime = stopF - startF

  if populationLinear == -1:
      print("No population provided by getPopLinear()")

  else:
      print("Linear: The population of ", state, " is ", populationLinear)

  if populationBinary == -1:
      print("No population provided by getPopBinary()")

  else:
      print("Binary: The population of ", state, " is ", populationBinary)
 
  if populationFaster == -1:
      print("No population provided by getPopBinary()")

  else:
      print("Faster: The population of ", state, " is ", populationFaster)

  print("Linear search took {} fractional seconds".format(format(linearTime, 'f')))
  print("Binary search took {} fractional seconds".format(format(binaryTime, 'f')))
  print("Faster search took {} fractional seconds".format(format(fasterTime, 'f')))

if __name__ == "__main__":
    main()
        
#Explain the process of Linear Search. When is it better than Binary Search? What is the runtime of it? How does the number of comparisions differ from binary search (Not just greater than or less than, but in terms of mathematical relations)?
#ANSWER: Linear search works by iterating through the list checking every element and this means that the time taken for a linear search algorithm to complete is propotional to the number of elements it has to search to - this can be beneficial if the element being searched for happens to be at the begining of the list or if the list is relatively small already, however, because of this inherent attribute, linear search has the worst-case complexity of O(n) where n is the total number of elements in the list. 

#Explain the process of Binary Search. When can you use binary search? What could you do to the state.txt file to break this function? What is the runtime of it? Explain why this runtime makes sense? (Hint: Think of what binary search is doing at every step)
#ANSWER: On long lists, a binary search algorithm can be much faster than a linear search algorithm as it only has a worst-case complexity of O(log2(n)). With every step the binary search algorithm is effectively halving the number of possible indices where the item belongs. However, it is much more complicated than linear search and would not be nessesary if the number of elements is very small. It would also not work if there isn't a less-than or more-than relationship between the elements. It also requires a sorted list of elements to work effectively as running a binary search algorithm on an unsorted list would be no better than performing linear search on the same list. (theoratically)

#Can you think of solution that is faster than binary search? Implement it! Explain why it is faster, and provide its runtime! (Hint: The solution that I though of changes getData() so feel free to change anything but make sure your other functions work too
#This link may be helpful https://docs.python.org/3/tutorial/datastructures.html
#ANSWER: The solution I came up with is to use dictionaries, this method works by generating a dictionary where the keys are the state names and the values are the population sizes of the various states, this is still slower than the linear search algorithm if the item is located at the begining of the list though. 
