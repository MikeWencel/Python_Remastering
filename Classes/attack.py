import random


class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy()
enemy2 = Enemy()
enemy1.getAtk()
enemy2.getAtk()


'''
playerhp = 260
enemyattacklow = 60
enemyattackhigh = 80


while playerhp > 0:
    damage = random.randrange(enemyattacklow,enemyattackhigh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for ", damage, "points of damage Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("You've been teleported for respawn")
    break

'''

