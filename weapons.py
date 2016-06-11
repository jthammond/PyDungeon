import dice

class MeleeWeapon(object):
    def __init__(self, dmg):
        self.dmg = dmg

class Staff(MeleeWeapon):
    def __init__(self):
        self.dmg = dice.d4()

class Sword(MeleeWeapon):
    def __init__(self):
        self.dmg = dice.d6()
