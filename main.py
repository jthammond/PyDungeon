import characters
import monsters
import battle
import world_map

character = characters.uijoti

#___________________________________Look__________________________________________
def look():
    print world_map.Tutorial[character.Loc[0]][character.Loc[1]]
    print character.Loc
    return

#___________________________________Command__________________________________________
def user_input():
    command = raw_input('COMMAND: ').upper()

    if command == 'LOOK':
        print command
        look()
        return
    elif command == 'N' or command == 'NORTH':
        print command
        character.Loc = [character.Loc[0] - 1, character.Loc[1]]
        return character.Loc
    elif command == 'S' or command == 'SOUTH':
        print command
        character.Loc = [character.Loc[0] + 1, character.Loc[1]]
        return character.Loc
    elif command == 'E' or command == 'EAST':
        print command
        character.Loc = [character.Loc[0], character.Loc[1] + 1]
        return character.Loc
    elif command == 'W' or command == 'WEST':
        print command
        character.Loc = [character.Loc[0], character.Loc[1] - 1]
        return character.Loc
    elif command == 'FIGHT':
        target = raw_input('WHO? ')
        battle.BATTLE(target, character)
        return
    else:
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    """playing = True

    while playing == True:
        look()
        user_input()"""



main()

battle.BATTLE(monsters.kobold, characters.zetaphor)
