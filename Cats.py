cats = 2
for a in range(1, 100):
    if a % 5 == 0:
        cats = cats - a / 5
    cats = cats * 2
    print(cats)