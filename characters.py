import json, os

#_____________________________Load Player__________________________________
with open(os.path.dirname(os.path.realpath(__file__)) + '/players.json') as player_file:
    player = json.load(player_file)

#_____________________________Load NPC__________________________________    
with open(os.path.dirname(os.path.realpath(__file__)) + '/npc.json') as npc_file:
    npc = json.load(npc_file)
    
#_____________________________Load Weapon__________________________________
with open(os.path.dirname(os.path.realpath(__file__)) + '/weapons.json') as weapon_file:
    weapon = json.load(weapon_file)
    