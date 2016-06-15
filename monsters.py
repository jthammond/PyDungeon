class Enemy(object):
        def __init__(self, Name, CR, AC, Attack, Status):
                self.Name = Name
                self.CR = CR
                self.AC = AC
                self.Attack = Attack
                self.HP = Status['HP']
                self.INIT = Status['Initiative']


class Kobold(Enemy):
        def __init__(self):
                self.Name = 'Kobold'
                self.CR = 0.25
                self.AC = 14
                self.Attack = 85
                self.Status = {'HP': 15, 'Initiative' : 1}

class Rat(Enemy):
        def __init__(self):
                self.Name = 'Rat'
                self.CR = 0.025
                self.AC = 12
                self.Attack = 8
                self.Status = {'HP': 5, 'Initiative' : 2}