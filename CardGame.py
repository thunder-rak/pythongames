from random import randint
import random
choice = {1:'attack', 555: 'counter', 2: 'rest'}
percentage = {1: 1, 2: 0}
stamina = {1: -55, 2: 100}
class dinosaur:
    def __init__(self, name, HP, attack, defence,speed, dom):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.dom = dom
trex = dinosaur('T-Rex', 345, 100, 26, 7, 10)
spino = dinosaur('Spinosaurus', 390, 90, 32, 6, 9)
allo = dinosaur('Allosaurus', 330, 75, 24, 8, 8)
ankylo = dinosaur('Ankylosaurus', 270, 80, 46, 4, 7)
carno = dinosaur('Carnotaurus', 300, 80, 20, 8, 6)
tricera = dinosaur('Triceratops', 285, 90, 18, 4, 5)
stego = dinosaur('Stegosaurus', 300, 85, 20, 3, 4)
kentro = dinosaur('Kentrosaurus', 225, 90, 40, 3, 3)
veloci = dinosaur('Velociraptor', 140, 40, 8, 10, 2)
draco = dinosaur('Dracorex', 140, 30, 8, 6, 1)
dinos = [trex,spino,allo,ankylo,carno,tricera,stego,kentro,veloci,draco]
AIdinos = []
playerDinos = []
for q in range(5):
    e = random.choice(dinos)
    playerDinos.append(e)
    dinos.remove(e)
    e = random.choice(dinos)
    AIdinos.append(e)
    dinos.remove(e)
dinos = [trex,spino,allo,ankylo,carno,tricera,stego,kentro,veloci,draco]
def printDeck():
    for w in playerDinos:
        print(playerDinos.index(w)+1,':',w.name,'|HP:',w.HP,'|attack:',w.attack,'| Defence:',w.defence,'| Speed:',w.speed)
while len(AIdinos) > 0 and len(playerDinos) > 0:
    printDeck()
    playerDino = playerDinos[int(input('choose number of dino: '))-1]
    dom = []
    for s in AIdinos:
        dom.append(s.dom)
    dom.sort()
    dom.reverse()
    AIdino = dinos[10-dom[0]]
    print('computer chose: ',AIdino.name)
    AIstamina = 200
    playerStamina = 200
    while AIdino.HP > 0 and playerDino.HP > 0:
        print(AIdino.name, 'has ',AIstamina,' stamina')
        print(playerDino.name, 'has ',playerStamina,' stamina')
        def choose(biggerThan, smallerThan, choice1, choice2, choice3):
            if AIstamina > biggerThan and AIstamina < smallerThan:
                if playerStamina > 130:
                    return choice1
                if playerStamina > 54 and playerStamina < 131:
                    return choice2
                if playerStamina < 55:
                    return choice3
            else:
                return 0
        playerChoice = int(input('1:attack, 2:rest: '))
        if playerStamina + stamina[playerChoice] < 0:
            opop = 0
            while opop == 0:
                print('not allowed')
        AIchoice = 0
        if playerDino.HP < 50 or playerDino.HP < 50:
         AIchoice = choose(130, 667400, 1, 1, 1) + AIchoice
         AIchoice=choose(54, 131, 1, 1, 1)+AIchoice
         AIchoice=choose(-1, 55, 2, 2, 2)+AIchoice
        else:
         AIchoice = choose(130, 667400, 1, 1, 1) + AIchoice
         AIchoice=choose(54, 131, 2, 2, 1)+AIchoice
         AIchoice=choose(-1, 55, 2, 2, 2)+AIchoice
        print('computer chose: ',choice[AIchoice])
        whoFirstPlayer = playerDino.speed * playerStamina
        whoFirstAi = AIdino.speed * AIstamina
        pa = percentage[playerChoice]
        aa = percentage[AIchoice]
        def AIattackFirst():
            playerDino.HP = playerDino.HP - AIdino.attack * (100 - playerDino.defence)/100 * aa
            print(AIdino.name, 'attacked')
            print(playerDino.name, 'has', playerDino.HP, 'HP')
            if playerDino.HP < 1:
              playerDinos.remove(playerDino)
            else:
                AIdino.HP = AIdino.HP - playerDino.attack * (100 - AIdino.defence)/100 * pa
                print(playerDino.name, 'attacked')
                print(AIdino.name, 'has', AIdino.HP, 'HP')
                if AIdino.HP < 1:
                  AIdinos.remove(AIdino)
        def playerAttackFirst():
            AIdino.HP = AIdino.HP - playerDino.attack * (100 - AIdino.defence)/100 * pa
            print(playerDino.name, 'attacked')
            print(AIdino.name, 'has', AIdino.HP, 'HP')
            if AIdino.HP < 1:
                AIdinos.remove(AIdino)
            else:
                playerDino.HP = playerDino.HP - AIdino.attack * (100 - playerDino.defence)/100 * aa
                print(AIdino.name, 'attacked')
                print(playerDino.name, 'has', playerDino.HP, 'HP')
                if playerDino.HP < 1:
                 playerDinos.remove(playerDino)
        if whoFirstAi > whoFirstPlayer:
            AIattackFirst()
        if whoFirstAi < whoFirstPlayer:
            playerAttackFirst()
        if whoFirstAi == whoFirstPlayer:
            random = randint(1, 2)
            if random == 1:
                AIattackFirst()
            else:
                playerAttackFirst()
        playerStamina = playerStamina + stamina[playerChoice]
        AIstamina = AIstamina + stamina[AIchoice]
        if playerStamina > 200:
            playerStamina = 200
        if AIstamina > 200:
            AIstamina = 200
