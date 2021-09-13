#import libraries
import numpy as np
import random
line_sep = '\n~~~~~~~~~~~~~~~~~~\n'
#______________________________________________________________________________________________________

#Define the environment
environment_rows = 6
environment_columns = 6

def print_grid():
    print("  "+" ".join(str(i)for i in range(6)))
    for y in range(6):
        print(str(y) + " " + " ".join(grid[y]))

#______________________________________________________________________________________________________
#Define rewards

rewards = np.full((environment_rows, environment_columns), -1)

#Give items their single character name
item_A = 'A'
item_B = 'B'
item_C = 'C'
item_D = 'D'
item_E = 'E'
item_F = 'F'
item_G = 'G'
item_H = 'H'
item_I = 'I'
item_J = 'J'

#______________________________________________________________________________________________________
#Generate random orders containing items A-J

x = random.randint(1,10)

items = [item_A,item_B, item_C, item_D, item_E, item_F, item_G, item_H, item_I, item_J]
ordered_items = random.sample(items,x)
print(line_sep)

print('Items ordered:',ordered_items)

print (line_sep)

#Define location of agent and shelves with items location and rewards

agentLocation = rewards[0,0] = 0

item_A = 'A'
if item_A in ordered_items:
            rewards [1,1] = 3
else:
    rewards[1,1] = -1

item_B = 'B'
if item_B in ordered_items:
            rewards [2,2] = 3
else:
    rewards[2,2] = -1

item_C = 'C'
if item_C in ordered_items:
            rewards [3,1] = 3
else:
    rewards[3,1] = -1


item_D = 'D'
if item_D in ordered_items:
            rewards [0,2] = 3
else:
    rewards[0,2] = -1


item_E = 'E'
if item_E in ordered_items:
            rewards [2,0] = 3
else:
    rewards[2,0] = -1


item_F = 'F'
if item_F in ordered_items:
            rewards [4,2] = 3
else:
    rewards[4,2] = -1


item_G = 'G'
if item_G in ordered_items:
            rewards [1,4] = 3
else:
    rewards[1,4] = -1


item_H = 'H'
if item_H in ordered_items:
            rewards [4,5] = 3
else:
    rewards[4,5] = -1


item_I = 'I'
if item_I in ordered_items:
            rewards [2,4] = 3
else:
    rewards[2,4] = -1


item_J = 'J'
if item_J in ordered_items:
            rewards [5,3] = 3
else:
    rewards[5,3] = -1

#Define empty shelves locations
empty = {}
empty[0] = [1,3,4,5]
empty[1] = [0,2,3,5]
empty[2] = [1,3,5]
empty[3] = [0,2,3,4,5]
empty[4] = [0,1,3,4]
empty[5] = [0,1,2,4,5]

#Print rewards matrix
for row in rewards:
    print(row)

#______________________________________________________________________________________________________


line_sep = '\n~~~~~~~~~~~~~~~~~~\n'
print (line_sep)

#______________________________________________________________________________________________________

def __init__(self, agentLocation, percept, customerOrder, acutator, randRange):
    self.location = agentLocation
    self.percept = percept
    self.order = customerOrder
    self.orderShelfLocations = []
    self.actuator = actuator
    self.random = randRange
    self.visitedList = []



def setLocation(agentLocation):
    self.location = [0,0]
    self.location = agentLocation


def getLocation():
    return self.location


def setPercept(percept):
    self.percept = percept


def getPercept():
    return self.percept


def addShelfLocation(location):
    self.orderShelfLocations.push(location)


def getNextShelfLocation():
    return self.orderShelfLocations.pop(0)


def getCurrentShelfLocation():
    return self.currentShelf


def setCurrentShelfLocation(location):
    self.currentShelf = location


# how to handle movement
# have a current movement?
def determineAction():
    if (self.percept.onOrderShelf()):
        self.actuator.collectItem()
        self.currentShelf = ""
    if (self.percept.detectShelves() == 0):
        if (len(self.orderShelfLocation) == 0):
            move = self.random(4)
            determineRandomMove(move)
        else:
            if (self.currentShelf != ""):
                self.actuator.move(self.currentShelf)
            else:
                setCurrentShelfLocation(getNextShelfLocation())
                self.actuator.move(self.currentShelf)
    if (self.percept.detectShelves() == 1):
        self.addShelfLocation(self.percept.getShelfLocation())
        self.actuator.move(getNextShelfLocation())
    elif (self.percept.detectShelves() > 1):
        while (self.percept.hasNextShelfLocation):
            self.addShelfLocation(self.percept.getShelfLocation())
        self.actuator.move(getNextShelfLocation())


def determineRandomMove(move):
    if (move == 0):
        self.actuator.left()
    elif (move == 1):
        self.actuator.right()
    elif (move == 2):
        self.actuator.up()
    elif (move == 3):
        self.actuator.down()

print('Agent start location = ', agentLocation)


#______________________________________________________________________________________________________

