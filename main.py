from time import sleep
import actions
import tools
import characters

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']

#___________________________________Command__________________________________________
def command(usr_input):

    command_list = ['Look', 'Help', 'Inventory', 'Fight', 'North or N', 'East or E', 'South or S', 'West or W', 'Quit']
    command = str(usr_input)

    if command == 'LOOK':
        actions.LOOK()
        return
    
    if command == 'HELP':
        tools.CLEAR_SCREEN()
        print "The commands are:"
        tools.PRINT_LIST(command_list)
        return
    
    if command == 'INVENTORY':
        tools.CLEAR_SCREEN()
        
        print "You open your pack to find:"
        inventory = character['Inventory']

        for i in inventory:
            print "%s X %s" % (str(inventory[i]), i)
        return
    
    if command == 'N' or command == 'NORTH':
        tools.CLEAR_SCREEN()
        actions.MOVE("North")
        actions.GET_ROOM(character["Loc"])
        return

    if command == 'S' or command ==  'SOUTH':
        tools.CLEAR_SCREEN()
        actions.MOVE("South")
        actions.GET_ROOM(character["Loc"])
        return

    if command == 'E' or command ==  'EAST':
        tools.CLEAR_SCREEN()
        actions.MOVE("East")
        actions.GET_ROOM(character["Loc"])
        return

    if command == 'W' or command ==  'WEST':
        tools.CLEAR_SCREEN()
        actions.MOVE("West")
        actions.GET_ROOM(character["Loc"])
        return

    if command == 'FIGHT':
        tools.CLEAR_SCREEN()
        actions.FIGHT(enemy, character)
        return

    else:
        tools.CLEAR_SCREEN()
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    
    print "______     ___  ____   _______  "
    print "| ___ \    |  \/  | | | |  _  \ "
    print "| |_/ /   _| .  . | | | | | | | "
    print "|  __/ | | | |\/| | | | | | | | "
    print "| |  | |_| | |  | | |_| | |/ /  "
    print "\_|   \__, \_|  |_/\___/|___/   "
    print "       __/ |                    "
    print "      |___/                     "
    
    sleep(1)
    tools.CLEAR_SCREEN()
    
    print "You wake up to a large crash, hazy and confused. LOOK around, maybe get some HELP."
      
    while True:
        raw_command = raw_input('CMD: ').upper()
        
        if raw_command == 'QUIT':
            break
        else:
            command(raw_command)
        
        


main()