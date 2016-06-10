
class Enemy(object):
        
        def __init__(self, CR, AC, Status):
                self.CR = CR
                self.AC = AC
                self.HP = Status['HP']
                self.INIT = Status['Initiative']


class KOBOLD(Enemy):
        def __init__(self):
                self.CR = 0.25
                self.AC = 15
                self.Status = {'HP': 4, 'Initiative' : 8}