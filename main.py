import actions
import characters

#_____________________________For Testing__________________________________
enemy = characters.npc['Kobold']
character = characters.player['Uijoti']

#___________________________________Command__________________________________________
def command():
    command_list = ['Look', 'Help', 'North or N', 'East or E', 'South or S', 'West or W', 'Fight']
    command = raw_input('COMMAND: ').upper()

    if command == 'LOOK':
        actions.look()
        return
    if command == 'HELP':
        print "The commands are:"
        actions.PRINT_LIST(command_list)
        return
    if command == 'N' or command == 'NORTH':
        actions.move("North")
        actions.look()
        return
    if command == 'S' or command ==  'SOUTH':
        actions.move("South")
        actions.look()
        return
    if command == 'E' or command ==  'EAST':
        actions.move("East")
        actions.look()
        return
    if command == 'W' or command ==  'WEST':
        actions.move("West")
        actions.look()
        return
    if command == 'FIGHT':
        #target = raw_input('WHO? ')
        actions.FIGHT(enemy, character)
        return
    else:
        print "INVALID COMMAND"
        return

#___________________________________Main__________________________________________
def main():
    
    playing = True
    
    actions.look()
    
    while playing == True:
        command()


main()