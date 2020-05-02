import random

def generate_roles_list(players):
    def calculate_roles_quantity(player_numbers):
        roles_quantity = {}
        roles_quantity['mafia'] = round(player_numbers*0.23)
        roles_quantity['civilian'] = round(player_numbers*0.61)
        roles_quantity['doctor'] = round(player_numbers*0.08)
        roles_quantity['detective'] = round(player_numbers*0.08)
        return roles_quantity

    player_numbers = len(players)
    print('Players quantity:',player_numbers)
    roles_quantity = calculate_roles_quantity(player_numbers)
    print(roles_quantity,'\n')

    #generate list of all roles
    roles_list = []
    for role in roles_quantity:
        for i in range(roles_quantity[role]):
            roles_list.append(str(role))

    #shuffle them to make an arbitrary order
    random.shuffle(roles_list)
    for player in players:
        players[player] = roles_list.pop() #random.randint(0,player_numbers-1)


players = {'Denis':None,
                'DimaM':None,
                'TanyaP':None,
                'Danya':None,
                'NastyaSh':None,
                'TanyaR':None,
                'Sveta':None,
                'Ali':None,
                'Alice':None,
                'EgorM':None}

generate_roles_list(players)
for p in players:
    print(p,'-->',players[p])

