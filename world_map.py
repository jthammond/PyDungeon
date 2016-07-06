import json, os

with open(os.path.dirname(os.path.realpath(__file__)) + '/rooms.json') as room_file:
    rooms = json.load(room_file)

Tutorial = {1:  {1: rooms['WALL'], 2:rooms['WALL'],    3:rooms['WALL'],     4:rooms['WALL'],    5:rooms['WALL'],     6:rooms['WALL'],        7:rooms['WALL'],        8:rooms['WALL'],    9:rooms['WALL']}, # 1
            2:  {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['F_ARMORY'], 4:rooms['F_DOJO'],  5:rooms['I_SHOP'],   6:rooms['I_KITCHEN'],   7:rooms['WALL'],        8:rooms['WALL'],    9:rooms['WALL']}, # 2
            3:  {1:rooms['WALL'],  2:rooms['R_HALL'],  3:rooms['R_ROOM'],   4:rooms['F_GUILD'], 5:rooms['I_BAR'],    6:rooms['I_HALL'],      7:rooms['T_STABLES'],   8:rooms['WALL'],    9:rooms['WALL']}, # 3
            4:  {1:rooms['WALL'],  2:rooms['R_TRAIN'], 3:rooms['R_GUILD'],  4:rooms['ROAD1'],   5:rooms['T_SQUARE'], 6:rooms['ROAD2'],       7:rooms['ROAD3'],       8:rooms['T_GATES'], 9:rooms['WALL']}, # 4
            5:  {1:rooms['WALL'],  2:rooms['R_ROOM'],  3:rooms['S_ROOM'],   4:rooms['S_GUILD'], 5:rooms['ROAD4'],    6:rooms['T_MAYOR'],     7:rooms['T_GRAVEYARD'], 8:rooms['WALL'],    9:rooms['WALL']}, # 5
            6:  {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['S_TRAIN'],  4:rooms['S_LIB'],   5:rooms['C_GUILD'],  6:rooms['C_ROOM'],      7:rooms['SW_PUZZLE'],   8:rooms['WALL'],    9:rooms['WALL']}, # 6
            7:  {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['WALL'],     4:rooms['WALL'],    5:rooms['C_PEWS'],   6:rooms['C_TRAIN'],     7:rooms['SW_MONSTER'],  8:rooms['WALL'],    9:rooms['WALL']}, # 7
            8:  {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['WALL'],     4:rooms['WALL'],    5:rooms['C_STAGE'],  6:rooms['C_CONF'],      7:rooms['SW_LOCKED'],   8:rooms['WALL'],    9:rooms['WALL']}, # 8
            9:  {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['WALL'],     4:rooms['WALL'],    5:rooms['WALL'],     6:rooms['SW_TREASURE'], 7:rooms['SW_BOSS'],     8:rooms['SW_QI'],   9:rooms['WALL']}, # 9
            10: {1:rooms['WALL'],  2:rooms['WALL'],    3:rooms['WALL'],     4:rooms['WALL'],    5:rooms['WALL'],     6:rooms['WALL'],        7:rooms['WALL'],        8:rooms['WALL'],    9:rooms['WALL']}  # 10
            }
