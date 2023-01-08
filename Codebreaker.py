import random
list = []
code = ''
for a in range(10):
    list.append(str(a))
for s in range(4):
    randol = random.choice(list)
    code = code + randol
    list.remove(randol)
lives = 12
user = ''
while lives > 0 and user != code:
    correct = 0
    wrong = 0
    user = input('code: ')
    for w in range(4):
        if user[w] == code[w]:
            correct = correct +1
    for q in code:
        for t in user:
            if q == t:
                wrong = wrong + 1
    wrong = wrong - correct
    print('+',correct)
    print('-',wrong)
    lives = lives - 1
    print('tries left: ',lives)
if user == code:
    print('nice u got it')
else:
    print('fail')