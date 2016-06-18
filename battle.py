import dice
import characters
import monsters

#_____________________________Print Enumerated List__________________________________
def PRINT_LIST(display):
    print ' '.join('{}: {}'.format(*i) for i in enumerate(display, 1),)

#______________________________User Input for Combat___________________________________
def atk_commands(defender, attacker):
    atk_choices = ['Melee Attack', 'Magic Attack', 'Use Item', 'Hold']

    PRINT_LIST(atk_choices)

    cmd = str(raw_input("BATTLE: "))

    if cmd == '1':
        ATTACK(defender, attacker, 'melee')

    elif cmd == '2':
        ATTACK(defender, attacker, 'magic')

    elif cmd == '3':
        print "This isn't in the game yet, but it looks like %s is getting ready to take a swing!" % (defender.Name)
        return

    elif cmd == '4':
        print "You hold the line!"
        return
    else:
        print "INVALID COMMAND"

#____________________________________Attack_____________________________________________
def ATTACK(target, attacker, atk_type):
    nat_roll = dice.d20()
    roll = nat_roll + attacker.RM  # <-- roll modifier

    #finds atk_type of attack and assigns damage accordingly
    if atk_type == 'melee':
        damage = attacker.Wield().Dmg

    elif atk_type == 'magic':
        if attacker.Spells == []:
            print "You search for a spell, but don't have any! Enemy %s gets the jump!" % (target.Name)
            return
        else:
            #Choosing spell
            spell_book = []
            for i in attacker.Spells:
                spell_book.append(i.Name)

            PRINT_LIST(spell_book)

            choice = int(raw_input('Choose Spell: ')) - 1
            spell = attacker.Spells[choice]

            #Checking for damage multiplier
            if spell.Mtplr:
                damage = attacker.Lvl * spell.Dmg

            elif not spell.Mtplr:
                damage = spell.Dmg

            else:
                print 'Something went wrong.'

    else:
        print "That's not a weapon!"
        return

    #Rolls to hit/crit/fumble and dealing damage to target
    if nat_roll == 1:
        print "%s fumbled..." % (attacker.Name)
        return
    elif nat_roll == 20:
        target.HP = target.HP - (2 * damage)
        print "CRITICAL HIT! %s dealt %s damage!" % (attacker.Name, damage)
        return target.HP
    elif roll >= target.AC:
        target.HP = target.HP - damage
        print "Hit! %s dealt %s damage!" % (attacker.Name, damage)
        return target.HP
    else:
        print "%s's attack missed!" % (attacker.Name)
        return

#____________________________________Battle_____________________________________________
def BATTLE(enemy, character):

    enemy_INIT = dice.d20() + enemy.INIT
    character_INIT = dice.d20() + character.INIT

    battle_pool = []

    #Roll initiative and assign to battle_pool
    if character_INIT >= enemy_INIT:
        print "%s gets first strike!" % (character.Name)
        battle_pool = [character, enemy]
    elif enemy_INIT > character_INIT:
        print "%s gets the jump on you!" % (enemy.Name)
        battle_pool = [enemy, character]

    #Loop to the death!
    while enemy.HP and character.HP > 0:

        if enemy.HP <= 0:
            print "You have slain the enemy!"
            return
        elif character.HP <= 0:
            print "You have been slain..."
            return
        else:
            for x in battle_pool:
                attacker = x
                defender = battle_pool[1]

                if isinstance(attacker, characters.Player):
                    atk_commands(defender, attacker)
                    battle_pool = [defender, attacker]
                    continue

                elif isinstance(attacker, monsters.Enemy):
                    ATTACK(defender, attacker, 'melee')
                    battle_pool = [defender, attacker]
                    continue

                else:
                    print "Something went wrong, time for a beer..."
                    break
