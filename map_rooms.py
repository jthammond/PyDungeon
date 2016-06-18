"""class ROOM(object):
    def __init__ (self, Name, Exits, Description):
        self.Name = Name
        self.Exits = Exits
        self.Description = Description


class I_BAR(ROOM):
    def __init__(self):
        self.Name = 'Inn Bar'
        self.Exits = ['North','East','South','West']
        self.Description = 'an empty bar with a few tables at the side. The bartender looks pissed.'

I_BAR = ROOM(I_BAR().Name, I_BAR().Exits, I_BAR().Description)
"""

import json, os

with open(os.path.dirname(os.path.realpath(__file__)) + '/rooms.json') as room_file:
    rooms = json.load(room_file)

# print map_rooms['I_BAR']
