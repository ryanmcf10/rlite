import libtcodpy as libtcod

from game_messages import Message

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('Inventory full! You cannot carry any more items.', libtcod.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You picked up the {}.'.format(item.name), libtcod.blue)
            })

            self.items.append(item)

        return results
