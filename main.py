import dice
#import weapons
#import spells
import monsters
import character

uijoti = character.Player(character.Uijoti().Name, character.Uijoti().Class, character.Uijoti().AC, character.Uijoti().Lvl, character.Uijoti().Wield, character.Uijoti().RM, character.Uijoti().Status, character.Uijoti().Spells)
kobold = monsters.Enemy(monsters.Kobold().Name, monsters.Kobold().CR, monsters.Kobold().AC, monsters.Kobold().Attack, monsters.Kobold().Status)


def attack(target, character):
    fumble = dice.d20()
    roll = fumble + character.INIT() # <-- character.RM
    damage = character.Wield().Dmg
    print "Fumble: " + str(fumble)
    print "Roll: " + str(roll)
    if fumble == 1:
        print "You fumbled..."
        return
    elif roll == 20:
        target.HP = target.HP - (2 * damage)
        if target.HP > 0:
            print "CRITICAL HIT! nemy %s health left!" % (target.HP)
            return target.HP
    elif roll >= target.AC:
        target.HP = target.HP - damage
        if target.HP > 0:
            print "Hit! You dealt %s damage!" % (damage)
            return target.HP
    else:
        print "Your attack missed!"
        return


def battle(enemy, character):
#------------------------------------------------------------------
    print "You can 1: FIGHT or 2: RUN!"
    command = str(raw_input("COMMAND: "))
    if command == '1':
        while enemy.HP and character.HP > 0:
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
                attack(enemy, character)
                if enemy.HP <= 0:
                    print "Congratulations, you have slain the enemy!"
                    if enemy.HP and character.HP > 0:
                        continue
                    else:
                        return
                else:
                    continue

            elif cmd == '2':
                #atk_spell = character.Wield
                attack(enemy, character)
                if enemy.HP <= 0:
                    print "Congratulations, you have slain the enemy!"
                    if enemy.HP and character.HP > 0:
                        continue
                    else:
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
            if character.HP > enemy.HP:
                print "Congratulations, you have slain the enemy party!"
                return

            elif enemy.HP > character.HP:
                print "Your skills were no match for the enemies. You have been eliminated"
                return

            else:
                print "I don't know what just happened. Time for beer."
                return

    elif command == '2':
        print "You scuttle away with your tail between your legs..."
        return

    else:
        print "Invalid command. Please try again."
        return

    return


def main():

    battle(kobold, uijoti)
    return

main()
