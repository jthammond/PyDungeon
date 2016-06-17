import characters
import battle
import map

character = characters.uijoti

#___________________________________Look__________________________________________
def look():
    print map.Tutorial[character.Loc[0]][character.Loc[1]]
    print character.Loc
    return

#___________________________________Command__________________________________________
def command():
    command = raw_input('COMMAND: ').upper()

    if command == 'LOOK':
        print command
        look()
        return
    elif command == 'N' or 'NORTH':
        print command
        character.Loc = [character.Loc[0] - 1, character.Loc[1]]
        return character.Loc
    elif command == 'S' or 'SOUTH':
        print command
        character.Loc = [character.Loc[0] + 1, character.Loc[1]]
        return character.Loc
    elif command == 'E' or 'EAST':
        print command
        character.Loc = [character.Loc[0], character.Loc[1] + 1]
        return character.Loc
    elif command == 'W' or 'WEST':
        print command
        character.Loc = [character.Loc[0], character.Loc[1] - 1]
        return character.Loc
    elif command == 'FIGHT':
        target = raw_input('WHO? ')
        battle(target, character)
        return
    else:
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    playing = True

    while playing == True:
        look()
        command()

main()
