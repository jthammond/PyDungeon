import dice
import weapons
import character
import monsters
import itertools

uijoti = character.Player(character.Uijoti().Name, character.Uijoti().Class, character.Uijoti().AC, character.Uijoti().Lvl, character.Uijoti().Wield, character.Uijoti().RM, character.Uijoti().Status, character.Uijoti().Spells)
kobold = monsters.Enemy(monsters.Kobold().Name, monsters.Kobold().CR, monsters.Kobold().AC, monsters.Kobold().Attack, monsters.Kobold().Status)


def battle(enemy, character):
    enemy_INIT = dice.d20() + enemy.INIT
    character_INIT = dice.d20() + character.INIT
    #battle_pool = [enemy, character]
    print "enemy_INIT = " + str(enemy_INIT)
    print "party_INIT = " + str(character_INIT)

    if character_INIT >= enemy_INIT:
        print "CHARACTER FIRST"
        battle_pool = [character, enemy]
        #for i in itertools.cycle(battle_pool[1:]):
        for i in itertools.cycle(battle_pool):
            print i

    if enemy_INIT >= character_INIT:
        print "ENEMY FIRST"
        battle_pool = [enemy, character]
        #for i in itertools.cycle(battle_pool[0:]):
        for i in itertools.cycle(battle_pool):
                print i

battle(kobold, uijoti)
