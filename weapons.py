import dice

class Weapon(object):
    def __init__(self, Name, Dmg):
        self.Name = Name
        self.Dmg = Dmg

class Melee(Weapon):
    def __init__(self, Name):
        self.Name = 'Staff'
        self.Dmg = dice.d4()

class Melee(Weapon):
    def __init__(self, Name):
        self.Name = 'Sword'
        self.Dmg = dice.d6()

class Magic(Weapon):
    def __init__(self, Name):
        self.Name = 'Magic Missile'
        self.Lvl = 1
        self.dmg = dice.d4()
