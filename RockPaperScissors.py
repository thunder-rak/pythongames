import random
print('first to ten wins!')
AIscore = 0
userScore = 0
winsAgainst = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
AIchoices = ["rock", "paper", "scissors"]
while userScore != 10 and AIscore != 10:
    choice = input('rock, paper, scissors?:  ')
    AIchoiceWord = random.choice(AIchoices)
    print('Computer chose: ',AIchoiceWord)
    if AIchoiceWord == choice:
        print('draw')
        AIscore = AIscore + 1
        userScore = userScore + 1
        print('Your Score  ',userScore,':',AIscore,'  computer score')
    else:
        if winsAgainst[choice] == AIchoiceWord:
            print('user wins')
            userScore = userScore + 1
            print('Your Score  ',userScore,':',AIscore,'  computer score')
        else:
            print('computer wins')
            AIscore = AIscore + 1
            print('Your Score  ',userScore,':',AIscore,'  computer score')
if AIscore == 10:
    print('computer wins the game!')
if userScore == 10:
    print('you win the game!')