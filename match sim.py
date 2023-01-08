from random import randint
att1 = float(input('attack for team 1: '))
def1 = float(input('defence for team 1: '))
att2 = float(input('attack for team 2: '))
def2 = float(input('defence for team 2: '))
att1 = (att1+2) * 30
att2 = (att2+2) * 30
def1 = (2-def1) * 50
def2 = (2-def2) * 50
att1 = int(att1)
att2 = int(att2)
def1 = int(def1)
def2 = int(def2)
team1goals = 0
team2goals = 0
goal1 = 0
goal2 = 0
win1 = 0
win2 = 0
points = 0
for ghjbgb in range(10000):
 for qwe in range(att1 - def2):
    goal = randint(1, 260 - att1)
    if goal > 0 and goal < 4 :
        team1goals = team1goals + 1
        goal = 0
 for qwe in range(att2-def1):
    goal = randint(1, 260 - att2)
    if goal > 0 and goal < 4 :
        team2goals = team2goals + 1
        goal = 0
 if team1goals > team2goals:
     win1 = win1 + 1
     points = points+3
 elif team2goals > team1goals:
     win2 = win2 + 1
 else:
     points = points+1

 goal1 = goal1 + team1goals
 goal2 = goal2 + team2goals
 print(team1goals,':',team2goals)
 team1goals = 0
 team2goals = 0
print(round(win1/100), '% win for team 1')
print(round(win2/100), '% win for team 2')
print(100 - round(win1/100) - round(win2/100), '% draw')
print(round(goal1/10000,1),':',round(goal2/10000,1))
print(round(points/300))