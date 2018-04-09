def ai (player, vessel, player_estate, environment_stats):
    """ calculate what the IA will do.

    Parameters
    ----------
    player : tell the IA, which player she is (1 or 2) (int) 
    vessel_stats : contains the information about the vessels of the players (lis)
    players_estate : contains the ore_amount, the vessels and the base of each player (list)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)

    Return
    ------
    orders : the orders of the IA (string)

    Version
    -------
    specification : Arnaud Schmetz (v.1 02/03/18) """
    
    from random import randint
    orders = ''
    
    # make the purchases 
     for vessel in ((config ['warship'] [5], 'warship'), (config ['excavator_l'] [5], 'excavator-L'), (config ['scout'] [5], 'scout'), (config ['excavator_m'] [5], 'excavtor-M'), (config ['excavator_s'] [5], 'excavator-S')) :
        if player_estate [player - 1] ['ore_amount'] >= vessel [0] and orders == '' :
            name = 'random_vessel_' + str(randint(0, 200)) + '_player_' + str(player) 
            while name in vessel_stats [player - 1] :
                name = 'random_vessel_' + str(randint(0, 200)) + '_player_' + str(player)  
            orders += name + ':' + vessel[1] + ' '
    
    # make the actions for the vessels
    for vessel in vessel_stats [player - 1] :
        choice = randint(1,2)
        new_coordinates = [vessel_stats [player - 1] [vessel] [1] [0] + randint(-1, 1), vessel_stats [player - 1] [vessel] [1] [1] + randint(-1, 1)]
        
        # make the actions for the exctractors
        if vessel_stats [player - 1] [vessel] [0] in ('excavator_m', 'excavator_s', 'excavator_l') :
            if choice == 1 :
                if vessel_stats [player - 1] == 'lock' :
                    orders += vessel + ':release '
                else :
                    for asteroid in environment_stats ['asteroid'] :
                        if vessel_stats [player - 1] [vessel] [1] [0] == asteroid [0] (0) and vessel_stats [player - 1] [vessel] [1] [1] == asteroid [0] [1] :
                            orders += vessel + ':lock '  
                    if vessel_stats [player - 1] [vessel] [1] == player_estate ['base'] :
                            orders += vessel + ':lock '      
            elif vessel_stats [player - 1] == 'unlock' :
                orders += vessel + ':@' + str(new_coordinates [0]) + '-' + str(new_coordinates [1]) + ' '         
                
        # make the actions for the offensive vessels
        else :
            if choice == 1 :
                orders += vessel + ':@' + str(new_coordinates [0]) + '-' + str(new_coordinates [1]) + ' '    
            else : 
                scope = config [vessel_stats [player - 1] [vessel] [0]] [2]
                tile_to_shoot = [int(vessel_stats [player - 1] [vessel] [1] [0]) + randint(-scope, scope) , in(vessel_stats [player - 1] [vessel] [1] [1]) + randint(-scope, scope)]
                orders += vessel + ':*' + str(tile_to_shoot [0]) + '-' + str(tile_to_shoot [1]) + ' ' 
    
    Return orders
                
