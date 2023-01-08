from decimal import Decimal
height = Decimal(input('Your height: '))
mumHeight = Decimal(input('Your mums height: '))
dadHeight = Decimal(input('Your dads height: '))
age = Decimal(input('Your age: '))
gender = input('Your gender(f for female and m for male): ')
if gender == 'f':
    if age >=4 and age<8:
        estimatedChildHeight = 162*height/(age*5+85)
    if age >=8 and age<=14:
        estimatedChildHeight = 162*height/(age*5+90)
    estimatedParentHeight = (dadHeight + mumHeight) / 2 - 6
if gender == 'm':
    if age >=4 and age<8:
        estimatedChildHeight = 174*height/(age*5+85)
    if age >=8 and age<=14:
        estimatedChildHeight = 174*height/(age*5+90)
    estimatedParentHeight = (dadHeight + mumHeight) / 2 + 6
print(round(estimatedChildHeight+estimatedParentHeight)/2)