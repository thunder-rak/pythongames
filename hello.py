from random import randint
table = []
stats = {
    "Manchester City" : 2.9,
    "Arsenal" : 2.3,
    "Brentford" : 1.9,
    "Tottenham Hotspur" : 2.3,
    "Newcastle United" : 2.1,
    "Leeds United" : 1.8,
    "Chelsea" : 2.3,
    "Brighton & Hove Albion" : 2.1,
    "Aston Villa" : 1.8,
    "Nottingham Forest" : 1.5,
    "AFC Bournemouth" : 1.5,
    "Liverpool" : 2.8,
    "Fulham" : 2.0,
    "Wolverhampton Wanderers" : 1.6,
    "Leicester City" : 1.9,
    "Crystal Palace" : 1.7,
    "Southampton" : 1.7,
    "Everton" : 1.6,
    "West Ham United" : 1.9,
    "Manchester United" : 2.3
}
deff = {
    "Manchester City" : 0.3,
    "Arsenal" : 0.7,
    "Brentford" : 1.0,
    "Tottenham Hotspur" : 0.6,
    "Newcastle United" : 0.6,
    "Leeds United" : 1.0,
    "Chelsea" : 0.5,
    "Brighton & Hove Albion" : 0.6,
    "Aston Villa" : 0.8,
    "Nottingham Forest" : 1.2,
    "AFC Bournemouth" : 1.1,
    "Liverpool" : 0.6,
    "Fulham" : 1.1,
    "Wolverhampton Wanderers" : 0.8,
    "Leicester City" : 0.9,
    "Crystal Palace" : 0.8,
    "Southampton" : 1.0,
    "Everton" : 0.9,
    "West Ham United" : 0.6,
    "Manchester United" : 0.8
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
for a in range(20):
    counter = -1
    for q in range(19):
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
         goal = randint(1, 260 - stats[team1])
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
for hj in range(20):
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