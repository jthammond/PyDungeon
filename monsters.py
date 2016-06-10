class Enemy(object):
        
        def __init__(self, Name, CR, AC, Status):
                self.Name = Name
                self.CR = CR
                self.AC = AC
                self.HP = Status['HP']
                self.INIT = Status['Initiative']


class Kobold(Enemy):
        def __init__(self, Name):
                self.Name = 'Kobold1'
                self.CR = 0.25
                self.AC = 15
                self.Status = {'HP': 15, 'Initiative' : 8}
