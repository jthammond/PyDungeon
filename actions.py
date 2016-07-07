import json, os
from random import randrange
import tools
import world_map
import characters
import battle

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']
    
#_____________________________Battle__________________________________
def FIGHT(enemy, character):
    battle.BATTLE(enemy, character)
    return
    
#_____________________________Roll Dice__________________________________
def ROLL(dice):

    if dice == "d4":
        return randrange(1, 4)
    
    if dice == "d6":
        return randrange(1, 6)
    
    if dice == "d8":
        return randrange(1, 8)
    
    if dice == "d10":
        return randrange(1, 10)
    
    if dice == "d12":
        return randrange(1, 12)
    
    if dice == "d20":
        return randrange(1, 20)
    
    if dice == "d100":
        return randrange(1, 100)

#___________________________________Look__________________________________________
def LOOK():
    
    room = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Name']
    desc = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Description']
    exitList = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Exits']
    
    tools.CLEAR_SCREEN()
    print "You are at the %s, %s" % (room, desc)
    if len(exitList) == 1:
        print "There are exits to your %s" % "".join(exitList)
        return
    else:
        print "There are exits to your",
        tools.PRINT_LIST(exitList),
        return

#___________________________________Move__________________________________________
def MOVE(dir):
    exits = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Exits']
    locked = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Lock']
    door_key = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]['Key']
    
    if dir not in exits:
        print "There's not an exit in that direction."
        return
    else:
        if dir == "North":
            character["Loc"] = [character["Loc"][0] - 1, character["Loc"][1]]
            return character["Loc"]
        if dir == "South":
            character["Loc"] = [character["Loc"][0] + 1, character["Loc"][1]]
            return character["Loc"]
        if dir == "East":
            character["Loc"] = [character["Loc"][0], character["Loc"][1] + 1]
            return character["Loc"]
        if dir == "West":
            character["Loc"] = [character["Loc"][0], character["Loc"][1] - 1]
            return character["Loc"]


    return