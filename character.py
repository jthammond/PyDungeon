import weapons
import spells

class Player(object):

        def __init__(self, Name, Class, AC, Lvl, Wield, RM, Status, Spells):
                self.Name = Name
                self.Class = Class
                self.AC = AC
                self.Lvl = Lvl
                self.Wield = Wield
                self.RM = RM
                self.HP = Status['HP']
                self.INIT = Status['Initiative']
                self.Spells = Spells

class Uijoti(Player):
        def __init__(self):
                self.Name = 'Uijoti'
                self.Class = 'Rogue'
                self.Lvl = 3
                self.Wield = weapons.Sword
                self.AC = 17
                self.RM = 5 #Roll Modifier
                self.Status = {'HP': 10, 'Initiative' : 5}
                self.Spells = []

class Zetaphor(Player):
        def __init__(self):
                self.Name = 'Zetaphor'
                self.Class = 'Sorcerer'
                self.AC = 15
                self.Lvl = 3
                self.Wield = weapons.Staff
                self.RM = 3 #Roll Modifier
                self.Status = {'HP': 10, 'Initiative' : 4}
                self.Spells = ['Magic_Missle', 'Fireball']
                
class Nobody(Player):
        def __init__(self):
                self.Name = 'Nobody'
                self.Class = 'Nothing'
                self.AC = 0
                self.Lvl = 0
                self.Wield = weapons.Nothing
                self.RM = 0 #Roll Modifier
                self.Status = {'HP': 0, 'Initiative' : 0}
                self.Spells = []
