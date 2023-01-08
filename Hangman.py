word = list('carcharodontosauruses')
guess = list('')
guesses = list('')
lives = 5
playerGuesses = []
for u in range(len(word)):
    guesses.append('*')
strGuesses = "".join(guesses)
print(strGuesses)
while guesses != word and lives > 0:
    guess = input('letter ')
    check = 0
    for e in playerGuesses:
        if e == guess:
            check = check + 1
    correct = 0
    playerGuesses.append(guess)
    for o in range(len(word)):
        if guess == word[o]:
            guesses[o] = word[o]
            correct = correct + 1
    strGuesses = "".join(guesses)
    if correct == 0 or check > 0:
        lives = lives - 1
    print(strGuesses)
    print('you have ',lives,' lives left')
if lives == 0:
    print('fail')
else:
    print('nice job!')