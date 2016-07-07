from time import sleep
import actions
import tools
import characters

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']

#___________________________________Command__________________________________________
def command(raw_command):

    command_list = ['Look', 'Help', 'Inventory', 'Fight', 'North or N', 'East or E', 'South or S', 'West or W', 'Quit']
    command = str(raw_command)

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
        usr_input = raw_input('CMD: ').upper()
        
        if usr_input == 'QUIT':
            break
        else:
            command(usr_input)
        
        


main()