import libtcodpy as libtcod
from random import randint

from entity import Entity
from map_objects.tile import Tile
from map_objects.rectangle import Rect
import components.fighter as fighter
from components.ai import BasicMonster
from render_functions import RenderOrder

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    # 'Carve out' the tiles in the given rectangle
    def create_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = self.tiles[x][y].block_sight = False

    def create_horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1,x2) + 1):
            self.tiles[x][y].blocked = self.tiles[x][y].block_sight = False

    def create_vertical_tunnel(self, x, y1, y2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = self.tiles[x][y].block_sight = False

    def connect_rooms(self, room1, room2):
        (prev_x, prev_y) = room1.center()
        (new_x, new_y) = room2.center()

        if randint(0, 1) == 1:
            self.create_horizontal_tunnel(prev_x, new_x, prev_y)
            self.create_vertical_tunnel(new_x, prev_y, new_y)
        else:
            self.create_vertical_tunnel(new_x, prev_y, new_y)
            self.create_horizontal_tunnel(prev_x, new_x, prev_y)


    def place_entities(self, room ,entities, max_monsters_per_room):
        number_of_monsters = randint(0, max_monsters_per_room)

        for i in range(number_of_monsters):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            ai_comp = BasicMonster()

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80:
                    monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter.create_fighter(fighter.FighterType.ORC), ai=ai_comp)
                else:
                    monster = Entity(x, y, 'T', libtcod.darker_green, 'Troll', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter.create_fighter(fighter.FighterType.TROLL), ai=ai_comp)

                entities.append(monster)

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities, max_monsters_per_room):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # random width and height
            width = randint(room_min_size, room_max_size)
            height = randint(room_min_size, room_max_size)

            # random position inside map boundaries
            x = randint(0, map_width - width - 1)
            y = randint(0, map_height - height - 1)

            new_room = Rect(x, y, width, height)

            # check if room intersects with any existing room
            # if so, throw it away
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break

            else:
                # "paint" it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room, will be useful later

                if num_rooms == 0:
                    (player.x, player.y) = new_room.center()

                else:
                    self.connect_rooms(rooms[num_rooms-1], new_room)

                self.place_entities(new_room, entities, max_monsters_per_room)

                rooms.append(new_room)
                num_rooms += 1

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked

