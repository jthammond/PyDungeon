import dice

class Melee(object):
    def __init__(self, Name, Dmg):
        self.Name = Name
        self.Dmg = Dmg

class Magic(object):
    def __init__(self, Name, Mtplr, Dmg, Lvl):
        self.Name = Name
        self.Mtplr = Mtplr #Flags if there is damage multiplyer
        self.Dmg = Dmg
        self.Lvl = Lvl
        
class Fists(Melee):
    def __init__(self):
        self.Name = 'Fists'
        self.Dmg = dice.d4()

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
        self.Mtplr = 'YES'
        self.Dmg = dice.d4()
        self.Lvl = 1

class Fireball(Magic):
    def __init__(self):
        self.Name = 'Fireball'
        self.Mtplr = 'YES'
        self.Dmg = dice.d6()
        self.Lvl = 2
        
magic_missle = Magic(Magic_Missile().Name, Magic_Missile().Mtplr, Magic_Missile().Dmg, Magic_Missile().Lvl)
fireball = Magic(Fireball().Name, Fireball().Mtplr, Fireball().Dmg, Fireball().Lvl)