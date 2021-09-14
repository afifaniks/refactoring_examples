from abc import ABCMeta, abstractmethod

class Soldier:
    def attack(self, health: int, weapon: Weapon) -> None:
        self.health = health
        self.weapon = Weapon


class IWeapon(metaclass=ABCMeta):
    @abstractmethod
    def get_damage(self) -> int:
        pass
    
    @abstractmethod
    def get_weapon_status(self) -> int:
        pass


class Weapon(IWeapon):
    def __init__(self, damage: int, weapon_status: int):
        self.damage = damage
        self.weapon_status = weapon_status

    def get_damage(self) -> int:
        return self.damage

    def get_weapon_status(self) -> int:
        return self.weapon_status