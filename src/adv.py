from room import Room
from player import Player
# Declare all the rooms


roomsDictionary = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

roomsDictionary['outside'].n_to = roomsDictionary['foyer']
roomsDictionary['foyer'].s_to = roomsDictionary['outside']
roomsDictionary['foyer'].n_to = roomsDictionary['overlook']
roomsDictionary['foyer'].e_to = roomsDictionary['narrow']
roomsDictionary['overlook'].s_to = roomsDictionary['foyer']
roomsDictionary['narrow'].w_to = roomsDictionary['foyer']
roomsDictionary['narrow'].n_to = roomsDictionary['treasure']
roomsDictionary['treasure'].s_to = roomsDictionary['narrow']


# user_input = input("to move type n,s,e or w : ")

# print(aaron.current_room.name)
# aaron.move(user_input)
# print(aaron.current_room.name)


# Main
#

# Make a new player object that is currently in the 'outside' roomsDictionary.

# Write a loop that:
#
# * Prints the current roomsDictionary name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the roomsDictionary there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


user_name = input('type in username: ')
user = Player(user_name, roomsDictionary['outside'])

user_input = input("to move type n,s,e or w : ")


while not user_input == 'q':
    if user_input == 'n' or 's' or 'e' or 'w':
        user.move(user_input)
        print(user.current_room.name)
        user_input = input("to move type n,s,e or w : ")
else:
    print('thanks for playing')
