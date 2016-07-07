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

#___________________________________Get Room Name__________________________________________

def GET_ROOM(dir):
    name = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]["Name"]
    print name

#___________________________________Look__________________________________________
def LOOK():
    
    room = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]["Name"]
    desc = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]["Description"]
    exitList = world_map.Tutorial[character["Loc"][0]][character["Loc"][1]]["Exits"]
    
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
    x = character["Loc"][0]
    y = character["Loc"][1]
    exits = world_map.Tutorial[x][y]["Exits"]
   
    def key_check(x, y):
        doorKey = world_map.Tutorial[x][y]["Key"]
        if doorKey == "":
            character["Loc"] = [x, y]
            return character["Loc"]
        else:
            if doorKey not in character["Inventory"]["Key"]:
                tools.CLEAR_SCREEN()
                print "You can't go that direction yet. Maybe you need a key?"
                return
            else:
                character["Loc"] = [x, y]
                return character["Loc"] 
 
    
    if dir not in exits:
        tools.CLEAR_SCREEN()
        print "There's not an exit in that direction."
        return
    else:
        if dir == "North":
            x = x - 1
            key_check(x, y)
            
        if dir == "South":
            x = x + 1
            key_check(x, y)

        if dir == "East":
            y = y + 1
            key_check(x, y)

        if dir == "West":
            y = y - 1
            key_check(x, y)
    
    return

