def get_order(order, vessel_stats, board, player_estate, environment_stats, vessel_position, final_coordinate) :
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
    Implem : Arnaud Schmetz v.1 (26/03/2018)
    """
    
    splited_orders = [] 
    for player_orders in order :
        splited_orders.append(player_orders.split())
    
    # scroll through the orders of each player and execute each buy order encountered (first turn phase)
    buy_types = { 'scout' : ('scout', create_scout), 'warship' : ('warship', create_warship) , 'excavator_M' : ('excavator_M', create_excavator_m) , 
                'excavator_S' :('excavator_S', create_excavator_s), 'excavator_L' : ('excavator_L', create_excavator_l) }
    for player_orders in splited_orders :
        for single_order in player_orders :
            for buy_type in buy_types :
                if str.find(single_order, buy_type (0)) != -1 :
                    buy_type (1) (single_order [0 : str.find(single_order, ':')], player_estate, splited_orders.index(player_orders), vessel_stats, vessel_position, 
                    [player_estate[int(splited_orders.index(player_orders))]['base'] [1], [player_estate[int(splited_orders.index(player_orders))]['base'] [2]]])
    
    # scroll through the orders of each player and execute each (un)lock order encountered (second turn phase)
    for player_orders in splited_orders :
        for single_order in player_orders :
            for order_type in (('release', unlock), ('lock', lock)) :
                if str.find(single_order, order_type (0)) != -1 :
                    order_type (1) (single_order [0 : str.find(single_order, ':')], vessel_stats, environment_stats, player_estate)
                    
    # scroll through the orders of each player and execute each move order encountered (third turn phase - moves)
    for player_orders in splited_orders :
        for single_order in player_orders :
            if str.isdigit(single_order[-1]) :
                if str.find(single_order, '*') == -1 :
                    if str.find(single_order, '@') != -1 :
                        row = single_order [str.find(single_order, '@')+1:str.find(single_order, ':')]
                    else :
                        row = single_order [str.find(single_order, ':')+1:]
                    final_coordinate [splited_orders.index(player_orders)].update({single_order [0 : str.find(single_order, ':')] : [single_order [str.find(single_order, '-'):], row] })
                    move (single_order [0 : str.find(single_order, ':')], splited_orders.index(player_orders), vessel_stats, vessel_position, final_coordinate)

    # scroll through the orders of each player and execute each attack order encountered (third turn phase - attacks)
    for player_orders in splited_orders :
        for single_order in player_orders :
            if str.isdigit(single_order[-1]) :
                if str.find(single_order, '*') != -1 :                    
                    attack (single_order [0 : str.find(single_order, ':')], [single_order[str.find(single_order, '-')+1:],single_order[str.find(single_order, '*')+1:str.find(single_order, '-')]] , vessel_position, vessel_stats)    

    # call the function operating all the operations required with the ore (last turn phase)
    get_ore (vessel_stats, player_estate, environment_stats)
