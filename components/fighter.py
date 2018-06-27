from enum import Enum, auto
import libtcodpy as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message':Message('{} attacks {} for {} hit points!'.format(self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))

        else:
            results.append({'message': Message('{} attacks {} but does no damage!'.format(self.owner.name.capitalize(), target.name), libtcod.white)})

        return results

class FighterType(Enum):
    PLAYER = auto()
    ORC = auto()
    TROLL = auto()

def create_fighter(fighter_type):
    if fighter_type == FighterType.PLAYER:
        return Fighter(hp=30, defense=2, power=5)

    elif fighter_type == FighterType.ORC:
        return Fighter(hp=10, defense=0, power=3)

    elif fighter_type == FighterType.TROLL:
        return Fighter(hp=16, defense=1, power=4)

    else:
        return None

