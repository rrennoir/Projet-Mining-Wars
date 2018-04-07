def IA (player, vessel, board, players_estate, environment_stats, vessel_position):
    """ calculate what the IA will do.

    Parameters
    ----------
    player : tell the IA, which player she is (1 or 2) (int) 
    vessel_stats : contains the information about the vessels of the players (lis)
    board : repository list of tuples used to calculate the content of each tile more easily (list)
    players_estate : contains the ore_amount, the vessels and the base of each player (list)
    environment_stats : countains the board size and the ore of each asteroid (dictionnary)
    vessel_position : countains the position of each entire vessel into a list (list)

    Return
    ------
    orders : the orders of the IA (string)

    Version
    -------
    specification : Arnaud Schmetz (v.1 02/03/18) """
    
    from random import randint
    orders = ''
    
    # make the purchases 
    for vessel in ((9, 'warship'), (4, 'excavator-L'), (3, 'scout'), (2, 'excavtor-M'), (1, 'excavator-S')) :
        if player_estate [player - 1] [ore_amount] >= vessel (0) and orders == '' :
            name = 'random_vessel' + randint(0, 200)
            while name in vessel_stats [player - 1] :
                name = 'vessel_' + randint(0, 200) + '_player_' + player + ' ' 
            orders += name + ':' + vessel(1)
    
    # make the actions for the vessels
    for vessel in vessel_stats [player - 1] :
        choice = randint(1,2)
        
        # make the actions for the exctractors
        if vessel_stats [player - 1] ['type'] in ('excavator_m', 'excavator_s', 'excavator_l') :
            if choice == 1 :
                if vessel_stats [player - 1] == 'lock' :
                    orders += vessel + ':release '
                else :
                    for asteroid in environment_stats ['asteroid'] :
                        if vessel_stats [player - 1] ['center coordinate'] [0] == asteroid [0] (0) and vessel_stats [player - 1] ['center coordinate'] [1] == asteroid [0] (1) :
                            orders += vessel + ':lock '  
                    if vessel_stats [player - 1] ['center coordinate'] == player_estate ['base'] :
                            orders += vessel + ':lock '      
            elif vessel_stats [player - 1] == 'unlock' :
                new_coordinates = [vessel_stats [player - 1] ['center coordinate'] [0] + randint(-1, 1), vessel_stats [player - 1] ['center coordinate'] [1] + randint(-1, 1) ]
                orders += vessel + ':@' + new_coordinates [0] + '-' + new_coordinates [1]          
                
                    