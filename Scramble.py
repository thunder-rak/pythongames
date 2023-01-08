import random
text = input('text:  ')
b = ''
text = text.upper()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = alpha.upper()
for a in text:
    if a in alpha:
        b = b + a


text = b
print(text)
alp = []
for s in alpha:
    alp.append(s)
code = ''
for q in alpha:
    x = random.choice(alp)
    code = code + x
    alp.remove(x)
new = ''
for t in text:
    t = code[alpha.index(t)]
    new = new + t
print(new)