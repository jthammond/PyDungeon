import map_rooms
WALL = 'None'

Tutorial = {1:  {1: WALL,   2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:WALL,         7:WALL,             8:WALL,         9:WALL}, # 1
            2:  {1:WALL,    2:WALL,         3:'F_ARMORY',   4:'F_DOJO',     5:'I_SHOP',     6:'I_KITCHEN',  7:WALL,             8:WALL,         9:WALL}, # 2
            3:  {1:WALL,    2:'R_HALL',     3:'R_ROOM',     4:'F_GUILD',    5:map_rooms.rooms['I_BAR'],      6:'I_HALL',     7:'T_STABLES',      8:WALL,         9:WALL}, # 3
            4:  {1:WALL,    2:'R_TRAIN',    3:'R_GUILD',    4:'ROAD',       5:map_rooms.rooms['T_SQUARE'],   6:'ROAD',       7:'ROAD',           8:'T_GATES',    9:WALL}, # 4
            5:  {1:WALL,    2:'R_ROOM',     3:'S_ROOM',     4:'S_GUILD',    5:'ROAD',       6:'T_MAYOR',    7:'T_GRAVEYARD',    8:WALL,         9:WALL}, # 5
            6:  {1:WALL,    2:WALL,         3:'S_TRAIN',    4:'S_LIB',      5:'C_GUILD',    6:'C_ROOM',     7:'C_PUZZLE',       8:WALL,         9:WALL}, # 6
            7:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:'C_PEWS',     6:'C_TRAIN',    7:'S_MONSTER',      8:WALL,         9:WALL}, # 7
            8:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:'C_STAGE',    6:'C_CONF',     7:'S_LOCKD',        8:WALL,         9:WALL}, # 8
            9:  {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:'S_TREASURE', 7:'S_BOSS',         8:'S_QI',       9:WALL}, # 9
            10: {1:WALL,    2:WALL,         3:WALL,         4:WALL,         5:WALL,         6:WALL,         7:WALL,             8:WALL,         9:WALL}  # 10
            }
