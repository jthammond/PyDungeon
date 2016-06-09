#import dice
import weapons
import monsters
    
def attack(target, weapon):
    if target.Status['HP'] <=0:
        print "They're already dead!"
        
    else:
        if target.Status['HP'] >= 0:
            target.Status['HP'] = target.Status['HP'] - weapon.dmg_amount
            print "Hit! Enemy %s health left!" % (target.Status['HP'])
            return target.Status['HP']
             
        else:
            print "Missed! Enemy %s health left!" % (target.Status['HP'])


