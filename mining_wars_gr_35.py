from termcolor import colored
import os
import configparser
from random import randint


def create_data(config):
    """
    create all data structure for the game

    Parameter:
    ----------
    config: contain he configuration of the game itself

    Return:
    -------
    data: list with all data structure (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
            Schmetz Arnaud v.1 (28/03/2018)

    Impl: Schmetz Arnaud v.1 (11/03/2018)
            Ryan Rennoir V.1 (30/03/2018)
    """
    file = os.listdir('./')
    game_config = ''  # To make pycharm happy (game_config may be not defined / referenced)
    for file_name in file:

        if file_name.endswith('.mw'):
            with open(file_name) as cfg:
                game_config = cfg.readlines()
                cfg.close()

    # create the empty vessel list
    vessel_stats = [{}, {}]
    vessel_position = [{}, {}]

    ore = config['general'][2]
    base_hp = config['general'][3]

    # create the player_estate dictionary
    player_estate = [{'ore_amount': ore, 'vessel': [],
                      'base': [int(game_config[3][0:game_config[3].find(' ')]),
                               int(game_config[3][game_config[3].find(' ') + 1:-1])],
                      'base_hp': base_hp},

                     {'ore_amount': ore, 'vessel': [],
                      'base': [int(game_config[4][0:game_config[4].find(' ')]),
                               int(game_config[4][game_config[4].find(' ') + 1:-1])],
                      'base_hp': base_hp}]

    # create the environment_stats dictionary, the asteroid_position and add the information about the asteroids on it
    environment_stats = {'board_size': (int(game_config[1][0:2]), int(game_config[1][3:5]))}
    asteroid_position = []

    _asteroid = []
    for i in range(len(game_config) - 6):
        asteroid_info = game_config[i + 6].split()

        asteroid_coord = [int(asteroid_info[0]),  int(asteroid_info[1])]
        asteroid_max_ore = int(asteroid_info[2])
        ore_output = int(asteroid_info[3])

        _asteroid += [[asteroid_coord, asteroid_max_ore, ore_output]]

        asteroid_position.append([int(asteroid_info[0]), int(asteroid_info[1])])

    environment_stats.update({'asteroid': _asteroid})

    # create all starting position for a new vessel
    vessel_start_position = create_vessel_starting_position(player_estate)
    base_position = create_base_position(player_estate)

    # Just one line to return
    data = [vessel_stats, player_estate, environment_stats, vessel_position,
            asteroid_position, vessel_start_position, base_position]

    return data


def create_base_position(player_estate):
    """
    Create the position around the portal/base.

    Parameters :
    ------------
    player_estate : Players stats (list)
    
    Version :
    ---------
    Spec: Ryan Rennoir V.1 (3/04/2018)
    Impl: Ryan Rennoir V.1 (3/04/2018)
    """
    base_position = []

    for player in player_estate:
        base = player['base']

        position = []
        column_ref = base[1] + 2  # offset on  the top

        for column_nb in range(5):

            row_ref = base[0] - 2  # offset on the left, now offset on the top left corner
            column = column_ref - column_nb

            for row_nb in range(5):

                row = row_ref + row_nb
                position.append([row, column])

        base_position.append(position)

    return base_position


def check_ore_account(player, player_estate, price):
    """
    Check if the player has enough ore to buy the vessel he wants to buy, and if he has, take the ore.
    
    Parameters :
    ------------
    player : Player number 0 or 1 (int)
    player_estate : contains the ore_amount, the vessels and the base of each player (list)
    price : the price of the vessel (int)
    
    Version :
    ---------
    spec : Arnaud Schmetz v.1 (12/04/2018)
    impl : Ryan Rennoir v.1 (11/04/2018)
    """
    player_account = player_estate[player]['ore_amount']

    if price > player_account:
        return False
    else:
        player_estate[player]['ore_amount'] -= price
        return True


def create_scout(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Spawn the scout.

    Parameters:
    -----------
    name : Name of the vessel (str)
    player_estate : Player stats (list)
    player : Player number 0 or 1 (int)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_position : The dictionary with all vessel position (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)
    config: contain the configuration the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'scout'

    price = config[vessel_type][5]
    if not check_ore_account(player, player_estate, price):
        return

    life = config[vessel_type][0]
    tonnage = 0

    if config[vessel_type][3]:
        locking = 'release'
    else:
        locking = None

    row = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [row, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_warship(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Spawn the warship.

    Parameters:
    -----------
    name : Name of the vessel (str)
    player_estate : Player stats (list)
    player : Player number 0 or 1 (int)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_position : The dictionary with all vessel position (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)
    config: contain the configuration the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    vessel_type = 'warship'

    price = config[vessel_type][5]
    if not check_ore_account(player, player_estate, price):
        return

    life = config[vessel_type][0]
    tonnage = 0

    if config[vessel_type][3]:
        locking = 'release'
    else:
        locking = None

    row = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [row, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_s(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Spawn the excavator S.

    Parameters:
    -----------
    name : Name of the vessel (str)
    player_estate : Player stats (list)
    player : Player number 0 or 1 (int)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_position : The dictionary with all vessel position (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)
    config: contain the configuration the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    # config
    vessel_type = 'excavator-S'

    price = config[vessel_type][5]
    if not check_ore_account(player, player_estate, price):
        return

    life = config[vessel_type][0]
    tonnage = 0

    if config[vessel_type][3]:
        locking = 'release'
    else:
        locking = None

    row = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [row, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_m(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Spawn the excavator M.

    Parameters:
    -----------
    name : Name of the vessel (str)
    player_estate : Player stats (list)
    player : Player number 0 or 1 (int)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_position : The dictionary with all vessel position (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)
    config: contain the configuration the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    # config
    vessel_type = 'excavator-M'

    price = config[vessel_type][5]
    if not check_ore_account(player, player_estate, price):
        return

    life = config[vessel_type][0]
    tonnage = 0

    if config[vessel_type][3]:
        locking = 'release'
    else:
        locking = None

    row = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [row, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_l(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Spawn the excavator L

    Parameters:
    -----------
    name : Name of the vessel (str)
    player_estate : Player stats (list)
    player : Player number 0 or 1 (int)
    vessel_stats : The dictionary with all vessel stats (list)
    vessel_position : The dictionary with all vessel position (list)
    vessel_start_position : list made at the start of the game with all the starting position of the vessels(list)
    config: contain the configuration the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (23/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    # config
    vessel_type = 'excavator-L'

    price = config[vessel_type][5]
    if not check_ore_account(player, player_estate, price):
        return

    life = config[vessel_type][0]
    tonnage = 0

    if config[vessel_type][3]:
        locking = 'release'
    else:
        locking = None

    row = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [row, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_vessel_starting_position(player_estate):
    """
    Create at the start of the game all vessels position when they are bought.

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

        for column_nb in range(3):

            row_ref = base[0] - 1  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for row_nb in range(3):

                row = row_ref + row_nb
                position.append([row, column])

        create_vessel_position.append({'scout': position})

        # Warship
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base

        for column_nb in range(5):

            row_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for row_nb in range(5):
                row = row_ref + row_nb

                if not ((row_nb == 0 or row_nb == 4) and (column_nb == 0 or column_nb == 4)):
                    position.append([row, column])

        create_vessel_position[player].update({'warship': position})

        # Excavator S
        # the vessel position is the base
        create_vessel_position[player].update({'excavator-S': [[base[0],  base[1]]]})

        # Excavator M
        position = []
        column_ref = base[1] + 1  # offset on  the top of the base

        for column_nb in range(3):

            row_ref = base[0] - 1  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for row_nb in range(3):
                row = row_ref + row_nb

                if not ((row_nb == 0 or row_nb == 2) and

                        (column_nb == 0 or column_nb == 2)):  # take only the row and column crossing by the base
                    position.append([row, column])

        create_vessel_position[player].update({'excavator-M': position})

        # Excavator L
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base

        for column_nb in range(5):

            column = column_ref - column_nb
            row_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner

            for row_nb in range(5):
                row = row_ref + row_nb

                if not ((row_nb != 2) and (column_nb != 2)):  # take only the row and column crossing the middle
                    position.append([row, column])

        create_vessel_position[player].update({'excavator-L': position})

    return create_vessel_position


def check_asteroid(asteroid_position, case):
    """
    Check if there is an asteroid at this case.

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
    for asteroid in asteroid_position:

        if case == asteroid:
            return True

    return False


def check_base(player_estate, case):
    """
    Check if there is a base at this case.

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
    Check if there are a vessel in this case.

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
    Check the type and the owner of the vessel.

    Parameters:
    -----------
    vessel_position: position of all vessels (list)
    vessel_stats: contain all stats of the vessels (list)
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
    vessel_stats: contain all stats of the vessels (list)
    case: position to test (list)

    Return:
    -------
    symbol: symbol with the right color to print on the screen

    Version:
    --------
    Spec: Ryan Rennoir V.1 (25/03/2018)
    Impl: Ryan Rennoir V.1 (23/03/2018)
    """
    player, vessel_type = check_vessel_type(vessel_position, vessel_stats, case)

    # Check the player color
    if player == 0:
        color = "green"
    else:
        color = 'red'

    # Check the vessel types
    if vessel_type == 'scout':
        symbol = '◇'
    elif vessel_type == 'warship':
        symbol = '△'
    else:
        symbol = '◎'

    return colored(symbol, color)


def game_stats_ui(vessel_stats, player_estate, environment_stats):
    """
    Create the list with all of the information the print on the right side of the screen/window during the game.

    Parameters:
    -----------
    vessel_stats: contain all stats of the vessels (list)
    player_estate: contain all of stats about the player (list)
    environment_stats: contain all information of the game (dic)

    Return:
    -------
    result: stats to print on the right side of the screen/window

    Version:
    --------
    spec: Ryan Rennoir V.1 (07/04/2018)
    Impl: Ryan Rennoir V.1 (07/04/2018)
    """
    # Init _ui
    _ui = ['Asteroid:']

    # Add ever asteroid in the game
    _asteroid = environment_stats['asteroid']
    for asteroid in _asteroid:

        asteroid_coord = asteroid[0]
        asteroid_ore = asteroid[1]
        asteroid_throughput = asteroid[2]

        _ui.append('In %s with %s ore at %s/round' % (asteroid_coord, asteroid_ore, asteroid_throughput))

    # Pass a line
    _ui += ' '

    # Stats for players
    for player in range(2):

        ore_amount = player_estate[player]['ore_amount']

        _ui.append('Player %s with %s ore:' % (player + 1, ore_amount))

        base_hp = player_estate[player]['base_hp']
        base_coord = [player_estate[player]['base'][0], player_estate[player]['base'][1]]

        _ui.append('Base at %s with %s HP' % (base_coord, base_hp))

        # Add ever vessel for each player
        for vessel in vessel_stats[player]:
            vessel_info = vessel_stats[player][vessel]

            vessel_type = str(vessel_info[0])
            vessel_coord = str(vessel_info[1])
            vessel_hp = str(vessel_info[2])
            vessel_ore = str(vessel_info[3])
            vessel_state = str(vessel_info[4])

            _ui.append('%s is a %s at %s:' % (vessel, vessel_type, vessel_coord))

            _ui.append(' with %s HP, %s ore and state = %s' % (vessel_hp, vessel_ore, vessel_state))

        # Pass a line between players
        _ui += ' '

    return _ui


def check_base_outside(case, base_position):
    """
    Check if the case is the portal/base outside.

    Parameters:
    -----------
    case: case to check (list)
    base_position: contain all of the portal/base position (list)

    Return:
    -------
    Color: color of the player base/portal

    Version:
    Spec: Ryan Rennoir V.1 (7/04/2018)
    Imp: Ryan Rennoir V.1 (7/04/2018)
    """
    color = 'white'
    for player in range(2):
        for position in base_position[player]:
            if case == position:
                if player == 0:
                    color = 'green'
                else:
                    color = 'red'

    return color


def ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position, base_position):
    """
    Calculate what to display in each tile of the board and display it with the information section
    and the legend section of the UI.

    Parameters:
    -----------
    vessel_stats : contains the information about the vessels of the players (list)
    players_estate : contains the ore_amount, the vessels and the base of each player (list)
    vessel_position : contains the position of each entire vessel into a list (list)
    environment_stats : contains the board size and the ore of each asteroid (dictionary)
    asteroid_position : contains the position of each asteroid (list)

    Version:
    --------
    Spec: Arnaud Schmetz (v.1 02/03/18)
            Ryan Rennoir (V.2 25/03/2018)
    Impl: Ryan Rennoir V.1 (25/03/2018)
    """
    size = environment_stats['board_size']  # get the board size
    grid = []  # Init the grid
    for row in range(size[1]):
        y_row = []

        for column in range(size[0]):
            case = [row + 1, column + 1]  # case to be check (+ 1 because start in 1,1 not in 0,0)

            if not check_base(player_estate, case):  # check if is a base
                if not check_asteroid(asteroid_position, case):  # check if it's a asteroid
                    if not check_vessel(vessel_position, case):  # check is it's a vessel
                        # it's nothing or the base outside(not the center)
                        y_row += colored('□', check_base_outside(case, base_position))

                    else:
                        y_row += vessel_character(vessel_position, vessel_stats, case)  # it's a vessel

                else:
                    y_row += colored('▣', 'cyan')  # it's an asteroid

            else:

                # Check ii it's the player 1 base and put the right color
                if case == player_estate[0]['base']:
                    color = 'green'  # Player 1 base

                else:
                    color = 'red'  # Player 2 base

                y_row += colored('●', color)  # it's a base

        grid.append(y_row)  # add character to the row

    # Get the stats to print
    stats = game_stats_ui(vessel_stats, player_estate, environment_stats)

    # Init the index for the stats to print on the right
    row_index = 0
    for row in grid:
        # Init the row to print
        final_row = ''

        for characters in row:
            final_row += characters

        # Add statistic
        # Try if the index is not out of range
        try:
            stats_to_print = stats[row_index]

        # Index out of range print nothing
        except IndexError:
            stats_to_print = ''

        # Print row per row the board with stats on the right
        print(final_row + ' ', stats_to_print)

        # Add 1 to the index
        row_index += 1

    # Print the legends at the end
    print('Color: Green Player 1, Red Player 2\n'
          'Characters:  □ Nothing, ● Base, ▣ Asteroid, ◎ Excavator, ◇ Scout, △ Warship\n')


def check_border(type_axis, vessel_position, board, direction):
    """
    Check if the vessel stay in the board.

    Parameters:
    -----------
    type_axis: row or column to check (str)
    vessel_position: contains the position of each entire vessel into a list (list)
    board: size of the game board (list)
    direction: move to check (int)

    Return:
    -------
    result: False if the vessel go outside , true otherwise

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir V.1 (04/04/2018)
    """

    if type_axis == 'row':
        for position in vessel_position:
            if position[0] + direction > board[0] or position[0] + direction < 1:
                return False
    else:
        for position in vessel_position:
            if position[1] + direction > board[1] or position[1] + direction < 1:
                return False

    return True


def move(vessel_stats, vessel_position, final_coordinate, environment_stats, config):
    """
    Move the vessel case per case in the right direction.

    Parameters:
    -----------
    vessel_stats: contains the information about the vessels of the players (list)
    vessel_position: contains the position of each entire vessel into a list (list)
    final_coordinate: contains the final position of the vessel when a received an order (list)
    environment_stats: contain all of the information of the game (dic)
    config: contain the configuration of the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir v.1 (30/03/2018)
    """
    case = config['general'][0]

    to_remove = [[], []]

    if final_coordinate == [{}, {}]:
        return

    for player in range(2):
        for vessel in final_coordinate[player]:

            # Check if the vessel still exist
            if vessel in vessel_stats[player]:
                position_row = vessel_stats[player][vessel][1][0]
                position_column = vessel_stats[player][vessel][1][1]

                destination_row = final_coordinate[player][vessel][0]
                destination_column = final_coordinate[player][vessel][1]

                board = environment_stats['board_size']

                # Check if the vessel can move and exist
                if vessel_stats[player][vessel][4] != 'lock':

                    # Check if the vessel is not already on the position
                    if final_coordinate[player][vessel] != vessel_stats[player][vessel][1]:

                        # Check if the vessel is not already on the row
                        if position_row != destination_row:
                            delta_row = destination_row - position_row

                            # Check if the move is negative
                            if delta_row < 0:
                                direction = case * - 1
                            else:
                                direction = case

                            # Check if not on a border
                            if check_border('row', vessel_position[player][vessel], board, direction):
                                for coordinate in vessel_position[player][vessel]:
                                    coordinate[0] += direction  # move the vessel in vessel_position

                                vessel_stats[player][vessel][1][0] += direction  # move the vessel in vessel_stat

                        # Check if the vessel is not already on the column
                        if position_column != destination_column:
                            # get the difference of case between the vessel and the destination
                            delta_column = destination_column - position_column

                            # check if the move is negative
                            if delta_column < 0:
                                direction = case * - 1
                            else:
                                direction = case

                            # Check if not on the border
                            if check_border('column', vessel_position[player][vessel], board, direction):
                                for coordinate in vessel_position[player][vessel]:
                                    coordinate[1] += direction  # move the vessel in vessel_position

                                vessel_stats[player][vessel][1][1] += direction  # move the vessel in vessel_stat
                    else:
                        # Removed because already on the case
                        to_remove[player].append(vessel)
                else:
                    # Removed because is locked
                    to_remove[player].append(vessel)
            else:
                # Removed because din't exist
                to_remove[player].append(vessel)

    # Remove the target coordinate
    for _player in range(2):
        for _vessel in to_remove[_player]:
            final_coordinate[_player].pop(_vessel)


def hit_enemy(vessels, attacker, vessel_stats, player, vessel_dmg):
    """
    Check if the vessel hit is different than the attacker.

    Parameters:
    -----------
    vessels: name of the vessel hit (str)
    attacker: name of the attacker (str)
    vessel_stats: contain all stats of the vessels (list)
    player: player who attack 0 or 1 (int)
    vessel_dmg: damage of the attacker (int)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (2/04/2018)
    Imp: Ryan Rennoir V.1 (2/04/2018)
    """
    # Check is the vessel hit it isn't itself and remove the hp
    if vessels != attacker:
        vessel_stats[player][vessels][2] -= vessel_dmg


def remove_vessel(vessel_stats, vessel_position, player_estate):
    """
    Check if there is vessels dead and delete them if yes.

    Parameters:
    -----------
    vessel_stats: contain all stats of the vessels (list)
    vessel_position: contain all position of the vessels (list)
    player_estate: contain all of the information about the players (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (12/04/2018)
    imp: Ryan Rennoir V.1 (12/04/2018)
    """
    vessels_to_remove = [[], []]

    for player in range(2):
        for vessels in vessel_stats[player]:

            if vessel_stats[player][vessels][2] <= 0:
                    vessels_to_remove[player].append(vessels)

        for _vessels in vessels_to_remove[player]:
            del vessel_stats[player][_vessels]
            del vessel_position[player][_vessels]
            player_estate[player]['vessel'].remove(_vessels)


def hit_base(player, coord, player_estate, base_position, dmg):
    """
    Check if the base has been it

    Parameters:
    -----------
    player: player who attack 0 or 1 (int)
    coord: coordinate of the attack (list)
    player_estate: contain all the information about the players (list)
    base_position: contain all of the base/portals position (list)
    dmg: damage of the vessel who attack (int)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (2/04/2018)
    Imp: Ryan Rennoir V.1 (2/04/2018)
    """
    if player == 1:
        player_base = 0
    else:
        player_base = 1

    for position in base_position[player_base]:
        if position == coord:
            player_estate[player_base]['base_hp'] -= dmg


def attack(player, attacker, coord, vessel_stats, vessel_position, player_estate, base_position, config):
    """
    Make the attack of a vessel on the targeted coordinates 
    
    Parameters:
    -----------
    player: Player number 0 or 1 of the attacker(int)
    attacker: name of the vessel which is making the attack (str)
    coord: coordinates of the place the vessel is attacking (list)
    vessel_stats: The dictionary with all vessel stats (list)
    vessel_position: The dictionary with all vessel position (list)
    player_estate: Player stats (list)
    base_position: contain all of the position of the base/portals (list)
    config: contain the configuration of the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (2/04/2018)
    Imp: Ryan Rennoir V.1 (2/04/2018)
    """
    # Get the range from the config.
    vessel_type = vessel_stats[player][attacker][0]
    vessel_range = config[vessel_type][1]

    center = vessel_stats[player][attacker][1]
    vessel_dmg = config[vessel_type][4]

    # Measures the Manhattan distance(|row_b - row_a| + |column_b - column_a|)
    delta_row = abs(coord[0] - center[0]) + abs(coord[1] - center[1])

    # Check if out of range
    if delta_row > vessel_range:
        return

    hit_base(player, coord, player_estate, base_position, vessel_dmg)

    # Check if there is a vessel at this coordinate and made the shoot.
    for player in range(2):
        for vessels in vessel_position[player]:
            for position in vessel_position[player][vessels]:

                # Check when position match
                if position == coord:
                    hit_enemy(vessels, attacker, vessel_stats, player, vessel_dmg)

    # Check if there is vessels dead and delete them if yes
    remove_vessel(vessel_stats, vessel_position, player_estate)


def get_ore(vessel_stats, player_estate, environment_stats, config):
    """
    Take ore out of an asteroid and give him to the vessel or transfer the ore from a vessel to the base.

    Parameters:
    -----------
    vessel_stats: contains the information about the vessels of the players (list)
    players_estate: contains the ore_amount, the vessels and the base of each player (list)
    environment_stats: contains the board size and the ore of each asteroid (dictionary)
    config: contains all configuration for the game (dic)

    Version:
    --------
    spec: Arnaud Schmetz (v.1 02/03/18)
    impl: Arnaud Schmetz (v.1 11/04/18)
    """
    # Make a dictionary to sort the vessels locked by asteroid, making easier any fair redistribution if an
    #  asteroid don't have enough ore
    vessels_by_asteroid = {}
    for asteroid in environment_stats['asteroid']:
        # {'asteroid_coordinates' : [[vessels], index_of_the_asteroid_in_environment_stats, total_ore_needed
        # _for_the_vessels, amount_of_vessels_needing_ore] , .... }
        # in which vessels are under the form : [name, ore_to_get_from_the_asteroid, player_index]
        #    ----- player_index is the index of the player's vessels in the other structures

        asteroid_coord_row = asteroid[0][0]
        asteroid_coord_column = asteroid[0][1]
        index_dic_asteroid = str(asteroid_coord_row) + '-' + str(asteroid_coord_column)

        asteroid_index = environment_stats['asteroid'].index(asteroid)

        vessels_by_asteroid.update({index_dic_asteroid: [[], asteroid_index, 0, 0]})

    # Transfer the ore between the vessels and the base and sort the vessels locked, by asteroid
    for player in vessel_stats:
        player_index = vessel_stats.index(player)

        for vessel in player:
            # Check if vessel is lock
            if player[vessel][4] == 'lock':
                # Check if the vessel is on the base
                if player[vessel][1] == player_estate[player_index]['base']:

                    # Remove the ore from the vessel and put it in the base
                    player_estate[player_index]['ore_amount'] += player[vessel][3]
                    vessel_stats[player_index][vessel][3] = 0

                # sort the vessels locked, by asteroid, after computing how many ore each vessel should get,
                #  regardless of the ore remaining on asteroids
                else:
                    coordinates = str(player[vessel][1][0]) + '-' + str(player[vessel][1][1])

                    # if free space on the board >= ore obtainable per round : ore_to_get = ore obtainable
                    # per round, else ore_to_get = free space on the board
                    max_ore_vessel = config[vessel_stats[player_index][vessel][0]][2]
                    ore_in_vessel = player[vessel][3]
                    asteroid_index = vessels_by_asteroid[coordinates][1]
                    ore_in_asteroid = environment_stats['asteroid'][asteroid_index][2]

                    # if free space on the board >= ore obtainable per round
                    if max_ore_vessel - ore_in_vessel >= ore_in_asteroid:
                        ore_to_get = ore_in_asteroid

                    # ore_to_get = free space on the board
                    else:
                        ore_to_get = max_ore_vessel - ore_in_vessel

                    vessels_by_asteroid[coordinates][0].append([vessel, ore_to_get, player_index])
                    vessels_by_asteroid[coordinates][2] += ore_to_get
                    vessels_by_asteroid[coordinates][3] += 1

    # Makes the transfer from the asteroids to the vessels
    for asteroid in vessels_by_asteroid:

        # if asteroid has enough ore : make the transfers normally
        if vessels_by_asteroid[asteroid][2] <= environment_stats['asteroid'][vessels_by_asteroid[asteroid][1]][1]:
            environment_stats['asteroid'][vessels_by_asteroid[asteroid][1]][1] -= vessels_by_asteroid[asteroid][2]
            for vessel in vessels_by_asteroid[asteroid][0]:
                vessel_stats[vessel[2]][vessel[0]][3] += vessel[1]

        # if asteroid doesn't have enough ore, share it between the vessels
        else:
            asteroid_ore = environment_stats['asteroid'][vessels_by_asteroid[asteroid][1]][1]

            while asteroid_ore != 0:
                shared_ore = asteroid_ore / vessels_by_asteroid[asteroid][3]

                for vessel in vessels_by_asteroid[asteroid]:

                    # if the vessel can get the amount of ore, equitably shared, make the transfer
                    if shared_ore <= vessel[1]:
                        asteroid_ore -= shared_ore
                        vessel_stats[vessel[2]][vessel[0]][3] += shared_ore
                        vessels_by_asteroid[asteroid][vessels_by_asteroid[asteroid].index(vessel)][1] -= shared_ore

                        if vessels_by_asteroid[asteroid][vessels_by_asteroid[asteroid].index(vessel)][1] == 0:
                            vessels_by_asteroid[asteroid][3] -= 1

                    # else, give him the max of ore the vessel can get, letting a little bit more ore to share
                    # for the others and so leafing through the while loop again
                    else:
                        environment_stats['asteroid'][vessels_by_asteroid[asteroid][1]][1] -= vessel[1]
                        vessel_stats[vessel[2]][vessel[0]][3] += vessel[1]
                        vessels_by_asteroid[asteroid][vessels_by_asteroid[asteroid].index(vessel)][1] -= vessel[1]
                        vessels_by_asteroid[asteroid][3] -= 1


def get_order(order, vessel_stats, player_estate, environment_stats, vessel_position, final_coordinate,
              vessel_start_position, asteroid_position, base_position, config):
    """
    Read the instructions give by the player and execute the function

    Parameters:
    -----------
    order: Instruction of the player (list)
    vessel_stats: contains the information about the vessels of the players (list)
    player_estate: contains the ore_amount, the vessels and the base of each player (list)
    environment_stats: contains the board size and the ore of each asteroid (dic)
    vessel_position: contains the position of each entire vessel into a list (list)
    final_coordinate: contains the final position of the vessel when a received an order (list)
    vessel_start_position: contains all of the vessel starting position (list)
    asteroid_position: contain all of the asteroid position (list)
    base_position: contain all of the portals/base position (list)
    config: contain all of the configuration of the game (dic)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
          Arnaud Schmetz V.2 (30/03/2018)
    Impl: Arnaud Schmetz v.1 (26/03/2018)
    """
    split_orders = []

    for player_orders in order:
        split_orders.append(player_orders.split())

    # scroll through the orders of each player and execute each buy order encountered (first turn phase)
    buy_types = {'scout': ('scout', create_scout),
                 'warship': ('warship', create_warship),
                 'excavator-M': ('excavator-M', create_excavator_m),
                 'excavator-S': ('excavator-S', create_excavator_s),
                 'excavator-L': ('excavator-L', create_excavator_l)}

    # Check false order (without the ':')
    false_order = [[], []]
    for player in split_orders:
        player_index = split_orders.index(player)

        # Find the :
        for order in player:
            if order.find(':') == -1:

                # Add to the list to be deleted
                false_order[player_index].append(order)

    # Delete false order
    for player in range(2):
        for elements in false_order[player]:
            split_orders[player].remove(elements)

    # Check if a player buy a vessel
    for player_orders in split_orders:
        for single_order in player_orders:
            for buy_type in buy_types:

                index_order = single_order.find(':')
                vessel_type_to_buy = single_order[index_order:]

                if vessel_type_to_buy.find(buy_type) != -1:

                    # Get the vessel name
                    vessel_name = single_order[:index_order]

                    # Buy the vessel
                    player = split_orders.index(player_orders)
                    if not(vessel_name in vessel_stats[player]):

                        buy_types[buy_type][1](vessel_name, player_estate, player, vessel_stats,
                                               vessel_position, vessel_start_position, config)

    # scroll through the orders of each player and execute each (un)lock order encountered (second turn phase)
    for player_orders in split_orders:
        for single_order in player_orders:
            for order_type in ('release', 'lock'):

                if single_order.find(order_type) != -1:
                    index_order = single_order.find(':')
                    order = single_order[index_order + 1:]
                    vessel_name = single_order[:index_order]

                    player = split_orders.index(player_orders)

                    if vessel_name in vessel_stats[player]:

                        if order == 'release':
                            release(player, vessel_name, vessel_stats)
                        else:
                            lock(player, vessel_name, vessel_stats, player_estate, asteroid_position)

    # scroll through the orders of each player and execute each move order encountered (third turn phase - moves)
    for player_orders in split_orders:
        for single_order in player_orders:
            if '@' in single_order:  # Check if the order is a move

                # Get the index to find any string I wan't
                index_order = single_order.find(':')
                index_order_type = single_order.find('@')
                index_coord_separator = single_order.find('-', index_order)

                vessel_name = single_order[:index_order]

                # Get all the coordinate info in the order
                row = single_order[index_order_type + 1:index_coord_separator]
                column = single_order[index_coord_separator + 1:]

                # Check if the coordinate given are digit
                if row.isdigit() and column.isdigit():
                    player = split_orders.index(player_orders)

                    # Check if the vessel exist
                    if vessel_name in vessel_stats[player]:

                        # Update the dictionary and change the coord from a str to an int
                        player = split_orders.index(player_orders)
                        final_coordinate[player].update({vessel_name: [int(row), int(column)]})

    # Make the move
    move(vessel_stats, vessel_position, final_coordinate, environment_stats, config)

    # scroll through the orders of each player and execute each attack order encountered (third turn phase - attacks)

    for player_orders in split_orders:
        for single_order in player_orders:
            if '*' in single_order:

                # Get the index to find any string I wan't
                index_order = single_order.find(':')
                index_order_type = single_order.find('*')
                index_coord_separator = single_order.find('-', index_order)

                vessel_name = single_order[:index_order]

                # Get all the coordinate info in the order
                row = single_order[index_order_type + 1:index_coord_separator]
                column = single_order[index_coord_separator + 1:]

                # Check if the coordinate given are digit
                if row.isdigit() and column.isdigit():

                    # Change them from a str to an int
                    attack_coord = [int(row), int(column)]

                    # Make the attack
                    player = split_orders.index(player_orders)
                    if vessel_name in vessel_stats[player]:

                        attack(player, vessel_name, attack_coord, vessel_stats, vessel_position, player_estate,
                               base_position, config)


def lock(player, vessel, vessel_stats, player_estate, asteroid_position):
    """
    Lock the excavator

    Parameters:
    -----------
    player: player index for list 0 or 1 (int)
    vessels: name of the vessel (str)
    vessel_stat: contains the information about the vessels of the players (list)
    player_estate : contains the ore_amount, the vessels and the base of each player (dic)
    asteroid_position: contain all asteroid position (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (07/04/2018)
    Impl: Ryan Rennoir V.1 (07/04/2018)
    """
    state = vessel_stats[player][vessel][4]

    if state is None or state == 'lock':
        return

    else:
        if not (player_estate[player]['base'] == vessel_stats[player][vessel][1]):

            on_asteroid = False

            for asteroid in asteroid_position:
                if asteroid == vessel_stats[player][vessel][1]:

                    on_asteroid = True

            if not on_asteroid:
                return

        vessel_stats[player][vessel][4] = 'lock'


def release(player, vessel, vessel_stats):
    """
    Release the excavator

    Parameters:
    -----------
    player: player index for list 0 or 1 (int)
    vessels: name of the vessel (str)
    vessel_stat : contains the information about the vessels of the players (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (07/04/2018)
    Impl: Ryan Rennoir V.1 (07/04/2018)
    """
    state = vessel_stats[player][vessel][4]

    if state is None or state == 'release':
        return

    vessel_stats[player][vessel][4] = 'release'


def ai(player, vessel_stats, environment_stats):
    """
    Calculate what the IA will do.

    Parameters:
    -----------
    player : tell the IA, which player she is (0 or 1) (int)
    vessel_stat : contains the information about the vessels of the players (list)
    environment_stats : contain the board size and the ore of each asteroid (dictionary)

    Return:
    -------
    order: the orders of the IA (string)

    Version:
    --------
    spec: Ryan Rennoir V.1 (07/04/2018)
    impl: Arnaud Schmetz V.1 (09/04/2018)
    """
    # TODO make the real ai
    orders = ''

    vessel_type = ('scout', 'warship', 'excavator-S', 'excavator-M', 'excavator-L')

    for i in range(randint(0, 3)):

        action_type = ['buy', 'move', 'lock', 'attack']

        action = action_type[randint(0, 3)]

        if action == 'buy':

            # make the purchases
            name = 'vessel_' + str(randint(0, 200))
            vessel = vessel_type[randint(0, 4)]
            orders += name + ':' + vessel + ' '

        if len(vessel_stats[player]) > 0:
            vessels = []
            for vessel in vessel_stats[player]:
                vessels.append(vessel)

            elements = len(vessels) - 1

            vessel = vessels[randint(0, elements)]

            if action == 'move' or action == 'attack':

                # make the actions for the vessels
                bord = environment_stats['board_size']

                row = randint(0, bord[0])
                column = randint(0, bord[1])
                new_coordinates = [row, column]

                if action == 'attack':
                    order_type = ':*'

                else:
                    order_type = ':@'

                orders += vessel + order_type + str(new_coordinates[0]) + '-' + str(new_coordinates[1]) + ' '

            if action == 'lock':

                random = randint(0, 1)

                if random == 1:
                    order_type = ':release'

                else:
                    order_type = ':lock'

                orders += vessel + order_type + ' '

    return orders


def continue_game(player_estate):
    """
    Check if the game is ended or not 
    
    Parameters:
    -----------
    player_estate: contains the ore_amount, the vessels and the base of each player (list)
    
    Return:
    -------
    Result: True if the game must continue, or False if it is ended (bool)
    
    Version:
    --------
    Spec: Arnaud Schmetz V.1 (09/04/2018)
    Impl: Ryan Rennoir V.1 (11/04/2018)
    """
    for player in player_estate:

        base = player['base_hp']
        ore = player['ore_amount']
        vessel = player['vessel']

        if ore == 0 and vessel == [] or base <= 0:
            return False

    return True


def str2bool(string):
    """
    If input string equal to True return True, False other wise.

    Parameters:
    -----------
    string: String to test (str)

    Return:
    -------
    Result: True or False (bool)

    Version:
    --------
    Spec : Ryan Rennoir V.1 (15/04/2018)
    Impl : Ryan Rennoir V.1 (15/04/2018)
    """
    string = string.lower()
    if string == 'true':
        return True

    return False


def game():
    """
    The game itself with the loop and all function call

    Version:
    --------
    Spec: Ryan Rennoir V.1 (30/03/2018)
    Impl: Ryan Rennoir v.1 (30/03/2018)
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    general = config['general']

    if general['max_round'] == 'None':
        max_round = None
    else:
        max_round = int(general['max_round'])

    scout = config['scout']
    warship = config['warship']
    excavator_s = config['excavator-S']
    excavator_m = config['excavator-M']
    excavator_l = config['excavator-L']

    config = {'general': [int(general['case per move']), int(general['nb_AI']), int(general['starting_ore']),
                          int(general['base_hp']), max_round],

              'scout': [int(scout['life']), int(scout['range']), int(scout['max ore']), str2bool(scout['lock']),
                        int(scout['attack']), int(scout['cost'])],

              'warship': [int(warship['life']), int(warship['range']), int(warship['max ore']), str2bool(warship['lock']),
                          int(warship['attack']), int(warship['cost'])],

              'excavator-S': [int(excavator_s['life']), int(excavator_s['range']), int(excavator_s['max ore']),
                              str2bool(excavator_l['lock']), int(excavator_s['attack']), int(excavator_s['cost'])],

              'excavator-M': [int(excavator_m['life']), int(excavator_m['range']), int(excavator_m['max ore']),
                              str2bool(excavator_m['lock']), int(excavator_m['attack']), int(excavator_m['cost'])],

              'excavator-L': [int(excavator_l['life']), int(excavator_l['range']), int(excavator_l['max ore']),
                              str2bool(excavator_l['lock']), int(excavator_l['attack']), int(excavator_l['cost'])]}

    # Init the game loop
    data = create_data(config)

    # Get all game structure
    vessel_stats = data[0]
    player_estate = data[1]
    environment_stats = data[2]
    vessel_position = data[3]
    asteroid_position = data[4]
    vessel_start_position = data[5]
    base_position = data[6]

    # Init the game
    nb_ai = config['general'][1]
    final_coordinate = [{}, {}]
    game_loop = True

    # Draw the map for the first time
    ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position, base_position)

    _round = 0

    while game_loop:

        # Check how many ai's
        if nb_ai == 2:
            command_p1 = ai(0, vessel_stats, environment_stats)
            command_p2 = ai(1, vessel_stats, environment_stats)
            print('AI 1 say: %s' % command_p1)
            print('AI 2 say: %s' % command_p2)

        elif nb_ai == 1:
            command_p1 = input('Player 1:')
            command_p2 = ai(1, vessel_stats, environment_stats)
            print('AI say: %s' % command_p2)
        else:
            command_p1 = input('Player 1:')
            command_p2 = input('Player 2:')

        get_order([command_p1, command_p2], vessel_stats, player_estate, environment_stats, vessel_position,
                  final_coordinate, vessel_start_position, asteroid_position, base_position, config)

        get_ore(vessel_stats, player_estate, environment_stats, config)

        ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position, base_position)

        # Check if the game end
        game_loop = continue_game(player_estate)

        if config['general'][4] == _round:
            game_loop = False

        _round += 1

    print('Game over')


game()