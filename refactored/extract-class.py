class Soldier:
    self.health = 0
    self.weaponStatus = 0

    def attack(self, weapon: Weapon) -> None:
        pass


class Weapon:
    self.damage = 0

    def getDamage(self):
        return self.damage