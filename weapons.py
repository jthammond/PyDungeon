import dice

class Melee(object):
    def __init__(self, Name, Dmg):
        self.Name = Name
        self.Dmg = Dmg

class Magic(object):
    def __init__(self, Name, Dmg, Lvl):
        self.Name = Name
        self.Dmg = Dmg
        self.Lvl = Lvl
        
class Nothing(Melee):
    def __init__(self):
        self.Name = 'Nothing'
        self.Dmg = 'NOBODY DAMAGE'

class Staff(Melee):
    def __init__(self):
        self.Name = 'Staff'
        self.Dmg = dice.d4()

class Sword(Melee):
    def __init__(self):
        self.Name = 'Sword'
        self.Dmg = dice.d6()

class Magic_Missile(Magic):
    def __init__(self):
        self.Name = 'Magic Missile'
        self.Dmg = dice.d4()
        self.Lvl = 1

class Fireball(Magic):
    def __init__(self):
        self.Name = 'Fireball'
        self.Dmg = dice.d6()
        self.Lvl = 1