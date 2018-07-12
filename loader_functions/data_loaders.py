import os
import shelve

def save_game(player, entities, game_map, message_log, game_state):
    with shelve.open('savegame', 'n') as f:
        f['player_index'] = entities.index(player)
        f['entities'] = entities
        f['game_map'] = game_map
        f['message_log'] = message_log
        f['game_state'] = game_state

def load_game():
    if not os.path.isfile('savegame.dat'):
        raise FileNotFoundError

    with shelve.open('savegame', 'r') as f:
        player_index = f['player_index']
        entities = f['entities']
        game_map = f['game_map']
        message_log = f['message_log']
        game_state = f['game_state']

    player = entities[player_index]

    return player, entities, game_map, message_log, game_state
