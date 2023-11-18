from combat import fight
from enemy import *
import random as rand
import linecache as lc
import math

class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = input("\nHey, what's your name? ")
        self.character_class = input("\n\nWhat class would you like to make your character? Barbarian, Fighter, Wizard, Druid. ")
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_mod = ability_mod_generator(strength)
        self.dexterity_mod = ability_mod_generator(dexterity)
        self.constitution_mod = ability_mod_generator(constitution)
        self.intelligence_mod = ability_mod_generator(intelligence)
        self.wisdom_mod = ability_mod_generator(wisdom)
        self.charisma_mod = ability_mod_generator(charisma)
        self.max_hp = 0
        self.hp = 0
        self.damage = 0
        self.expeirence = 0
        

        while True:
            self.level = int(input("\nPlease select a level, 1 through 20? "))
            if self.level > 0 and self.level < 21:
                break
            else:
                print("Please input a valid number")        

        if self.character_class.lower() == "barbarian": 
            self.damage = rand.randint(1,8) + self.strength_mod
            for i in range(self.level-1):
                self.max_hp += (rand.randint(1,12) + self.constitution_mod)
            self.max_hp += 12
            self.hp = self.max_hp
        elif self.character_class.lower() == "fighter":
            self.damage = rand.randint(1,8) + self.strength_mod
            for i in range(self.level-1):
                self.max_hp += (rand.randint(1,10) + self.constitution_mod)
            self.max_hp += 10
            self.hp = self.max_hp
        elif self.character_class.lower() == "wizard":
            self.damage = rand.randint(4,10) + self.intelligence_mod
            for i in range(self.level-1):
                self.max_hp += (rand.randint(1,6) + self.constitution_mod)
            self.max_hp += 6
            self.hp = self.max_hp
        elif self.character_class.lower() == "druid":
            self.damage = rand.randint(1,8) + self.wisdom_mod
            for i in range(self.level-1):
                self.max_hp += (rand.randint(1,8) + self.constitution_mod)
            self.max_hp += 8
            self.hp = self.max_hp
        else:
            print("Please repeat that.")

    def attack(self, h):
        h.hp -= self.damage

    class Barbarian():
        def __init__(self, level):
            if level > 5:
                #super(damage).damage +=5
                pass

    class Fighter:
        pass

    class Druid:
        pass

    class Wizard:
        pass

def character_generator():
    strength:int
    dexterity:int
    constitution:int
    intelligence:int
    wisdom:int
    charisma:int

    temp_score:int = 0
    scores = []
    rolls = []

    imp = input("How would you like to roll your stats, 4d6, 1d20 or manual? ")
    while True:
        if imp == "4d6":
            for i in range(6):
                for j in range(4):
                    rolls.append(rand.randint(1,6))
                    rolls.sort()
                rolls.pop(0)
                for j in range(len(rolls)):
                    temp_score += rolls[0]
                    rolls.pop(0)
                scores.append(temp_score)
                temp_score = 0
            break
        elif imp == "1d20":
            for i in range(6):
                scores.append(rand.randint(1,20))
            break
        elif imp.lower() == "manual":
            print("\n Please input your six scoes. ")
            while len(scores) != 6:
                imp = int(input("\n"))
                if imp < 21 and imp > 0:
                    scores.append(int(imp))
                else:
                    print("Please enter a valid number")
            break
        else:
            pass

    print(scores)
    print("\nOk, now that we have your scores, it's time to assign them to the their respective abilities. We'll start with strength, which score would you like to represent your strength ie: 1,2,3,4,5,6")
    imp = int(input()) - 1
    strength = scores[imp]
    scores.pop(imp)

    print(scores)
    print("\nNext we'll do dexterity")
    imp = int(input()) - 1
    dexterity = scores[imp]
    scores.pop(imp)

    print(scores)
    print("\nNext we'll do constitution")
    imp = int(input()) - 1
    constitution = scores[imp]
    scores.pop(imp)

    print(scores)
    print("\nNext we'll do intelligence")
    imp = int(input()) - 1
    intelligence = scores[imp]
    scores.pop(imp)

    print(scores)
    print("\nNext we'll do wisdom and then the value not selected will be assigned to charisma")
    imp = int(input()) - 1
    wisdom = scores[imp]
    scores.pop(imp)
    charisma = scores[0]
    scores.pop(0)

    p1 = Character(strength, dexterity, constitution, intelligence, wisdom, charisma)
    dict = vars(p1)
    print(dict)
    combat = input("\n\n Would you like to battle? ")

    if combat == "yes":
        opponent = input("\nWho would you like to fight? Your options are the Goblin, Troll and Litch. ")
        imp = input("\nHave you been ambushed? ")
        ambush = 0
        if imp == "yes":
            ambush = 1
        e1 = enemy(opponent)
        fight(p1, e1, ambush)
        p1.hp = p1.max_hp

    with open("Character_Data.txt", "a") as f:
        f.write(str(dict)+"\n\n")

def ability_mod_generator(temp_score):
    mod = (temp_score - 10)/2
    mod = math.floor(mod)
    return(mod)

def character_viewer():
    with open("Character_Data.txt", "r") as f:
        print(lc.getline("Character_Data.txt", int(input("Which character would you like to see? ")))) # Taking input for which line to print along with printing the line

