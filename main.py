import dice
import weapons
import spells
import monsters
import character

player = character.Player('Uijoti')
character = character.Character(player.Name, player.AC, player.Status, player.Lvl, player.Wield, player.RM)

#weapon = weapons.Weapon(weapons.Melee('Sword').Name, weapons.Melee('Sword').Dmg)  #<--- Path to follow for damage from weapons


kobold = monsters.Kobold('Kobold1')
enemy = monsters.Enemy(kobold.Name, kobold.CR, kobold.AC, kobold.Status )


def attack(target, character):
    fumble = 1 #dice.d20()
    #melee_weapon = weapons.Weapon(weapons.Melee(character.Wield).Name, weapons.Melee(character.Wield).Dmg)
    #magic_weapon = weapons.Weapon(weapons.Magic(character.Wield).Name, weapons.Magic(character.Wield).Dmg)
    roll = fumble + 5 # <-- character.RM
    print "Fumble: " + str(fumble)
    print "Roll: " + str(roll)
    if fumble == 1:
        "You fumbled..."
        return
    elif roll == 20:
        target.HP = target.HP - (2 * character.Dmg)
        if target.HP > 0:
            print "CRITICAL HIT! nemy %s health left!" % (target.HP)
            return target.HP
    elif roll >= target.AC:
        target.HP = target.HP - character.Dmg
        if target.HP > 0:
            print "Hit! You dealt %s damage!" % (character.Dmg)
            return target.HP
    else:
        print "Your attack missed!"
        return


def battle(enemy, party):
#------------------------------------------------------------------
    command_list = ['1 : FIGHT',
                    '2 : RUN']
    print "You can 1: FIGHT or 2: RUN!"

    command = str(raw_input("COMMAND: "))
    if command == '1':
        while enemy.HP and party.HP > 0:
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
                melee_weapon = weapons.Weapon(weapons.Melee(party.Wield).Name, weapons.Melee(party.Wield).Dmg)
                attack(enemy, character)
                if enemy.HP <= 0:
                    print "Congratulations, you have slain the enemy!"
                    return
                else:
                    continue

            elif cmd == '2':
                magic_weapon = weapons.Weapon(weapons.Magic(character.Wield).Name, weapons.Magic(character.Wield).Dmg)
                attack(enemy, character.Magic)
                if enemy.HP <= 0:
                    print "Congratulations, you have slain the enemy!"
                    return
                else:
                    continue

            elif cmd == '3':
                print "This isn't in the game yet"
                continue

            elif cmd == '4':
                print "You hold the line!"
                continue
            else:
                print "Invalid command. Please try again."
                continue

        else:
            if party.HP > enemy.HP:
                print "Congratulations, you have slain the enemy party!"
                combat = False
                return

            elif enemy.HP > party.HP:
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
        return

    return


def main():

    battle(enemy, character)
    return

main()
