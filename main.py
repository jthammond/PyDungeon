import characters
import battle
import world_map

character = characters.uijoti

#___________________________________Look__________________________________________
def look():
    room = world_map.Tutorial[character.Loc[0]][character.Loc[1]]['Name']
    desc = world_map.Tutorial[character.Loc[0]][character.Loc[1]]['Description']
    print "You are at the %s, %s" % (room, desc)
    return

#___________________________________Move__________________________________________
def move(dir):
    exits = desc = world_map.Tutorial[character.Loc[0]][character.Loc[1]]['Exits']
    if dir in exits:
        if dir == "North":
            character.Loc = [character.Loc[0] - 1, character.Loc[1]]
            return character.Loc
        if dir == "South":
            character.Loc = [character.Loc[0] + 1, character.Loc[1]]
            return character.Loc
        if dir == "East":
            character.Loc = [character.Loc[0], character.Loc[1] + 1]
            return character.Loc
        if dir == "West":
            character.Loc = [character.Loc[0], character.Loc[1] - 1]
            return character.Loc
        else:
            print "That's not a direction."
            return
    else:
        print "There's not an exit in that direction."
        return
    return

#___________________________________Command__________________________________________
def command():
    command = raw_input('COMMAND: ').upper()

    if command == 'LOOK':
        look()
        return
    if command == 'N' or command == 'NORTH':
        move("North")
        look()
        return
    if command == 'S' or command ==  'SOUTH':
        move("South")
        look()
        return
    if command == 'E' or command ==  'EAST':
        move("East")
        look()
        return
    if command == 'W' or command ==  'WEST':
        move("West")
        look()
        return
    if command == 'FIGHT':
        target = raw_input('WHO? ')
        battle.BATTLE(target, character)
        return
    else:
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    playing = True
    look()
    while playing == True:
        command()

main()