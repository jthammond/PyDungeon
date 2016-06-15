import dice
import characters
import monsters

def PRINT_LIST(list):
    print(' '.join('{}: {}'.format(*i) for i in enumerate(list, 1),))

#____________________________________Attack_____________________________________________
def ATTACK(target, attacker, type):
    nat_roll = dice.d20()
    roll = nat_roll + attacker.RM  # <-- roll modifier

    if type == 'melee':
        damage = attacker.Wield().Dmg
        
    elif type == 'magic':
        if attacker.Spells == []:
            print "You search for a spell, but don't have any! Enemy %s gets the jump!" % (target.Name)
            return
        else:
            spell_book = []
            for i in attacker.Spells:
                spell_book.append(i.Name)
                
            PRINT_LIST(spell_book)
            
            choice = int(raw_input('Choose Spell: ')) - 1
            spell = attacker.Spells[choice]
            damage = spell.Dmg
    
    else:
        print "That's not a weapon!"
        return
    
    if nat_roll == 1:
        print "%s fumbled..." % (attacker.Name)
        return
    elif nat_roll == 20:
        target.HP = target.HP - (2 * damage)
        if target.HP > 0:
            print "CRITICAL HIT! %s dealt %s damage!" % (attacker.Name, damage)
            return target.HP
    elif roll >= target.AC:
        target.HP = target.HP - damage
        if target.HP > 0:
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

    if character_INIT >= enemy_INIT:
        print "%s gets first strike!" % (character.Name)
        battle_pool = [character, enemy]
    if enemy_INIT > character_INIT:
        print "%s gets the jump on you!" % (enemy.Name)
        battle_pool = [enemy, character]

    while enemy.HP and character.HP > 0:
        
        for x in battle_pool:
            attacker = x
            defender = battle_pool[1]
            
            if isinstance(attacker, characters.Player):
                atk_commands = ['Melee Attack', 'Magic Attack', 'Use Item', 'Hold']
                PRINT_LIST(atk_commands)
                    
                cmd = str(raw_input("BATTLE: "))
                
                if cmd == '1':
                    ATTACK(defender, attacker, 'melee')

                    if enemy.HP <= 0:
                        print "You have slain the enemy!"
                        return
                    elif character.HP <= 0:
                        print "You have been slain..."
                        return
                    else:
                        battle_pool = [defender, attacker]
                        continue
                    
                elif cmd == '2':
                        ATTACK(defender, attacker, 'magic')
                        
                        if enemy.HP <= 0:
                            print "You have slain the enemy!"
                            return
                        elif character.HP <= 0:
                            print "You have been slain..."
                            return
                        else:
                            battle_pool = [defender, attacker]
                            continue
                        
                elif cmd == '3':
                    print "This isn't in the game yet"
                
                elif cmd == '4':
                    print "You scuttle away with your tail between your legs..."
                    return
                else:
                    print "INVALID COMMAND"
                
            elif isinstance(attacker, monsters.Enemy):
                    ATTACK(defender, attacker, 'melee')

                    if defender.HP <= 0:
                        print "You have slain the enemy!"
                        return
                    elif attacker.HP <= 0:
                        print "You have been slain..."
                        return
                    else:
                        battle_pool = [defender, attacker]
                        continue
                    
            else:
                print "Something went wrong, time for a beer..."
                break
