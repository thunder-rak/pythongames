from array import *
from random import randint
counter = -1
list = []
bigList = []
def hottness(bigger, smaller, distance, responce):
    if distance > bigger and distance < smaller:
        print(responce)
for a in range(11):
    counter = counter + 1
    bigList.append(list)
    list = []
    for b in range(10):
        coor = a,b
        list.append(coor)
for r in bigList:
    for c in r:
        print(c,end = "")
    print()
list = bigList[randint(1, 10)]
hidden = list[randint(0, 9)]
choice3 = 0
while choice3 != hidden:
    choice1 = int(input('Enter y coordinate: '))
    choice2 = int(input('Enter x coordinate: '))
    choice3 = choice1, choice2
    if choice3[0] > hidden[0]:
        y = (choice3[0] - hidden[0])
    else:
        y = (hidden[0] - choice3[0])
    if choice3[1] > hidden[1]:
        x = (choice3[1] - hidden[1])
    else:
        x = (hidden[1] - choice3[1])
    distance = x + y
    hottness(10, 19, distance, 'freezing')
    hottness(6, 11, distance, 'cold')
    hottness(3, 7, distance, 'warm')
    hottness(1, 4, distance, 'hot')
    hottness(0, 2, distance, 'boiling')
print('Well done!')