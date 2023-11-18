from enemy import enemy
from character import *

def fight(character, enemy, ambush):
    turn = character
    print(f'{character.name} has {character.hp}hp left and {enemy.name} has {enemy.hp}hp left')
    while character.hp > 0 and enemy.hp > 0:        
        if ambush == 1:
            if turn == character:
                character.attack(enemy)
                turn = enemy
            else:
                enemy.attack(character)
                turn = character
        else:
            if turn == character:
                character.attack(enemy)
                turn = enemy
            else:
                enemy.attack(character)
                turn = character
        if character.hp < 0: character.hp = 0
        print(f'{character.name} has {character.hp}hp left and {enemy.name} has {enemy.hp}hp left')
    
    if character.hp < 1:
        print("\nThe hero has died ")
        character.experience += enemy.experience
    elif enemy.hp < 1:
        print("\nThe hero has slain their opponent.")
    else:
        pass