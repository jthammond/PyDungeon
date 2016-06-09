import dice

"""class MeleeWeapon(object):
    def __init__(self, dmg_amount):
        self.dmg_amount = dmg_amount"""

class SWORD(object):
    dmg_amount = dice.d6()
    
class FIREBALL(object):
    dmg_amount = dice.d6()
    