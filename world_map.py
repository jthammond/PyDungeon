import json, os

with open(os.path.dirname(os.path.realpath(__file__)) + '/rooms.json') as room_file:
    room = json.load(room_file)

Tutorial = {1:  {1:room['WALL'],  2:room['WALL'],    3:room['WALL'],     4:room['WALL'],    5:room['WALL'],     6:room['WALL'],        7:room['WALL'],        8:room['WALL'],    9:room['WALL']}, # 1
            2:  {1:room['WALL'],  2:room['WALL'],    3:room['F_ARMORY'], 4:room['F_DOJO'],  5:room['I_SHOP'],   6:room['I_KITCHEN'],   7:room['WALL'],        8:room['WALL'],    9:room['WALL']}, # 2
            3:  {1:room['WALL'],  2:room['R_HALL'],  3:room['R_ROOM'],   4:room['F_GUILD'], 5:room['I_BAR'],    6:room['I_HALL'],      7:room['T_STABLES'],   8:room['WALL'],    9:room['WALL']}, # 3
            4:  {1:room['WALL'],  2:room['R_TRAIN'], 3:room['R_GUILD'],  4:room['ROAD1'],   5:room['T_SQUARE'], 6:room['ROAD2'],       7:room['ROAD3'],       8:room['T_GATES'], 9:room['WALL']}, # 4
            5:  {1:room['WALL'],  2:room['R_ROOM'],  3:room['S_ROOM'],   4:room['S_GUILD'], 5:room['ROAD4'],    6:room['T_MAYOR'],     7:room['T_GRAVEYARD'], 8:room['WALL'],    9:room['WALL']}, # 5
            6:  {1:room['WALL'],  2:room['WALL'],    3:room['S_TRAIN'],  4:room['S_LIB'],   5:room['C_GUILD'],  6:room['C_ROOM'],      7:room['SW_PUZZLE'],   8:room['WALL'],    9:room['WALL']}, # 6
            7:  {1:room['WALL'],  2:room['WALL'],    3:room['WALL'],     4:room['WALL'],    5:room['C_PEWS'],   6:room['C_TRAIN'],     7:room['SW_MONSTER'],  8:room['WALL'],    9:room['WALL']}, # 7
            8:  {1:room['WALL'],  2:room['WALL'],    3:room['WALL'],     4:room['WALL'],    5:room['C_STAGE'],  6:room['C_CONF'],      7:room['SW_LOCKED'],   8:room['WALL'],    9:room['WALL']}, # 8
            9:  {1:room['WALL'],  2:room['WALL'],    3:room['WALL'],     4:room['WALL'],    5:room['WALL'],     6:room['SW_TREASURE'], 7:room['SW_BOSS'],     8:room['SW_QI'],   9:room['WALL']}, # 9
            10: {1:room['WALL'],  2:room['WALL'],    3:room['WALL'],     4:room['WALL'],    5:room['WALL'],     6:room['WALL'],        7:room['WALL'],        8:room['WALL'],    9:room['WALL']}  # 10
            }
