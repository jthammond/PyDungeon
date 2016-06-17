import weapons

class Enemy(object):
    def __init__(self, Name, CR, AC, RM, Wield, AttackPerc, Status):
        self.Name = Name
        self.CR = CR  # Combat Rating
        self.AC = AC  # Armor Class
        self.RM = RM  # Roll Modifier
        self.Wield = Wield
        self.AttackPerc = AttackPerc  # Liklihood to attack
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
        self.Status = {'HP': 8, 'Initiative': 1}


class Rat(Enemy):
    def __init__(self):
        self.Name = 'Rat'
        self.CR = 0.025
        self.AC = 10
        self.RM = 0
        self.Wield = weapons.Fists
        self.AttackPerc = 8
        self.Status = {'HP': 4, 'Initiative': 2}

kobold = Enemy(Kobold().Name, Kobold().CR, Kobold().AC, Kobold().RM,
               Kobold().Wield, Kobold().AttackPerc, Kobold().Status)

rat = Enemy(Rat().Name, Rat().CR, Rat().AC, Rat().RM,
            Rat().Wield, Rat().AttackPerc, Rat().Status)
