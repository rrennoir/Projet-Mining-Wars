def get_ore(vessel_stats, player_estate, environment_stats):
    """ take ore out of an asteroid and give him to the vessel or tranfer the ore from a vessel to the base.

    Parameters:
    ----------
    vessel_stats : contains the information about the vessels of the players (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (list)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)

    Version:
    -------
    specification : Arnaud Schmetz (v.1 02/03/18)
    """
    
    # Make a dictionary to sort the vessels locked by asteroid, making easier any fair redistribution if an asteroid don't have enough ore
    vessels_by_asteroid = {}
    for asteroid in environment_stats ['asteroid'] :
        vessels_by_asteroid.update({asteroid [0] : []})
    
    # Transfer the ore between the vessels and the base and sort the vessels locked, by asteroid
    for player in vessel_stats :
        for vessel in player :
            if player [vessel] ['lock'] == 'lock' :
                if vessel ['center coordinate'] == player_estate [int(vessel_stats.index(player))] ['base'] :
                    player_estate [int(vessel_stats.index(player))] ['ore_amount'] = vessel_stats [int(vessel_stats.index(player))] [vessel] ['ore']
                    vessel_stats [int(vessel_stats.index(player))] [vessel] ['ore'] = 0
                else :
                    vessels_by_asteroid [vessel] ['center coordinate'].append(vessel)
    
    # Makes the transfer from the asteroids to the vessels
    for asteroid in vessels_by_asteroid :
        if len(asteroid) == 1 :
            environment_stats [] -= vessel_stats [int(vessel_stats.index(player))] [vessel] ['ore']
            vessel_stats [int(vessel_stats.index(player))] [vessel] ['ore'] = 0
