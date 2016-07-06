import map_rooms
WALL = 'None'

Tutorial = {1:  {1: WALL,   2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:WALL,         7:WALL,             8:WALL,         9:WALL}, # 1
            2:  {1:WALL,    2:WALL,         3:map_rooms.rooms['F_ARMORY'],   4:map_rooms.rooms['F_DOJO'],     5:map_rooms.rooms['I_SHOP'],     6:map_rooms.rooms['I_KITCHEN'],  7:WALL,             8:WALL,         9:WALL}, # 2
            3:  {1:WALL,    2:map_rooms.rooms['R_HALL'],     3:map_rooms.rooms['R_ROOM'],     4:map_rooms.rooms['F_GUILD'],    5:map_rooms.rooms['I_BAR'],      6:map_rooms.rooms['I_HALL'],     7:map_rooms.rooms['T_STABLES'],      8:WALL,         9:WALL}, # 3
            4:  {1:WALL,    2:map_rooms.rooms['R_TRAIN'],    3:map_rooms.rooms['R_GUILD'],    4:map_rooms.rooms['ROAD1'],       5:map_rooms.rooms['T_SQUARE'],   6:map_rooms.rooms['ROAD2'],       7:map_rooms.rooms['ROAD3'],           8:map_rooms.rooms['T_GATES'],    9:WALL}, # 4
            5:  {1:WALL,    2:map_rooms.rooms['R_ROOM'],     3:map_rooms.rooms['S_ROOM'],     4:map_rooms.rooms['S_GUILD'],    5:map_rooms.rooms['ROAD4'],       6:map_rooms.rooms['T_MAYOR'],    7:map_rooms.rooms['T_GRAVEYARD'],    8:WALL,         9:WALL}, # 5
            6:  {1:WALL,    2:WALL,         3:map_rooms.rooms['S_TRAIN'],    4:map_rooms.rooms['S_LIB'],      5:map_rooms.rooms['C_GUILD'],    6:map_rooms.rooms['C_ROOM'],     7:map_rooms.rooms['SW_PUZZLE'],       8:WALL,         9:WALL}, # 6
            7:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:map_rooms.rooms['C_PEWS'],     6:map_rooms.rooms['C_TRAIN'],    7:map_rooms.rooms['SW_MONSTER'],      8:WALL,         9:WALL}, # 7
            8:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:map_rooms.rooms['C_STAGE'],    6:map_rooms.rooms['C_CONF'],     7:map_rooms.rooms['SW_LOCKED'],        8:WALL,         9:WALL}, # 8
            9:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:map_rooms.rooms['SW_TREASURE'], 7:map_rooms.rooms['SW_BOSS'],         8:map_rooms.rooms['SW_QI'],       9:WALL}, # 9
            10: {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:WALL,         7:WALL,             8:WALL,         9:WALL}  # 10
            }
