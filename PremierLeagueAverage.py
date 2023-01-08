from random import randint
table = []
stats = {
    "Manchester City" : 17,
    "Arsenal" : 16,
    "Brentford" : 13,
    "Tottenham Hotspur" : 16,
    "Newcastle United" : 14,
    "Leeds United" : 14,
    "Chelsea" : 16,
    "Brighton & Hove Albion" : 14,
    "Aston Villa" : 13,
    "Nottingham Forest" : 12,
    "AFC Bournemouth" : 12,
    "Liverpool" : 17,
    "Fulham" : 12,
    "Wolverhampton Wanderers" : 12,
    "Leicester City" : 14,
    "Crystal Palace" : 13,
    "Southampton" : 13,
    "Everton" : 13,
    "West Ham United" : 14,
    "Manchester United" : 15
}
deff = {
    "Manchester City" : 9,
    "Arsenal" : 6,
    "Brentford" : 6,
    "Tottenham Hotspur" : 7,
    "Newcastle United" : 7,
    "Leeds United" : 5,
    "Chelsea" : 8,
    "Brighton & Hove Albion" : 7,
    "Aston Villa" : 6,
    "Nottingham Forest" : 5,
    "AFC Bournemouth" : 5,
    "Liverpool" : 8,
    "Fulham" : 6,
    "Wolverhampton Wanderers" : 7,
    "Leicester City" : 5,
    "Crystal Palace" : 7,
    "Southampton" : 5,
    "Everton" : 5,
    "West Ham United" : 6,
    "Manchester United" : 7
}
teams = list(stats.keys())
teams.extend(stats.keys())
gd = 0
points = 0
scores = []
for rtt in range(300):
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
        for qwe in range(stats[team1]-deff[team2]):
            goall = randint(1, 30 - stats[team1])
            if goall > 0 and goall < 4 :
                team1goals = team1goals + 1
                goall = 0
        for qwe in range(stats[team2]-deff[team1]-1):
            goall = randint(1, 35-stats[team2])
            if goall > 0 and goall < 4 :
                team2goals = team2goals + 1
                goall = 0
        score = team1,team1goals,team2goals,team2
        team2goals = 0
        team1goals = 0
        goall = 0
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
    DD = round(points/300), round(gd/300), tea
    table.append(DD)
table.sort()
table.reverse()
print('   P  GD  Team')
print()
for k in table:
    print(table.index(k)+1, k)
    print()