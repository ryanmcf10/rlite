from enum import Enum, auto
import libtcodpy as libtcod

from game_messages import Message


class Fighter:
    def __init__(self, hp, defense, power, xp=0):
        self.base_max_hp = hp
        self.base_defense = defense
        self.base_power = power

        self.hp = hp
        self.xp = xp

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            return self.base_max_hp + self.owner.equipment.max_hp_bonus
        else:
            return self.base_max_hp

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            return self.base_defense + self.owner.equipment.defense_bonus
        else:
            return self.base_defense

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            return self.base_power + self.owner.equipment.power_bonus
        else:
            return self.base_power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message': Message('{} attacks {} for {} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{} attacks {} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

class FighterType(Enum):
    PLAYER = auto()
    ORC = auto()
    TROLL = auto()

def create_fighter(fighter_type):
    if fighter_type == FighterType.PLAYER:
        return Fighter(hp=30, defense=2, power=5)

    elif fighter_type == FighterType.ORC:
        return Fighter(hp=10, defense=0, power=2, xp=35)

    elif fighter_type == FighterType.TROLL:
        return Fighter(hp=16, defense=1, power=4, xp=100)

    else:
        return None
