import dice
import itertools
import weapons
import spells
import characters
import monsters

uijoti = characters.Player(characters.Uijoti().Name, characters.Uijoti().Class, characters.Uijoti().AC, characters.Uijoti().Lvl, characters.Uijoti().Wield, characters.Uijoti().RM, characters.Uijoti().Status, characters.Uijoti().Spells)
zetaphor = characters.Player(characters.Zetaphor().Name, characters.Zetaphor().Class, characters.Zetaphor().AC, characters.Zetaphor().Lvl, characters.Zetaphor().Wield, characters.Zetaphor().RM, characters.Zetaphor().Status, characters.Zetaphor().Spells)
kobold = monsters.Enemy(monsters.Kobold().Name, monsters.Kobold().CR, monsters.Kobold().AC, monsters.Kobold().RM, monsters.Kobold().Wield, monsters.Kobold().AttackPerc, monsters.Kobold().Status)

magic_missle = weapons.Magic(weapons.Magic_Missile().Name, weapons.Magic_Missile().Dmg, weapons.Magic_Missile().Lvl)
fireball = weapons.Magic(weapons.Fireball().Name, weapons.Fireball().Dmg, weapons.Fireball().Lvl)

