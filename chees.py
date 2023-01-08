from random import randint
bigList = []
list = []
random = {1: '0', 2: ' '}
for a in range(11):
    bigList.append(list)
    list = []
    for b in range(10):
        list.append(random[randint(1,2)])
for r in bigList:
    for c in r:
        print(c,end = " | ")
    print()
x = 5
y = 5
while bigList[y] != '7':
    bigList[y] = '7'
print()
for r in bigList:
 for c in r:
    print(c,end = " | ")
print()