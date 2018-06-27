import libtcodpy as libtcod

def handle_keys(key):
    key_char = chr(key.c)

    # Movement
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

    # Alt+Enter - toggle fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    # ESC - exit
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit':True}

    if key.vk == libtcod.KEY_0:
        return {'fov': 0}
    elif key.vk == libtcod.KEY_1:
        return {'fov': 1}
    elif key.vk == libtcod.KEY_2:
        return {'fov': 2}
    elif key.vk == libtcod.KEY_3:
        return {'fov': 3}
    elif key.vk == libtcod.KEY_4:
        return {'fov': 4}
    elif key.vk == libtcod.KEY_5:
        return {'fov': 5}
    elif key.vk == libtcod.KEY_6:
        return {'fov': 6}
    elif key.vk == libtcod.KEY_7:
        return {'fov': 7}
    elif key.vk == libtcod.KEY_8:
        return {'fov': 8}
    elif key.vk == libtcod.KEY_9:
        return {'fov': 9}

    # No key pressed
    else:
        return {}

