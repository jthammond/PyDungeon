import dice

class MeleeWeapon(object):
    def __init__(self, dmg):
        self.dmg = dmg


class Sword(MeleeWeapon):
    def __init__(self):
        self.dmg = dice.d6()
    
    