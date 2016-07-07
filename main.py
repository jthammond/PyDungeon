import actions
import tools
import characters

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']

#___________________________________Command__________________________________________
def command(raw_command):

    command_list = ['Look', 'Help', 'North or N', 'East or E', 'South or S', 'West or W', 'Fight', 'Quit']
    command = str(raw_command)

    if command == 'LOOK':
        actions.LOOK()
        return
    
    if command == 'HELP':
        tools.CLEAR_SCREEN()
        print "The commands are:"
        tools.PRINT_LIST(command_list)
        return
    
    if command == 'N' or command == 'NORTH':
        actions.MOVE("North")
        actions.LOOK()
        return

    if command == 'S' or command ==  'SOUTH':
        actions.MOVE("South")
        actions.LOOK()
        return

    if command == 'E' or command ==  'EAST':
        actions.MOVE("East")
        actions.LOOK()
        return

    if command == 'W' or command ==  'WEST':
        actions.MOVE("West")
        actions.LOOK()
        return

    if command == 'FIGHT':
        tools.CLEAR_SCREEN()
        actions.FIGHT(enemy, character)
        return

    #if command == 'QUIT':
    #    return False

    else:
        tools.CLEAR_SCREEN()
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    
    while True:
        usr_input = raw_input('CMD: ').upper()
        if usr_input == 'QUIT':
            break
        else:
            command(usr_input)
        


main()