import characters
import monsters
import battle
import map

character = characters.uijoti

#___________________________________Look__________________________________________
def look():
    print map.Tutorial[character.Loc[0]][character.Loc[1]]
    return

#___________________________________Move__________________________________________
def move(direction):
    
    # map.Tutorial[x][y]
    
    if direction == 'N':
        character.Loc = [character.Loc[0] - 1, character.Loc[1]]
        look()
        return character.Loc
    elif direction == 'S' :
        character.Loc = [character.Loc[0] + 1, character.Loc[1]]
        look()
        return character.Loc
    elif direction == 'E':
        character.Loc = [character.Loc[0], character.Loc[1] + 1]
        look()
        return character.Loc
    elif direction == 'W':
        character.Loc = [character.Loc[0], character.Loc[1] - 1]
        look()
        return character.Loc
    else:
        print "Not a valid direction."
        return
    
    return

#___________________________________Command__________________________________________
def command():
    command = raw_input('COMMAND: ').upper()
    
    if command == 'LOOK':
        look()
        return
    elif command == 'N' or 'NORTH':
        move('N')
        return
    elif command == 'S' or 'SOUTH':
        move('S')
        return
    elif command == 'E' or 'EAST':
        move('E')
        return
    elif command == 'W' or 'WEST':
        move('W')
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

    return

main()