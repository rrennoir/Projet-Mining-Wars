def get_ore(vessel_stats, player_estate, environment_stats, config):
    """ take ore out of an asteroid and give him to the vessel or tranfer the ore from a vessel to the base.

    Parameters:
    ----------
    vessel_stats : contains the information about the vessels of the players (list)
    players-estate : contains the ore_amount, the vessels and the base of each player (list)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    config :

    Version:
    -------
    specification : Arnaud Schmetz (v.1 02/03/18)
    """
    
    # Make a dictionnary to sort the vessels locked by asteroid, making easier any fair redistribution if an asteroid don't have enough ore
    vessels_by_asteroid = {}
    for asteroid in environment_stats ['asteroid'] :
        # {'asteroid_coordinates' : [[vessels], index_of_the_asteroid_in_environment_stats, total_ore_needed_for_the_vessels, amount_of_vessels_needing_ore] , .... } 
        # in which vessels are under the form : [name, ore_to_get_from_the_asteroid, player_index]   ----- player_index is the index of the player's vessels in the other structures 
        vessels_by_asteroid.update({asteroid [0] : [[], environment_stats ['asteroid'].index(asteroid), 0, 0] })
    
    # Transfer the ore between the vessels and the base and sort the vessels locked, by asteroid
    for player in vessel_stats :
        player_index = int(vessel_stats.index(player))
        for vessel in player :
            if player [vessel] [4] == 'lock' :
                # ore from the vessels to the base
                if player [vessel] [1] == player_estate [int(vessel_stats.index(player))] ['base'] :
                    player_estate [player_index] ['ore_amount'] += player [vessel] [3]
                    vessel_stats [player_index] [vessel] [3] = 0
            
                # sort the vessels locked, by asteroid, after computing how many ore each vessel should get, regardless of the ore remaining on asteroids
                else :
                    coordinates = (player [vessel] [1] [0], player [vessel] [1] [1])
                    
                    # if free space on the board >= ore obtainable per round : ore_to_get = ore obtainable per round, else ore_to_get = free space on the board
                    if config [vessel_stats [player_index] [vessel] [0]] [3] - player [vessel] [3] >= environment_stats ['asteroid'] [vessels_by_asteroid [coordinates] [1]] [2] :
                        ore_to_get = environment_stats ['asteroid'] [vessels_by_asteroid [coordinates] [1]] [2]
                    else :
                        ore_to_get = config [vessel_stats [player_index] [vessel] [0]] [3] - player [vessel] [3]
                        
                    vessels_by_asteroid [coordinates] .append([vessel, ore_to_get, player_index])
                    vessels_by_asteroid [coordinates] [2] += ore_to_get
                    vessels_by_asteroid [coordinates] [3] += 1
                   
    # Makes the transfer from the asteroids to the vessels
    for asteroid in vessels_by_asteroid :
        
        # if asteroid has enough ore : make the transfers normally
        if vessels_by_asteroid [asteroid] [2] <= environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] :
            environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] -= vessels_by_asteroid [asteroid] [2]
            for vessel in vessels_by_asteroid [asteroid] [0] :
                vessel_stats [vessel [2]] [vessel [0]] [3] += vessel [1]
        
        # if asteroid doesn't have enough ore, share it between the vessels 
        else :
            while environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] != 0 :
                shared_ore = environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] / vessels_by_asteroid [asteroid] [3]
                for vessel in vessels_by_asteroid [asteroid] :
                    
                    # if the vessel can get the amount of ore, equitably shared, make the transfer
                    if shared_ore <= vessel [1] :
                        environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] -= shared_ore
                        vessel_stats [vessel [2]] [vessel [0]] [3] += shared_ore
                        vessels_by_asteroid [asteroid] [vessels_by_asteroid [asteroid].index(vessel)] [1] -= shared_ore
                        if vessels_by_asteroid [asteroid] [vessels_by_asteroid [asteroid].index(vessel)] [1] == 0 :
                            vessels_by_asteroid [asteroid] [3] -= 1
                    
                    # else, give him the max of ore the vessel can get, letting a little bit more ore to share for the others and so leafing through the while loop again
                    else :
                        environment_stats ['asteroid'] [vessels_by_asteroid [asteroid] [1]] [1] -= vessel [1]
                        vessel_stats [vessel [2]] [vessel [0]] [3] += vessel [1]
                        vessels_by_asteroid [asteroid] [vessels_by_asteroid [asteroid].index(vessel)] [1] -= vessel [1]
                        vessels_by_asteroid [asteroid] [3] -= 1       
