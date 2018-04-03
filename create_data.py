def create_data():
    """
    create all data structure for the game

    Parameter:
    ----------
    game_config.mw : string with all the parameters for the party (str)

    Return:
    -------
    vessel : contains the informations about the vessels of the players (dico)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (dico)
    environment_stats : countains the board size and the ore of each asteroid (dico)
    vessel_position : countains the position of each entire vessel into a list (dico)
    asteroid_position : contains the position of each asteroid (list)

    Version:
    --------
    Spec: Ryan Rennoir V.1 (02/03/2018)
          Schmetz Arnaud v.2 (28/03/2018)
    Implem: Schmetz Arnaud v.1 (11/03/2018)
    """

    with open('./game_config.mw') as cfg:
        game_config = cfg.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    # game_config = [x.strip() for x in game_config]
    cfg.close()

    # create the empty vessel list
    vessel_stats = [{}, {}]
    vessel_position = [{}, {}]

    # create the player_estate dictionary
    player_estate = [{'ore_amount': 4, 'vessels_names': [],
                      'base': [game_config[3][0:str.find(game_config[3], ' ')],
                               game_config[3][str.find(game_config[3], ' ') + 1:-1]]},
                     {'ore_amount': 4, 'vessels_names': [],
                      'base': [game_config[4][0:str.find(game_config[4], ' ')],
                               game_config[4][str.find(game_config[4], ' ') + 1:-1]]}]

    # create the environment_stats dictionary, the asteroid_position and add the information about the asteroids on it
    environment_stats = {'board_size': (game_config[1][0:2], game_config[1][3:5])}
    asteroid_position = []

    for i in range(len(game_config) - 6):
        asteroid_name = 'asteroid' + str(i + 1)
        asteroid_infos = str.replace(game_config[i + 6], '\n', '').split
        environment_stats.update(
            {asteroid_name: [(asteroid_infos[0], asteroid_infos[1]), asteroid_infos[2], asteroid_infos[3]]})
        asteroid_position.append([asteroid_infos[0], asteroid_infos[1]])

    # create all starting position for a new vessel
    vessel_start_position = create_vessel_starting_position(player_estate)

    return vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position
