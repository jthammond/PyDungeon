import dice
import itertools
import weapons
import spells
import characters
import monsters

uijoti = characters.Player(characters.Uijoti().Name, characters.Uijoti().Class, characters.Uijoti().AC, characters.Uijoti().Lvl, characters.Uijoti().Wield, characters.Uijoti().RM, characters.Uijoti().Status, characters.Uijoti().Spells)
zetaphor = characters.Player(characters.Zetaphor().Name, characters.Zetaphor().Class, characters.Zetaphor().AC, characters.Zetaphor().Lvl, characters.Zetaphor().Wield, characters.Zetaphor().RM, characters.Zetaphor().Status, characters.Zetaphor().Spells)
kobold = monsters.Enemy(monsters.Kobold().Name, monsters.Kobold().CR, monsters.Kobold().AC, monsters.Kobold().RM, monsters.Kobold().Wield, monsters.Kobold().AttackPerc, monsters.Kobold().Status)


def attack(target, attacker):
    nat_roll = dice.d20()
    roll = nat_roll + attacker.RM  # <-- roll modifier
    damage = attacker.Wield().Dmg
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
    

def magic_attack(target, attacker, spell):
    nat_roll = dice.d20()
    roll = nat_roll + attacker.RM  # <-- roll modifier
    damage = spell.Dmg
    if nat_roll == 1:
        print "%s fumbled..." % (attacker.Name)
        return
    elif nat_roll == 20:
        target.HP = target.HP - (2 * damage)
        if target.HP > 0:
            print "CRITICAL HIT! %s's %s dealt %s damage!" % (attacker.Name, spell.Name, damage)
            return target.HP
    elif roll >= target.AC:
        target.HP = target.HP - damage
        if target.HP > 0:
            print "Hit! %s's %s dealt %s damage!" % (attacker.Name, spell.Name, damage)
            return target.HP
    else:
        print "%s's %s missed!" % (attacker.Name, spell.Name)
        return


def battle(enemy, character):
    
#___________________VVV Initiative System VVV_______________________________
    enemy_INIT = dice.d20() + enemy.INIT
    character_INIT = dice.d20() + character.INIT

    battle_pool = []

    if character_INIT >= enemy_INIT:
        print "%s gets first strike!" % (character.Name.upper())
        battle_pool = [character, enemy]
    if enemy_INIT > character_INIT:
        print "%s gets the jump on you!" % (enemy.Name.upper())
        battle_pool = [enemy, character]
#___________________^^^ Initiative System ^^^____________________________
    
    while enemy.HP and character.HP > 0:
        
        for x in battle_pool:
            attacker = x
            defender = battle_pool[1]
            
            if isinstance(x, characters.Player):
                atk_commands = ['1 : Melee Attack',
                                '2 : Magic Attack',
                                '3 : Use Item',
                                '4 : Hold']
                print atk_commands
                cmd = str(raw_input("COMMAND: "))
                if cmd == '1':
                    attack(defender, attacker)
                    print "Enemy has %s health" % (enemy.HP)
                    print "You have %s health" % (character.HP)
                    if enemy.HP <= 0:
                        print "Congratulations, you have slain the enemy!"
                        return
                    elif character.HP <= 0:
                        print "You have been slain..."
                        return
                    else:
                        battle_pool = [battle_pool[1], x]
                        continue
                elif cmd == '2':
                    if character.Spells == []:
                        print "You don't have any spells!"
                        print atk_commands
                        #return
                    else:
                        spell_book =[]
                        option = 1
                        for i in character.Spells:
                            spell_book.append(str(option) + " : " + i.Name)
                            option += 1
                        print spell_book
                        choice = int(raw_input('Choose Spell: ')) - 1
                        spell = character.Spells[choice]
                        magic_attack(defender, attacker, spell)
                        print "Enemy has %s health" % (enemy.HP)
                        print "You have %s health" % (character.HP)
                        if enemy.HP <= 0:
                            print "Congratulations, you have slain the enemy!"
                            return
                        elif character.HP <= 0:
                            print "You have been slain..."
                            return
                        else:
                            battle_pool = [battle_pool[1], x]
                            continue
                elif cmd == '3':
                    print "This isn't in the game yet"
                    print atk_commands
                    #continue
                elif cmd == '4':
                    print "You scuttle away with your tail between your legs..."
                    return
                else:
                    print "INVALID COMMAND"
                    print atk_commands
                    #continue
                
            elif isinstance(x, monsters.Enemy):
                    attack(defender, attacker)
                    print "Enemy has %s health" % (enemy.HP)
                    print "You have %s health" % (character.HP)
                    if enemy.HP <= 0:
                        print "Congratulations, you have slain the enemy!"
                        return
                    elif character.HP <= 0:
                        print "You have been slain..."
                        return
                    else:
                        battle_pool = [battle_pool[1], x]
                        continue
            else:
                print "Something went wrong, time for a beer..."
                break
            



def main():

    battle(kobold, uijoti)
    return

main()
