class Enemy(object):
        def __init__(self, AC, Status):
                self.AC = AC
                self.HP = Status['HP']
                self.INTV = Status['Initiative']
                

class KOBALD(Enemy):
        def __init__(self):
                AC = 15
                Status = {'HP': 4, 'Initiative' : 8}