from termcolor import colored


def create_scout(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    create the scout and his positions

    Parameters:
    -----------
    vessel_position : The dictionary with all vessel position (dico)
    name : Name of the vessel (str)
    player : Player number 0 or 1 (int)
    player_estate : Player stats (list)
    vessel_stats : The dictionary with all vessel stats (dico)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)

    Version:
    --------
    Spec: Ryan Rennoir V.2 (23/03/2018)
    """
    vessel_type = 'scout'
    base = player_estate[player]['base']
    print(base)
    vessel_stats[player].update({name: [vessel_type, base, 3, 'NONE', 'NONE']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_warship(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    create the warship and his positions

    Parameters:
    -----------
    vessel_position : The dictionary with all vessel position (list)
    name : Name of the vessel (str)
    player : Player number 0 or 1 (int)
    player_estate : Player stats (list)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)

    Version:
    --------
    Spec: Ryan Rennoir V.2 (23/03/2018)
    """
    vessel_type = 'warship'
    base = player_estate[player]['base']
    vessel_stats[player].update({name: [vessel_type, base, 18, 'NONE', 'NONE']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_s(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    Create the excavator S and his positions.

    Parameters:
    -----------
    vessel_position : The dictionary with all vessel position (list)
    name : Name of the vessel (str)
    player : Player number 0 or 1 (int)
    player_estate : Player stats (list)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)

    Version:
    --------
    Spec: Ryan Rennoir V.2 (23/03/2018)
    """
    vessel_type = 'excavator_s'
    base = player_estate[player]['base']
    vessel_stats[player].update({name: [vessel_type, base, 2, 0, 'unlock']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_m(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    Create the excavator M and his positions.

    Parameters:
    -----------
    vessel_position : The dictionary with all vessel position (list)
    name : Name of the vessel (str)
    player : Player number 0 or 1 (int)
    player_estate : Player stats (list)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)

    Version:
    --------
    Spec: Ryan Rennoir V.2 (23/03/2018)
    """
    vessel_type = 'excavator_m'
    base = player_estate[player]['base']
    vessel_stats[player].update({name: [vessel_type, base, 3, 0, 'unlock']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_l(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    Create the excavator L and his positions.

    Parameters:
    -----------
    vessel_position : The dictionary with all vessel position (list)
    name : Name of the vessel (str)
    player : Player number 0 or 1 (int)
    player_estate : Player stats (list)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)

    Version:
    --------
    Spec: Ryan Rennoir V.2 (23/03/2018)
    """
    vessel_type = 'excavator_l'
    base = player_estate[player]['base']
    vessel_stats[player].update({name: [vessel_type, base, 6, 0, 'unlock']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_vessel_starting_position(player_estate):
    """
    Parameters:
    -----------
    player_estate : Player stats (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (16/03/2018)
    """
    create_vessel_position = []
    for player in range(2):
        base = player_estate[player]['base']

        # Scout
        position = []
        y_ref = base[1] + 1
        for line in range(3):
            x_ref = base[0] - 1
            y = y_ref - line

            for colone in range(3):
                x = x_ref + colone
                position.append([x, y])

        create_vessel_position.append({'scout': position})

        # Warship
        position = []
        y_ref = base[1] + 2
        for line in range(5):
            y = y_ref - line
            x_ref = base[0] - 2

            for colone in range(5):
                x = x_ref + colone

                if not ((line == 0 or line == 4) and (colone == 0 or colone == 4)):
                    position.append([x, y])

        create_vessel_position[player].update({'warship': position})

        # Excavator S
        create_vessel_position[player].update({'excavator_s': base})

        # Excavator M
        position = []
        y_ref = base[1] + 1
        for line in range(3):
            y = y_ref - line
            x_ref = base[0] - 1

            for colone in range(3):
                x = x_ref + colone

                if not ((line == 0 or line == 2) and (colone == 0 or colone == 2)):
                    position.append([x, y])

        create_vessel_position[player].update({'excavator_m': position})

        # Excavator L
        position = []
        y_ref = base[1] + 2
        for line in range(5):
            y = y_ref - line
            x_ref = base[0] - 2

            for colone in range(5):
                x = x_ref + colone

                if not ((line != 2) and (colone != 2)):
                    position.append([x, y])

        create_vessel_position[player].update({'excavator_l': position})

    return create_vessel_position


def check_asteroid(asteroid_position, case):
    """
    Check if there is an asteroid at this case
    Parameters:
    -----------
    asteroid_position: position of the asteroids (list)
    case: position to test (list)

    Return:
    -------
    result: True if the position match, False if not (bool)

    Version:
    --------
    Ryan Rennoir V.1 (23/03/2018)
    """
    for elements in asteroid_position:
        if case == elements:
            return True
    return False


def check_base(player_estate, case):
    """
    Parameters:
    -----------
    player_estate: Player stats (list)
    case: position to test (list)

    Return:
    -------
    result: True if the position match, False if not (bool)

    Version:
    --------
    Ryan Rennoir V.1 (23/03/2018)
    """
    for player in range(2):
        if case == player_estate[player]['base']:
            return True
    return False


def check_vessel(vessel_position, case):
    """
    Check if there are a vessel in this case
    Parameters:
    -----------
    vessel_position: position of all vessels (list)
    case: position to test (list)

    Return:
    -------
    result: True if the position match, False if not (bool)

    Version:
    --------
    Ryan Rennoir V.1 (23/03/2018)
    """
    for player in vessel_position:
        for vessels in player:
            for position in player[vessels]:
                if case == position:
                    return True
    return False


def check_vessel_type(vessel_position, vessel_stats, case):
    """
    check the type and the owner of the vessel

    Parameters:
    -----------
    vessel_position: position of all vessels (list)
    case: position to test (list)

    Return:
    -------
    Player_number: give the player number 1 or 2 (int)
    Type: give the type of vessel (str)

    Version:
    --------
    Ryan Rennoir V.1 (25/03/2018)
    """
    for player in range(2):

        for vessels in vessel_position[player]:
            for position in vessel_position[player][vessels]:
                if case == position:
                    vessels_type = vessel_stats[player][vessels][0]

                    return player, vessels_type


def vessel_character(vessel_position, vessel_stats, case):
    """
    Set the symbol and the color base on the player and type of vessel

    Parameters:
    -----------
    vessel_position: position of all vessels (list)
    case: position to test (list)

    Return:
    -------
    symbol: symbol with the right color to draw on the screen

    Version:
    --------
    Ryan Rennoir V.1 (25/03/2018)
    """
    player, vessel_type = check_vessel_type(vessel_position, vessel_stats, case)
    if player == 0:
        color = "green"
    else:
        color = 'red'

    if vessel_type == 'scout':
        symbol = '◇'
    elif vessel_type == 'warship':
        symbol = '△'
    else:
        symbol = '◎'

    return colored(symbol, color)


def ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position):
    """
    Calculate what to display in each tile of the board and display it with the information section
    and the legend section of the UI.

    Parameters:
    ----------
    vessel_stats : contains the information about the vessels of the players (dictionary)
    players_estate : contains the ore_amount, the vessels and the base of each player (dictionary)
    environment_stats : contains the board size and the ore of each asteroid (dictionary)
    vessel_position : contains the position of each entire vessel into a list (dictionary)
    asteroid_position : contains the position of each asteroid (list)

    Version:
    --------
    specification : Arnaud Schmetz (v.1 02/03/18) Ryan Rennoir (V.2 25/03/2018)
    """
    size = environment_stats['board_size']
    grid = []
    for line in range(size[1]):
        y_line = []

        for colone in range(size[0]):
            color = 'white'
            case = [colone + 1, line + 1]

            if not check_base(player_estate, case):
                if not check_asteroid(asteroid_position, case):
                    if not check_vessel(vessel_position, case):

                        y_line += colored('□', color)

                    else:
                        y_line += vessel_character(vessel_position, vessel_stats, case)

                else:
                    y_line += colored('▣', 'cyan')

            else:

                if case == player_estate[0]['base']:
                    color = 'green'
                else:
                    color = 'red'

                y_line += colored('●', color)

        grid.append(y_line)

    for line in grid:
        final_line = ''

        for characters in line:
            final_line += characters

        print(final_line)


def move(vessel, player, vessel_stats, vessel_position, final_coordinate):
    """
    Move the vessel case per case in the right direction

    Parameters:
    -----------
    vessel: Name of the vessel (str)
    vessel_stats:
    vessel_position:
    final_coordinate:
    player: number of the player O or 1 (int)
    """
    position_x = vessel_stats[player][vessel][1][0]
    position_y = vessel_stats[player][vessel][1][1]
    destination_x = final_coordinate[player][vessel][0]
    destination_y = final_coordinate[player][vessel][1]

    if position_x != destination_x:
        delta_x = destination_x - position_x
        direction = delta_x // delta_x

        vessel_stats[player][vessel][1][0] += direction

    if position_y != destination_y:
        delta_y = destination_y - position_y
        direction = delta_y // delta_y

        vessel_stats[player][vessel][1][1] += direction


asteroid_position = [[2, 6], [16, 7]]

player_estate = [{'ore_amount': 3, 'vessel': [], 'base': [5, 5]},
                 {'ore_amount': 9, 'vessel': [], 'base': [12, 12]}]

environment_stats = {'board_size': (20, 20),
                     'asteroid 1': [('x', 'y'), 'ore', 'ore/round'],
                     'asteroid 2': [('x', 'y'), 'ore', 'ore/round']}

vessel_stats = [{}, {}]

vessel_position = [{}, {}]

final_coordinate = [{'jean': [5, 4]}, {'louis': [12, 12]}]

vessel_start_position = create_vessel_starting_position(player_estate)
create_warship('jean', player_estate, 0, vessel_stats, vessel_position, vessel_start_position)
create_scout('louis', player_estate, 1, vessel_stats, vessel_position, vessel_start_position)

print(vessel_stats)
move('jean', 0, vessel_stats, vessel_position, final_coordinate)
move('louis', 1, vessel_stats, vessel_position, final_coordinate)
print(vessel_stats)
print(player_estate)  # base has moved like the center ...
ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position)
