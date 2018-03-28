def game():
    """
    The party,will loop and continue the game until the end

    Version:
    -------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def create_vessel(player_estate, type, player, vessel_stats):
    """
    create the vessel and his positions

    Parameters:
    -----------
    player : Player number 1 or 2 (int)
    player_estate : Player stats (dic)
    type : Type of vessel (str)
    vessel_stats : The dictionary with all vessel stats (dico)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def attack(attacker, target, vessel_position, vessel_stats):
    """
    Make the attack and change the stats of the vessels

    Parameters:
    -----------
    attacker : the vessel name how attack (str)
    target : The vessel name of the target (str)
    vessel_position : The dictionary with all vessel position (dico)
    vessel_stats : The dictionary with all vessel stats (dico)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def lock_unlock(vessel, vessel_stats):
    """
    Lock or unlock the miner

    Parameters:
    -----------
    vessel : Name of the vessel to lock/unlock (str)
    vessel_stats : Stats of the vessel (dico)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def get_order(order, player):
    """
    Read the instructions give by the player and execute the function

    Parameters:
    -----------
    order :Instruction of the player (str)
    player : number of the player 1 or 2 (int)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def move(vessel_position, vessel_stats, vessel):
    """
    Move the vessel to the correct position

    Parameters:
    -----------
    vessel_position : Dico with the vessel position (dico)
    vessel_stats : Dico with vessel stat (dico)
    vessel : vessel name to move (str)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def create_data(game_config):
    """
    create all data structure for the game

    Parameter:
    ----------
    game_config : string with all the parameters for the party (str)

    Return:
    -------
    vessel : contains the informations about the vessels of the players (dico)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (dico)
    environment_stats : countains the board size and the ore of each asteroid (dico)
    vessel_position : countains the position of each entire vessel into a list (dico)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """


def ai(vessel_stats, board, players_estate, environment_stats, vessel_position):
    """ calculate what the IA will do.

    Parameters
    ----------
    vessel_stats : contains the informations about the vessels of the players (dictionnary)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (dictionnary)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    vessel_position : countains the position of each entire vessel into a list (dictionnary)

    Return
    ------
    orders : the orders of the IA (string)

    Version
    -------
    specification : Arnaud Schmetz (v.1 02/03/18) """


def check_range(x1, y1, x2, y2):
    """ Calculate the distance between a point 1 and a point 2 and tell if the attack can happen.

    Parameters
    ----------
    x1 : x_number of the point 1 (string)
    y1 : y_number of the point 1 (string)
    x2 : x_number of the point 2 (string)
    y2 : y_number of the point 2 (string)

    Return
    ------
    result : tell if the attack happen (bool)

    Version
    -------
    specification : Arnaud Schmetz, Ryan Rennoir (v.2 09/03/18)"""


def ui(vessel, board, players_estate, environment_stats, vessel_position, characters):
    """ Calculate what to display in each tile of the board and display it with the information section
    and the legend section of the UI.

    Parameters:
    ----------
    vessel : contains the information about the vessels of the players (dictionnary)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (dictionnary)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    vessel_position : countains the position of each entire vessel into a list (dictionnary)
    characters : countains the characters used for the display of each asteroid, base, type of vessel (dictionnary)

    Version:
    --------
    specification : Arnaud Schmetz (v.1 02/03/18) """


def get_ore(vessel, players_estate, environment_stats, vessel_stats):
    """ take ore out of an asteroid and give him to the vessel or tranfer the ore from a vessel to the base.

    Parameters
    ----------
    vessel : contains the informations about the vessels of the players (dictionnary)
    players-estate : contains the ore_amount, the vessels and the base of each player (dictionnary)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    vessel_stats : The dictionary with all vessel stats (dico)

    Version
    -------
    specification : Arnaud Schmetz (v.1 02/03/18) """


def character_color(character, vessel_position, player_estate):
    """
    Take a character and chose the right color to display.

    Parameters:
    -----------
    character: The character to color (str)
    vessel_position: position of all vessel (dico)
    player_estate: Contains the ore_amount, the vessels and the base of each player (dico)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
    """