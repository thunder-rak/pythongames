from random import randint
table = []
stats = {
    "Munich" : 3.4,
    "Benfica" : 2.6,
    "Dortmund" : 2.1,
    "Leipzig" : 2.0,
}
deff = {
    "PSG" : 0.6,
    "Napoli" : 0.7,
    "Brighton" : 0.6,
    "Atlet" : 0.7,
}
teams = list(stats.keys())
for q in teams:
    stats[q] = (stats[q] + 2) * 30
    deff[q] = (2 - deff[q]) * 50
    stats[q] = int(stats[q])
    deff[q] = int(deff[q])
teams.extend(stats.keys())
gd = 0
points = 0
scores = []
for a in range(4):
    counter = -1
    for q in range(3):
        counter = counter + 1
        team1No = (a + 1)
        team2No = (a + counter + 1)
        if team1No == team2No:
            if team2No == 20:
                team2No = 1
            else:
                team2No = team2No + 1
            counter = counter +1
        team1 = teams[team1No]
        team2 = teams[team2No]
        goal = 0
        team2goals = 0
        team1goals = 0
        for qwe in range(stats[team1] - deff[team2]):
            goal = randint(1, 250 - stats[team1])
            if goal > 0 and goal < 4 :
                team1goals = team1goals + 1
                goal = 0
        for qwe in range(stats[team2]-deff[team1]):
            goal = randint(1, 250 - stats[team1])
            if goal > 0 and goal < 4 :
                team2goals = team2goals + 1
                goal = 0
        score = team1,team1goals,team2goals,team2
        team2goals = 0
        team1goals = 0
        goall = 0
        print(score)
        scores.append(score)
print()
for hj in range(4):
    points = 0
    gd = 0
    goals = 0
    concede = 0
    wins = 0
    loss = 0
    draw = 0
    tea = teams[hj]
    for x in scores:
        if tea in x:
            if x[1] > x[2]:
                if x.index(tea) == 3:
                    loss = loss + 1
                    goals = goals + x[2]
                    concede = concede + x[1]
                    gd = gd + (x[2] - x[1])
                else:
                    wins = wins + 1
                    goals = goals + x[1]
                    concede = concede + x[2]
                    gd = gd + (x[1] - x[2])
                    points = points + 3
            elif x[1] == x[2]:
                draw = draw + 1
                goals = goals + x[2]
                concede = concede + x[1]
                points = points + 1
            else:
                if x[1] < x[2]:
                    if x.index(tea) == 3:
                        wins = wins + 1
                        goals = goals + x[2]
                        concede = concede + x[1]
                        points = points + 3
                        gd = gd + (x[2] - x[1])
                    else:
                        loss = loss + 1
                        goals = goals + x[1]
                        concede = concede + x[2]
                        gd = gd + (x[1] - x[2])
    DD = points, gd, goals, concede, wins, draw, loss, tea
    table.append(DD)
table.sort()
table.reverse()
print('   P  GD   G   GC   W  D  L   Team')
print()
for k in table:
    print(table.index(k)+1, k)
    print()