class Character(object):
        
        def __init__(self, Name, AC, Status):
                self.Name = Name
                self.AC = AC
                self.HP = Status['HP']
                self.INIT = Status['Initiative']


class Player(Character):
        def __init__(self, Name):
                self.Name = 'Uijoti'
                self.AC = 15
                self.Status = {'HP': 10, 'Initiative' : 12}
                
class Player(Character):
        def __init__(self, Name):
                self.Name = 'Zetaphor'
                self.AC = 15
                self.Status = {'HP': 10, 'Initiative' : 12}