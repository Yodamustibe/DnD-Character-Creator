from math import random as rand
class enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 0
        self.damage = 0


        if self.name == "Litch":
            for i in range(8):
                self.hp += (rand.randint(5,10) + 2)
            self.hp += 15
            self.damage = (rand.randint(10,15)+5)
            self.expeirence = 100
        if self.name == "Troll":
            for i in range(6):
                self.hp += (rand.randint(7,12) + 4)
            self.hp += 12
            self.damage = 10
            self.expeirence = 50
        if self.name == "Goblin":
            for i in range(4):
                self.hp += (rand.randint(2,6) + 1)
            self.hp += 6
            self.damage = 6
            self.expeirence = 25

    def attack(self, h):
        h.hp -= self.damage