import weapons

class Enemy(object):
        def __init__(self, Name, CR, AC, RM, Wield, AttackPerc, Status):
                self.Name = Name
                self.CR = CR
                self.AC = AC
                self.RM = RM
                self.Wield = Wield
                self.AttackPerc = AttackPerc
                self.HP = Status['HP']
                self.INIT = Status['Initiative']


class Kobold(Enemy):
        def __init__(self):
                self.Name = 'Kobold'
                self.CR = 0.25
                self.AC = 14
                self.RM = 1
                self.Wield = weapons.Fists
                self.AttackPerc = 85
                self.Status = {'HP': 8, 'Initiative' : 1}

class Rat(Enemy):
        def __init__(self):
                self.Name = 'Rat'
                self.CR = 0.025
                self.AC = 12
                self.AttackPerc = 8
                self.Status = {'HP': 5, 'Initiative' : 2}
                
kobold = Enemy(Kobold().Name, Kobold().CR, Kobold().AC, Kobold().RM, Kobold().Wield, Kobold().AttackPerc, Kobold().Status)