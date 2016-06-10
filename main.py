import dice
import weapons
import spells
import monsters
import character

player = character.Player('uijoti')
character = character.Character(player.Name, player.AC, player.Status)

kobold = monsters.Kobold('Kobold1')
enemy = monsters.Enemy(kobold.Name, kobold.CR, kobold.AC, kobold.Status )

melee_attk = weapons.Sword()
sword = weapons.MeleeWeapon(melee_attk.dmg)

magic_attk = spells.MagicMissle()
missle = spells.MagicWeapon(magic_attk.dmg)



def attack(target, weapon):

            target.HP = enemy.HP - weapon.dmg
            if enemy.HP > 0:
                print "Hit! Enemy %s health left!" % (target.HP)
                return target.HP



def battle(enemies, party):
#------------------------------------------------------------------    
    enemy_HP = enemies.HP
    party_HP = party.HP
    command_list = ['1 : FIGHT',
                    '2 : RUN']
    print "You can 1: FIGHT or 2: RUN!"
    
    while enemy_HP and party_HP > 0:
        command = str(raw_input("COMMAND: "))
        if command == '1':
            if enemy_HP & party_HP > 0:
#--------------INITIATIVE SYSTEM--------------------
                """combat_pool = {}
                for i in enemies:
                    combat_pool[i] = i.INIT
                for i in party:
                    combat_pool[i] = i.INIT"""
#----------------------------------------------------
                atk_commands = ['1 : Melee Attack',
                                '2 : Magic Attack',
                                '3 : Use Item',
                                '4 : Hold']
                print atk_commands
                
                cmd = str(raw_input("COMMAND: "))
                
                if cmd == '1':
                    attack(enemy, sword)
                    if enemy_HP <= 0:
                        combat = False
                        print "Congratulations, you have slain the enemy party!"
                        #break
                    else:
                        return
                else:
                    return
                    
                if cmd == '2':
                    attack(enemy, missle)
                    if enemy_HP < 0:
                        combat = False
                        print "Congratulations, you have slain the enemy party!"
                        #break
                    else:
                        return
                else:
                    return
                    
                if cmd == '3':
                    print "This isn't in the game yet"
                    
                if cmd == '4':
                    print "You hold the line!"
                    return
            
            else:
                if party_HP > enemy_HP:
                    print "Congratulations, you have slain the enemy party!"
                    combat = False
                    return
                
                elif enemy_HP > party_HP:
                    print "Your skills were no match for the enemies. You have been eliminated"
                    combat = False
                    return
                
                else:
                    print "I don't know what just happened. Time for beer."
                    return
                
        elif command == '2':
            print "You scuttle away with your tail between your legs..."
            combat = False
            return
        
        else:
            print "Invalid command. Please try again."
            print atk_commands
            return
            
    return


def main():
    
    battle(enemy, character)
    return

main()