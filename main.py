from time import sleep
import actions
import tools
import characters
import world_map

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']

#___________________________________Command__________________________________________
def command(usr_input):
    x = character["Loc"][0]
    y = character["Loc"][1]
    command_list = ['LOOK (direction)', 'HELP', 'INVENTORY', 'FIGHT', 'NORTH OR N', 'EAST or E', 'SOUTH or S', 'WEST or W', 'QUIT']
    cmdSplit = usr_input.split()
    
    if len(cmdSplit) > 2:
        print "Too many options"
        return
    if len(cmdSplit) == 2:
        command = cmdSplit[0]
        cmd_lwr = cmdSplit[1].lower()
        cmd_opt = cmd_lwr.capitalize()
        
        if command == 'LOOK':
            exits = world_map.Tutorial[x][y]["Exits"]
            
            if cmd_opt in exits:  # or cmd_opt in exit_letters
                if cmd_opt == "North":
                    #tools.CLEAR_SCREEN()
                    print world_map.Tutorial[x-1][y]["Name"]
                if cmd_opt == "South":
                    #tools.CLEAR_SCREEN()
                    print world_map.Tutorial[x+1][y]["Name"]
                if cmd_opt == "East":
                    #tools.CLEAR_SCREEN()
                    print world_map.Tutorial[x][y+1]["Name"]
                if cmd_opt == "West":
                    #tools.CLEAR_SCREEN()
                    print world_map.Tutorial[x][y-1]["Name"]
                return
            else:
                print "Look where?"
                return
            return
        return
        
        
    if len(cmdSplit) == 1:
        command = usr_input

        if command == 'LOOK':
            actions.LOOK()
            return
        
        if command == 'HELP':
            tools.CLEAR_SCREEN()
            print "Commands are not case sensative and are displayed as COMMAND (options). The commands are:"
            for i in command_list:
                print i
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
            actions.GET_ROOM()
            return
    
        if command == 'S' or command ==  'SOUTH':
            tools.CLEAR_SCREEN()
            actions.MOVE("South")
            actions.GET_ROOM()
            return
    
        if command == 'E' or command ==  'EAST':
            tools.CLEAR_SCREEN()
            actions.MOVE("East")
            actions.GET_ROOM()
            return
    
        if command == 'W' or command ==  'WEST':
            tools.CLEAR_SCREEN()
            actions.MOVE("West")
            actions.GET_ROOM()
            return
    
        if command == 'FIGHT':
            tools.CLEAR_SCREEN()
            actions.FIGHT(enemy, character)
            return
    
        else:
            tools.CLEAR_SCREEN()
            print "INVALID COMMAND"
            return
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
            command(str(raw_command))



main()