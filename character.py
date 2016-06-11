import dice
import weapons
import spells

sword = weapons.MeleeWeapon(weapons.Sword)
staff = weapons.MeleeWeapon(weapons.Staff)
missle = spells.MagicWeapon(spells.MagicMissle)

class Character(object):

        def __init__(self, Name, AC, Status, Lvl, Wield, RM):
                self.Name = Name
                self.AC = AC
                self.HP = Status['HP']
                self.INIT = Status['Initiative']
                self.Lvl = Lvl
                self.Wield = Wield
                self.RM = RM


class Player(Character):
        def __init__(self, Name):
                self.Name = 'Uijoti'
                self.Lvl = 3
                self.Wield = sword
                self.AC = 15
                self.RM = 5 #Roll Modifier
                self.Status = {'HP': 10, 'Initiative' : 12}

"""class Player(Character):
        def __init__(self, Name):
                self.Name = 'Zetaphor'
                self.AC = 15
                self.Lvl = 3
                self.Wield = Staff.dmg
                self.RM = 3 #Roll Modifier
                self.Status = {'HP': 10, 'Initiative' : 12}
                # SPELLS DICT = {'SPELL NAME' : [MANA COST, DAMAGE]}
                self.Spells = {'Magic Missle' : [5, (d6()*self.Lvl)]}"""
