import dice
import weapons
import monsters


KOBOLD = monsters.KOBOLD()
enemy = monsters.Enemy(KOBOLD.CR, KOBOLD.AC, KOBOLD.Status )

SWORD = weapons.SWORD()
attk = weapons.MeleeWeapon(SWORD.dmg)


def attack(target, weapon):
    if enemy.HP <=0:
        print "They're already dead!"
        
    else:
        if enemy.HP >= 0:
            enemy.HP = enemy.HP - weapon.dmg
            if enemy.HP > 0:
                print "Hit! Enemy %s health left!" % (enemy.HP)
                return enemy.HP
            else:
                print "You have slain the %s!" % (target)
        else:
            print "Missed! Enemy %s health left!" % (enemy.HP)

def main():
    attack(KOBOLD, SWORD)
    
    return

main()