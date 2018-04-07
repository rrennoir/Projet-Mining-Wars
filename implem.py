from termcolor import colored
import os
import configparser


def create_data(config):
    """
    create all data structure for the game

    Parameter:
    ----------
    config:

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

    if not ('game_config' in locals()):
        return  # return nothing

    # create the empty vessel list
    vessel_stats = [{}, {}]
    vessel_position = [{}, {}]

    ore = config['general'][2]

    # create the player_estate dictionary
    player_estate = [{'ore_amount': ore, 'vessel': [],
                      'base': [int(game_config[3][0:str.find(game_config[3], ' ')]),
                               int(game_config[3][str.find(game_config[3], ' ') + 1:-1])]},
                     {'ore_amount': ore, 'vessel': [],
                      'base': [int(game_config[4][0:str.find(game_config[4], ' ')]),
                               int(game_config[4][str.find(game_config[4], ' ') + 1:-1])]}]

    # create the environment_stats dictionary, the asteroid_position and add the information about the asteroids on it
    environment_stats = {'board_size': (int(game_config[1][0:2]), int(game_config[1][3:5]))}
    asteroid_position = []

    _asteroid = []
    for i in range(len(game_config) - 6):
        asteroid_info = game_config[i + 6].split()
        _asteroid += [[[int(asteroid_info[0]), int(asteroid_info[1])], int(asteroid_info[2]), int(asteroid_info[3])]]
        asteroid_position.append([int(asteroid_info[0]), int(asteroid_info[1])])

    environment_stats.update({'asteroid': _asteroid})

    # create all starting position for a new vessel
    vessel_start_position = create_vessel_starting_position(player_estate)

    return vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position


def create_scout(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    create the scout and his positions

    Parameters:
    -----------
    config:
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

    life = config[vessel_type][0]
    tonnage = config[vessel_type][1]
    if config[vessel_type][2]:
        locking = 'unlock'
    else:
        locking = None

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_warship(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
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

    life = config[vessel_type][0]
    tonnage = config[vessel_type][1]
    if config[vessel_type][2]:
        locking = 'unlock'
    else:
        locking = None

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_s(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Create the excavator S and his positions.

    Parameters:
    -----------
    config:
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
    # config
    vessel_type = 'excavator_s'

    life = config[vessel_type][0]
    tonnage = config[vessel_type][1]
    if config[vessel_type][2]:
        locking = 'unlock'
    else:
        locking = None

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_m(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Create the excavator M and his positions.

    Parameters:
    -----------
    config:
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
    # config
    vessel_type = 'excavator_m'

    life = config[vessel_type][0]
    tonnage = config[vessel_type][1]
    if config[vessel_type][2]:
        locking = 'unlock'
    else:
        locking = None

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
    player_estate[player]['vessel'].append(name)

    vessel_position[player].update({name: vessel_start_position[player][vessel_type]})


def create_excavator_l(name, player_estate, player, vessel_stats, vessel_position, vessel_start_position, config):
    """
    Create the excavator L and his positions.

    Parameters:
    -----------
    config:
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
    # config
    vessel_type = 'excavator_l'

    life = config[vessel_type][0]
    tonnage = config[vessel_type][1]
    if config[vessel_type][2]:
        locking = 'unlock'
    else:
        locking = None

    line = player_estate[player]['base'][0]
    column = player_estate[player]['base'][1]
    base = [line, column]

    vessel_stats[player].update({name: [vessel_type, base, life, tonnage, locking]})
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
        for column_nb in range(3):
            line_ref = base[0] - 1  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for line_nb in range(3):
                line = line_ref + line_nb
                position.append([line, column])

        create_vessel_position.append({'scout': position})

        # Warship
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base
        for column_nb in range(5):
            line_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for line_nb in range(5):
                line = line_ref + line_nb

                if not ((line_nb == 0 or line_nb == 4) and (column_nb == 0 or column_nb == 4)):
                    position.append([line, column])

        create_vessel_position[player].update({'warship': position})

        # Excavator S
        create_vessel_position[player].update({'excavator_s': base})  # the vessel position is the base, nothing to do

        # Excavator M
        position = []
        column_ref = base[1] + 1  # offset on  the top of the base
        for column_nb in range(3):
            line_ref = base[0] - 1  # offset on the left of the base, now offset on the top left corner
            column = column_ref - column_nb

            for line_nb in range(3):
                line = line_ref + line_nb

                if not ((line_nb == 0 or line_nb == 2) and
                        (column_nb == 0 or column_nb == 2)):  # take only the line and column crossing by the base
                    position.append([line, column])

        create_vessel_position[player].update({'excavator_m': position})

        # Excavator L
        position = []
        column_ref = base[1] + 2  # offset on  the top of the base
        for column_nb in range(5):
            column = column_ref - column_nb
            line_ref = base[0] - 2  # offset on the left of the base, now offset on the top left corner

            for line_nb in range(5):
                line = line_ref + line_nb

                if not ((line_nb != 2) and (column_nb != 2)):  # take only the line and column crossing the middle
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


def game_stats_ui(vessel_stats, player_estate, environment_stats):
    """
    Parameters:
    -----------
    vessel_stats:
    player_estate:
    environment_stats:

    Return:
    -------
    result:

    Version:
    --------
    spec: Ryan Rennoir V.1 (07/04/2018)
    Impl: Ryan Rennoir V.1 (07/04/2018)
    """
    # Init _ui
    _ui = ['Stats:', ' ', 'Asteroid:']

    # Add ever asteroid in the game
    _asteroid = environment_stats['asteroid']
    for asteroid in _asteroid:
        _ui.append(asteroid)

    # Pass a line
    _ui += ' '

    # Stats for players
    for player in range(2):
        _ui.append('Player' + str(player + 1) + ':')  # Player nb:

        _ui.append('Ore:' + str(player_estate[player]['ore_amount']))  # Ore: ore of the player

        # Add ever vessel for each player
        for vessel in vessel_stats[player]:
            _ui.append(vessel_stats[player][vessel])

        # Pass a line between players
        _ui += ' '

    return _ui


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
    grid = []  # Init the grid
    for line in range(size[1]):
        y_line = []

        for column in range(size[0]):
            color = 'white'  # Set the default color at white
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

                # Check ii it's the player 1 base and put the right color
                if case == player_estate[0]['base']:
                    color = 'green'  # Player 1 base

                else:
                    color = 'red'  # Player 2 base

                y_line += colored('●', color)  # it's a base

        grid.append(y_line)  # add character to the line

    # Get the stats to print
    stats = game_stats_ui(vessel_stats, player_estate, environment_stats)
    # Init the index for the stats to print on the right
    line_index = 0

    for line in grid:

        # Init the line to print
        final_line = ''

        for characters in line:
            final_line += characters

        # Add statistic
        # Try if the index is not out of range
        try:
            stats_to_print = stats[line_index]

        # Index out of range print nothing
        except IndexError:
            stats_to_print = ''

        # Print line per line the board with stats on the right
        print(final_line + ' ', stats_to_print)

        # Add 1 to the index
        line_index += 1

    # Print the legends at the end
    print('Color: Green Player 1, Red Player 2\n'
          'Characters:  □ Nothing, ● Base, ▣ Asteroid, ◎ Excavator, ◇ Scout, △ Warship')


def check_border(type_axis, vessel_position, board, direction):
    """
    Check if the vessel stay in the board

    Parameters:
    -----------
    type: line or column to check (str)
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

    if type_axis == 'line':
        for position in vessel_position:
            if position[0] + direction > board[0] or position[0] + direction < 0:
                return False
    else:
        for position in vessel_position:
            if position[1] + direction > board[1] or position[1] + direction < 0:
                return False

    return True


def move(vessel, player, vessel_stats, vessel_position, final_coordinate, environment_stats, config):
    """
    Move the vessel case per case in the right direction

    Parameters:
    -----------
    config:
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
    case = config['general'][0]

    position_line = vessel_stats[player][vessel][1][0]
    position_column = vessel_stats[player][vessel][1][1]

    destination_line = final_coordinate[player][vessel][0]
    destination_column = final_coordinate[player][vessel][1]

    board = environment_stats['board_size']

    # Check if the vessel can move
    if vessel_stats[player][vessel][4] == 'lock':
        return

    # Check if the vessel is not already on the position
    if final_coordinate[player][vessel] != vessel_stats[player][vessel][1]:

            # Check if the vessel is not already on the line
            if position_line != destination_line:
                delta_line = destination_line - position_line

                # Check if the move is negative
                if delta_line < 0:
                    direction = case * - 1
                else:
                    direction = case

                # Check if not on a border
                if check_border('line', vessel_position[player][vessel], board, direction):
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
        # Remove the target coordinate
        final_coordinate[player].pop(vessel)


def get_order(order, vessel_stats, player_estate, environment_stats, vessel_position, final_coordinate):
    """
    Read the instructions give by the player and execute the function

    Parameters:
    -----------
    order :Instruction of the player (list)
    vessel_stats : contains the informations about the vessels of the players (dictionnary)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    player-estate : contains the ore_amount, the vessels and the base of each player (dictionnary)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    vessel_position : countains the position of each entire vessel into a list (dictionnary)
    final_coordinate :

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
          Arnaud Schmetz V.2 (30/03/2018)
    Impl: Arnaud Schmetz v.1 (26/03/2018)
    """


def attack(player, attacker, coord, vessel_stats, vessel_position, player_estate, config):
    """

    :return:
    """
    # Get the range from the config.
    vessel_type = vessel_stats[player][attacker][0]
    vessel_range = config[vessel_type][1]

    center = vessel_stats[player][attacker][1]
    vessel_dmg = config[vessel_type][4]

    # Measures the Manhattan distance
    delta_line = abs(coord[0] - center[0]) + abs(coord[1] - center[1])

    # Check if out of range
    if delta_line > vessel_range:
        return

    # Check if there is a vessel at this coordinate and made the shoot.
    for player in range(2):
        for vessels in vessel_position[player]:
            for position in vessel_position[player][vessels]:

                # Check when position match
                if position == coord:

                    # Check is the vessel hit it isn't itself and remove the hp
                    if vessels != attacker:
                        vessel_stats[player][vessels][2] -= vessel_dmg

                        # Check if the vessel is dead and delete him is yes
                        if vessel_stats[player][vessels][2] <= 0:
                            del vessel_stats[player][vessels]
                            del vessel_position[player][vessels]
                            player_estate[player]['vessel'].remove(vessels)


def lock_unlock(player, vessel, vessel_stats, order, player_estate, asteroid_position):
    """
    Lock or release the excavator

    Parameters:
    -----------
    player:
    vessels:
    vessel_stats:

    Version:
    --------
    Spec: Ryan Rennoir V.1 (07/04/2018)
    Impl: Ryan Rennoir V.1 (07/04/2018)
    """
    state = vessel_stats[player][vessel][4]

    if state is None or state == order:
        return

    else:
        if not (player_estate[player]['base'] == vessel_stats[player][vessel][1]):

            for asteroid in asteroid_position:
                if not(asteroid == vessel_stats[player][vessel][1]):
                    return

        vessel_stats[player][vessel][4] = order


def ai(player, vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position):
    """
    Return:
    -------
    command:

    Version:
    --------
    spec: Ryan Rennoir V.1 (07/04/2018)
    impl:
    """


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
    scout = config['scout']
    warship = config['warship']
    excavator_s = config['excavator_s']
    excavator_m = config['excavator_m']
    excavator_l = config['excavator_l']

    game_config = {'general': [int(general['case per move']), int(general['nb_AI']), int(general['starting_ore'])],

                   'scout': [int(scout['life']), int(scout['range']), int(scout['max ore']), scout['lock'],
                             int(scout['attack']), int(scout['cost'])],

                   'warship': [int(warship['life']), int(warship['range']), int(warship['max ore']), warship['lock'],
                               int(warship['attack']), int(warship['cost'])],

                   'excavator_s': [int(excavator_s['life']), int(excavator_s['range']), int(excavator_s['max ore']),
                                   excavator_l['lock'], int(excavator_s['attack']), int(excavator_s['cost'])],

                   'excavator_m': [int(excavator_m['life']), int(excavator_m['range']), int(excavator_m['max ore']),
                                   excavator_m['lock'], int(excavator_m['attack']), int(excavator_m['cost'])],

                   'excavator_l': [int(excavator_l['life']), int(excavator_l['range']), int(excavator_l['max ore']),
                                   excavator_l['lock'], int(excavator_l['attack']), int(excavator_l['cost'])]}

    vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position \
        = create_data(game_config)

    nb_ai = game_config['general'][2]
    if nb_ai == 2:
        command_p1 = ai(0, vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position)
        command_p2 = ai(1, vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position)

    elif nb_ai == 1:
        command_p1 = input()
        command_p2 = ai(1, vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position)

    else:
        command_p1 = input()
        command_p2 = input()

    # get_order()

    create_warship('jean', player_estate, 0, vessel_stats, vessel_position, vessel_start_position, game_config)
    create_warship('louis', player_estate, 1, vessel_stats, vessel_position, vessel_start_position, game_config)

    final_coordinate = [{'jean': [15, 20]}, {'louis': [15, 0]}]

    move('jean', 0, vessel_stats, vessel_position, final_coordinate, environment_stats, game_config)
    move('louis', 1, vessel_stats, vessel_position, final_coordinate, environment_stats, game_config)

    attack(1, 'louis', [15, 9], vessel_stats, vessel_position, player_estate, game_config)

    ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position)


game()