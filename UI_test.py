from termcolor import colored


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
        line += 1
        y_line = []

        for colone in range(size[0]):
            colone += 1
            color = 'white'
            case = [colone, line]
            print(case)
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


ui(vessel_stats, player_estate, vessel_position, environment_stats, asteroid_position)
