# Write a class to hold player information, e.g. what room they are in
# currently.

directions = {
    "n": "n_to",
    "s": "s_to",
    "e": "e_to",
    "w": "w_to"
}


class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room

    def move(self, movement):
        direction = directions[movement]
        next_room = getattr(self.current_room, direction)
        if not next_room:
            print("Error no room there")
        else:
            self.current_room = next_room
