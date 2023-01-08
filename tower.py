across = []
down = []
for a in range(1, 9):
    across.append(a)
    for w in range(2):
        across.append('.')
    down.append(across)
    across = []
across = ['-', '-', '-']
down.append(across)
for r in down:
    for c in r:
        print(c, end=" ")
    print()
aks = 0
while aks != 68460950:
 placeFrom  = int(input('place to move from:'))
 placeTo = int(input('place to move to'))
 check = -1
 while check != 8:
     check = check + 1
     if down[check][placeFrom-1] != '.':
         placeFrom = down[check][placeFrom-1]
         down[check][placeFrom-1] = '.'
         check = 8
 t = -1
 check = 1
 while check != 0:
     t = t + 1
     if down[t+1][placeTo-1] != '.':
         down[t][placeTo-1] = placeFrom
         check = 0

 for r in down:
     for c in r:
         print(c, end=" ")
     print()



