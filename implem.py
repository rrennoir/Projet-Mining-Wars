from termcolor import colored
import os


def create_data():
    """
    create all data structure for the game

    Return:
    -------
    vessel_stats : contains the information about the vessels of the players (lis)
    players-estate : contains the ore_amount, the vessels and the base of each player (list)
    environment_stats : contains the board size and the ore of each asteroid (dic)
    vessel_position : contains the position of each entire vessel into a list (list)
    asteroid_position : contains the position of each asteroid (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
            Schmetz Arnaud v.1 (28/03/2018)

    Impl: Schmetz Arnaud v.1 (11/03/2018)
            Ryan Rennoir V.1 (30/03/2018)
    """
    file = os.listdir('./')
    for file_name in file:

        if file_name.endswith('.mw'):
            with open(file_name) as cfg:
                game_config = cfg.readlines()
                cfg.close()

    if not('game_config' in locals()):
        return  # return nothing

    # create the empty vessel list
    vessel_stats = [{}, {}]
    vessel_position = [{}, {}]

    # create the player_estate dictionary
    player_estate = [{'ore_amount': 4, 'vessel': [],
                      'base': [int(game_config[3][0:str.find(game_config[3], ' ')]),
                               int(game_config[3][str.find(game_config[3], ' ') + 1:-1])]},
                     {'ore_amount': 4, 'vessel': [],
                      'base': [int(game_config[4][0:str.find(game_config[4], ' ')]),
                               int(game_config[4][str.find(game_config[4], ' ') + 1:-1])]}]

    # create the environment_stats dictionary, the asteroid_position and add the information about the asteroids on it
    environment_stats = {'board_size': (int(game_config[1][0:2]), int(game_config[1][3:5]))}
    asteroid_position = []

    for i in range(len(game_config) - 6):
        asteroid_name = 'asteroid' + str(i + 1)
        asteroid_info = game_config[i + 6].split()
        environment_stats.update(
            {asteroid_name: [[int(asteroid_info[0]), int(asteroid_info[1])], int(asteroid_info[2]), int(asteroid_info[3])]})
        asteroid_position.append([int(asteroid_info[0]), int(asteroid_info[1])])

    # create all starting position for a new vessel
    vessel_start_position = create_vessel_starting_position(player_estate)

    return vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position


def create_scout(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position):
    """
    create the scout and his positions

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
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'scout'

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

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

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

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
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'excavator_s'

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

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
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'excavator_m'

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

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
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'excavator_l'

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, 6, 0, 'unlock']})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_vessel_starting_position(player_estate):
    """
    Create at the start of the game all vessels position when they are bought

    Parameters:
    -----------
    player_estate : Player stats (list)

    Return:
    -------
    create_vessel_position: all position when a vessel is bought (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (16/03/2018)
    impl: Ryan Rennoir V.1 (23/03/2018)
    """
    create_vessel_position = []
    for player in range(2):
        base = player_estate[player]['base']

        # Scout
        position = []
        column_ref = base[1] + 1  # offset on  the top of the base
        for column in range(3):
            line_ref = base[0] - 1  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column

            for line in range(3):
                line = line_ref + line
                position.append([line, column])

        create_vessel_position.append({'scout': position})

        # Warship
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base
        for column in range(5):
            line_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column

            for line in range(5):
                line = line_ref + line

                if not ((line == 0 or line == 4) and (column == 0 or column == 4)):
                    position.append([line, column])

        create_vessel_position[player].update({'warship': position})

        # Excavator S
        create_vessel_position[player].update({'excavator_s': base})  # the vessel position is the base, nothing to do

        # Excavator M
        position = []
        column_ref = base[1] + 1  # offset on  the top of the base
        for column in range(3):
            line_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column

            for line in range(3):
                line = line_ref + column

                if not ((line == 0 or line == 2) and
                        (column == 0 or column == 2)):  # take only the line and column crossing by the base
                    position.append([line, column])

        create_vessel_position[player].update({'excavator_m': position})

        # Excavator L
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base
        for column in range(5):
            column = column_ref - column
            line_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner

            for line in range(5):
                line = line_ref + line

                if not ((line != 2) and (column != 2)):  # take only the line and column crossing the middle
                    position.append([line, column])

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
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    for elements in asteroid_position:
        if case == elements:
            return True
    return False


def check_base(player_estate, case):
    """
    Check if there is a base at this case

    Parameters:
    -----------
    player_estate: Player stats (list)
    case: position to test (list)

    Return:
    -------
    result: True if the position match, False if not (bool)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
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
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
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
    Spec: Ryan Rennoir V.1 (25/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
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
    Spec: Ryan Rennoir V.1 (25/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
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
    Impl: Ryan Rennoir V.1 (25/03/2018)
    """
    size = environment_stats['board_size']  # get the board size
    grid = []
    for line in range(size[1]):
        y_line = []

        for column in range(size[0]):
            color = 'white'
            case = [line + 1, column + 1]  # case to be check (+ 1 because start in 1,1 not in 0,0)

            if not check_base(player_estate, case):  # check if is a base
                if not check_asteroid(asteroid_position, case):  # check if it's a asteroid
                    if not check_vessel(vessel_position, case):  # check is it's a vessel

                        y_line += colored('□', color)  # it's nothing so blank case

                    else:
                        y_line += vessel_character(vessel_position, vessel_stats, case)  # it's a vessel

                else:
                    y_line += colored('▣', 'cyan')  # it's an asteroid

            else:

                if case == player_estate[0]['base']:
                    color = 'green'
                else:
                    color = 'red'

                y_line += colored('●', color)  # it's a base

        grid.append(y_line)  # add character to the line

    for line in grid:
        final_line = ''

        for characters in line:
            final_line += characters

        print(final_line)


def check_border(base, vessel_position):
    """
    Check if the vessel is not on a border

    Parameters:
    -----------
    base: base coordinate (list)
    vessel_position: contains the position of each entire vessel into a list (dic)

    Return:
    -------
    check_x:
    check_y:

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir V.1 (30/03/2018)
    """
    check_line = True
    check_column = True

    for position in vessel_position:
        if position[0] == base[0]:
            check_line = False

        if position[1] == base[1]:
            check_column = False

    return check_line, check_column


def move(vessel, player, vessel_stats, vessel_position, final_coordinate, environment_stats):
    """
    Move the vessel case per case in the right direction

    Parameters:
    -----------
    vessel: Name of the vessel (str)
    vessel_stats: contains the information about the vessels of the players (dic)
    vessel_position: contains the position of each entire vessel into a list (dic)
    final_coordinate: contains the final position of the vessel when a received an order (list)
    player: number of the player O or 1 (int)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir v.1 (30/03/2018)
    """
    position_line = vessel_stats[player][vessel][1][0]
    position_column = vessel_stats[player][vessel][1][1]

    destination_line = final_coordinate[player][vessel][0]
    destination_column = final_coordinate[player][vessel][1]

    base = environment_stats['board_side']

    check_line, check_column = check_border(base, vessel_position)

    if position_line != destination_line:
        delta_line = destination_line - position_line  # get the difference of case between the vessel and the destination
        direction = delta_line // abs(delta_line)  # get a 1 case move (positive or negative)

        if direction == 1 and check_line:
            for coordinate in range(len(vessel_position[player][vessel])):
                vessel_position[player][vessel][coordinate][0] += direction  # move the vessel in vessel_position

            vessel_stats[player][vessel][1][0] += direction  # move the vessel in vessel_stat

    if position_column != destination_column:
        delta_column = destination_column - position_column  # get the difference of case between the vessel and the destination
        direction = delta_column // abs(delta_column)  # get a 1 case move (positive or negative)

        if direction == 1 and check_column:
            for coordinate in range(len(vessel_position[player][vessel])):
                vessel_position[player][vessel][coordinate][1] += direction  # move the vessel in vessel_position

            vessel_stats[player][vessel][1][1] += direction  # move the vessel in vessel_stat


def game():
    """
    The game itself with the loop and all function call

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir v.1 (30/03/2018)
    """
    file = os.listdir('./')
    for file_name in file:

        if file_name.endswith('.cfg'):
            with open(file_name) as cfg:
                config = cfg.readlines()
                cfg.close()

    if not('config' in locals()):
        return  # get out of the game

    vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position = create_data()

    final_coordinate = [{'jean': [4, 4]}, {'louis': [12, 12]}]

    create_warship('jean', player_estate, 0, vessel_stats, vessel_position, vessel_start_position)
    create_scout('louis', player_estate, 1, vessel_stats, vessel_position, vessel_start_position)

    # move('jean', 0, vessel_stats, vessel_position, final_coordinate)
    # move('louis', 1, vessel_stats, vessel_position, final_coordinate)

    ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position)
