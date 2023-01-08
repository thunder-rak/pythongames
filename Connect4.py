list = []
bigList = []
for a in range(10):
    bigList.append(list)
    list = []
    for b in range(8):
       if a == 8:
           list.append('-')
       else:
           list.append(' ')


def printList():
    for r in bigList:
        if bigList.index(r) > 0:
            print('---------------------------------------------')
        for c in r:
            print('|',c,end = " | ")
        print()
    print('------------------------------------------')
printList()
win = 0
goes = 0
XY = {
    1 : 'X',
    2 : 'O'
}
while win == 0:
    print('player ',goes%2 + 1,' slot: ')
    place = int(input())
    place = place - 1
    t = 0
    check = 1
    while check != 0:
        t= t+1
        if bigList[t+1][place] != ' ' and bigList[t][place]  == ' ':
            bigList[t][place] = XY[goes % 2 + 1]
            check = 0
    printList()
    goes = goes + 1
