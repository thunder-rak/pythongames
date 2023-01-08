list = []
bigList = []
for a in range(4):
    bigList.append(list)
    list = []
    for b in range(3):
        list.append(' ')
def printList():
    for r in bigList:
        if bigList.index(r) > 0:
            print('-----------------')
        for c in r:
            print('|',c,end = " | ")
        print()
    print('-----------------')
printList()
def check(coor1, coor2, coor3):
    if coor1 == coor2 and coor2 == coor3 and coor1 != ' ':
        return (1)
    else:
        return (0)
def checkAll(w):
    w = check(bigList[1][0], bigList[2][0], bigList[3][0]) + w
    w = check(bigList[1][1], bigList[2][1], bigList[3][1]) + w
    w= check(bigList[1][2], bigList[2][2], bigList[3][2])+w
    w=check(bigList[1][0], bigList[1][1], bigList[1][2])+w
    w= check(bigList[2][0], bigList[2][1], bigList[2][2])+w
    w=check(bigList[3][0], bigList[3][1], bigList[3][2])+w
    w=check(bigList[1][0], bigList[2][1], bigList[3][2])+w
    w=check(bigList[1][2], bigList[2][1], bigList[3][0])+w
    return(w)
win = 0
goes = 0
XY = {
    1 : 'X',
    2 : 'O'
}
while win == 0 and goes != 9:
    print('player ',goes%2 + 1,' y coordinate: ')
    y = int(input())
    print('player ',goes%2 + 1,' x coordinate: ')
    x = int(input())
    list = bigList[4-y]
    if list[x-1] != ' ':
        print('not allwed')
        win = 1
    list[x-1] = XY[goes%2 + 1]
    win = checkAll(win)
    printList()
    goes = goes + 1