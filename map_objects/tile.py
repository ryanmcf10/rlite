"""
A tile on a map.  It may or may not be blocked, and may or may not block sight
"""
class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # By default, sight is blocked if the tile is blocked
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

        self.explored = False
