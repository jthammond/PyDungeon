import dice

class MagicWeapon(object):
    def __init__(self, dmg):
        self.dmg = dmg

class MagicMissle(MagicWeapon):
    def __init__(self):
        self.dmg = dice.d6()
    
    