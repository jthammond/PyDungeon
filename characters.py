import weapons
import spells

class Player(object):
    def __init__(self, Name, Class, Loc, Lvl, Wield, AC, RM, Status, Spells):
        self.Name = Name
        self.Class = Class
        self.AC = AC  # Armor Class
        self.Loc = Loc  # Location
        self.Lvl = Lvl
        self.Wield = Wield
        self.RM = RM  # Roll Modifier
        self.HP = Status['HP']
        self.INIT = Status['Initiative']
        self.Spells = Spells

class Uijoti(Player):
    def __init__(self):
        self.Name = 'Uijoti'
        self.Class = 'Rogue'
        self.Loc = [3, 5]
        self.Lvl = 3
        self.Wield = weapons.Sword
        self.AC = 17
        self.RM = 5
        self.Status = {'HP': 15, 'Initiative': 5}
        self.Spells = []


class Zetaphor(Player):
    def __init__(self):
        self.Name = 'Zetaphor'
        self.Class = 'Sorcerer'
        self.Loc = [3, 5]
        self.Lvl = 3
        self.Wield = weapons.Staff
        self.AC = 15
        self.RM = 3
        self.Status = {'HP': 15, 'Initiative': 4}
        self.Spells = [weapons.magic_missle, weapons.fireball]

uijoti = Player(Uijoti().Name, Uijoti().Class, Uijoti().Loc, Uijoti().Lvl, Uijoti().Wield,
                Uijoti().AC, Uijoti().RM, Uijoti().Status, Uijoti().Spells)

zetaphor = Player(Zetaphor().Name, Zetaphor().Class, Zetaphor().Loc, Zetaphor().Lvl,
                  Zetaphor().Wield, Zetaphor().AC, Zetaphor().RM, Zetaphor().Status, Zetaphor().Spells)
