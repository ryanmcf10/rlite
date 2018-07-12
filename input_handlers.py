import libtcodpy as libtcod

from game_states import GameStates

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYER_TURN:
        return handle_player_turn_keys(key)

    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)

    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_show_inventory_keys(key)

    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)

    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_keys(key)

    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen_keys(key)

    return {}

def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}
    elif key_char == 'z':
        return {'wait': True}

    # Pick up item
    elif key_char == 'g':
        return {'pickup': True}

    # Inventory
    elif key_char == 'i':
        return {'show_inventory': True}
    elif key_char == 'd':
        return {'drop_inventory': True}

    # Stats
    elif key_char == 'c':
        return {'show_character_screen': True}


    elif key.vk == libtcod.KEY_ENTER:
        return {'take_stairs': True}

    # Alt+Enter: toggle full screen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    # ESC - Exit the game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    # No key was pressed
    return {}

def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    # Alt+Enter: toggle full screen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    # ESC - Exit the game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_show_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    # Alt+Enter: toggle full screen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    # ESC - Exit the game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_main_menu_keys(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}

    elif key_char == 'b':
        return {'load_game': True}

    elif key_char == 'c':
        return {'exit': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_level_up_keys(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'level_up': 'hp'}

    elif key_char == 'b':
        return {'level_up': 'str'}

    elif key_char == 'c':
        return {'level_up': 'def'}

    return {}

def handle_character_screen_keys(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_targeting_keys(key):
    # ESC - Exit the game
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}

    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}
