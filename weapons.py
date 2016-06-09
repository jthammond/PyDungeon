import dice

class Weapon:
    def __init__(self, dmg_amount):
        self.dmg_amount = dmg_amount

SWORD = Weapon(dice.d6())