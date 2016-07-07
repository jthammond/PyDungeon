import tools
import characters
import actions

#______________________________User Input for Combat___________________________________
def atk_commands(defender, attacker):
    atk_choices = ['Melee Attack', 'Magic Attack', 'Use Item', 'Hold']

    tools.ENUM_LIST(atk_choices)

    cmd = str(raw_input("BATTLE: "))

    if cmd == '1':
        ATTACK(defender, attacker, "Melee")

    elif cmd == '2':
        ATTACK(defender, attacker, "Magic")

    elif cmd == '3':
        print "This isn't in the game yet, but it looks like %s is getting ready to take a swing!" % (defender["Name"])
        return

    elif cmd == '4':
        print "You hold the line!"
        return
    else:
        print "INVALID COMMAND"

#____________________________________Attack_____________________________________________
def ATTACK(target, attacker, atk_type):
    nat_roll = actions.ROLL("d20")
    roll = nat_roll + attacker["RM"]  # <-- roll modifier

    #finds atk_type of attack and assigns damage accordingly
    if atk_type == "Melee":
        damage = actions.ROLL(characters.weapon["Melee"][attacker["Wield"]]["Dmg"])

    elif atk_type == "Magic":
        if attacker["Spells"] == []:
            print "You search for a spell, but don't have any! Enemy %s gets the jump!" % (target["Name"])
            return
        else:
            #Choosing spell
            spell_book = []
            for i in attacker["Spells"]:
                spell_book.append(i)

            tools.ENUM_LIST(spell_book)

            choice = int(raw_input('Choose Spell: ')) - 1
            spell = attacker["Spells"][choice]

            #Checking for damage multiplier
            if characters.weapon["Magic"][spell]["Mtplr"]:
                damage = attacker["Lvl"] * actions.ROLL(characters.weapon["Magic"][spell]["Dmg"])

            elif not characters.weapon["Magic"][spell]["Mtplr"]:
                damage = actions.ROLL(characters.weapon["Magic"][spell]["Dmg"])

            else:
                print 'Something went wrong.'

    else:
        print "That's not a weapon!"
        return

    #Rolls to hit/crit/fumble and dealing damage to target
    if nat_roll == 1:
        print "%s fumbled..." % (attacker["Name"])
        return
    elif nat_roll == 20:
        target["Status"]["HP"] = target["Status"]["HP"] - (2 * damage)
        print "CRITICAL HIT! %s dealt %s damage!" % (attacker["Name"], damage)
        return target["Status"]["HP"]
    elif roll >= target["AC"]:
        target["Status"]["HP"] = target["Status"]["HP"] - damage
        print "Hit! %s dealt %s damage!" % (attacker["Name"], damage)
        return target["Status"]["HP"]
    else:
        print "%s's attack missed!" % (attacker["Name"])
        return

#____________________________________Battle_____________________________________________
def BATTLE(enemy, character):

    enemy_INIT = actions.ROLL("d20") + enemy["Status"]["INIT"]
    character_INIT = actions.ROLL("d20") + character["Status"]["INIT"]

    battle_pool = []

    #Roll initiative and assign to battle_pool
    if character_INIT >= enemy_INIT:
        print "%s gets first strike!" % (character["Name"])
        battle_pool = [character, enemy]
    elif enemy_INIT > character_INIT:
        print "%s gets the jump on you!" % (enemy["Name"])
        battle_pool = [enemy, character]

    #Loop to the death!
    while enemy["Status"]["HP"] and character["Status"]["HP"] > 0:
        tools.CLEAR_SCREEN()
        if enemy["Status"]["HP"] <= 0:
            print "You have slain the enemy!"
            return
        elif character["Status"]["HP"] <= 0:
            print "You have been slain..."
            return
        else:
            for x in battle_pool:
                attacker = x
                defender = battle_pool[1]

                if attacker == character:
                    atk_commands(defender, attacker)
                    battle_pool = [defender, attacker]
                    continue

                elif attacker == enemy:
                    ATTACK(defender, attacker, "Melee")
                    print "You have %s health left!" % str(character["Status"]["HP"])
                    battle_pool = [defender, attacker]
                    continue

                else:
                    print "Something went wrong, time for a beer..."
                    break
