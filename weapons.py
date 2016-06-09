import dice

class MeleeWeapon(object):
    def __init__(self, dmg_amount):
        self.dmg_amount = dmg_amount

class Spell(object):
    def __init__(self, dmg_amount):
        self.dmg_amount = dmg_amount

class SWORD(MeleeWeapon):
    dmg_amount = dice.d6()
    
class FIREBALL(Spell):
    dmg_amount = dice.d6()
    