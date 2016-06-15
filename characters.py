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
                self.Status = {'HP': 15, 'Initiative' : 5}
                self.Spells = []

class Zetaphor(Player):
        def __init__(self):
                self.Name = 'Zetaphor'
                self.Class = 'Sorcerer'
                self.AC = 15
                self.Lvl = 3
                self.Wield = weapons.Staff
                self.RM = 3 #Roll Modifier
                self.Status = {'HP': 15, 'Initiative' : 4}
                self.Spells = [weapons.magic_missle, weapons.fireball]
                
uijoti = Player(Uijoti().Name, Uijoti().Class, Uijoti().AC, Uijoti().Lvl, Uijoti().Wield, Uijoti().RM, Uijoti().Status, Uijoti().Spells)
zetaphor = Player(Zetaphor().Name, Zetaphor().Class, Zetaphor().AC, Zetaphor().Lvl, Zetaphor().Wield, Zetaphor().RM, Zetaphor().Status, Zetaphor().Spells)