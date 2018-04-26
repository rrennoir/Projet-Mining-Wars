from random import randint


def ai(player, vessel_stats, environment_stats, player_estate, final_coordinate, config):
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

    # shopping

    # lock / release

    # attack/move
    if len(vessel_stats[player]) != 0:
        # Get the coordinate of all enemy vessel
        if player == 1:
            enemy_player = 0
        else:
            enemy_player = 1

        enemy_vessel = vessel_stats[enemy_player]

        attacker = []
        excavator = []
        for ships in vessel_stats:
            if ships[0] in ('scout', 'warship'):
                attacker.append(ships)
            else:
                excavator.append(ships)

        if len(vessel_stats[enemy_player]) != 0:
            for vessel in attacker:
                vessel_center = vessel[1]
                vessel_distance = []

                for enemy in enemy_vessel:
                    coord = enemy[1]
                    enemy_name = enemy_vessel.index(enemy)

                    # Measures the Manhattan distance(|row_b - row_a| + |column_b - column_a|)
                    delta = abs(coord[0] - vessel_center[0]) + abs(coord[1] - vessel_center[1])

                    vessel_distance.append([enemy_name, delta])

                # Find the closest vessel
                closest = min(vessel_distance)
                vessel_index = vessel_distance.index(closest)
                vessel_name = vessel_distance[vessel_index][0]

                # Compute the base distance
                enemy_base = player_estate[enemy_player]['base']
                delta_base = abs(enemy_base[0] - vessel_center[0]) + abs(enemy_base[1] + vessel_center[1])

                # Get the range and name of the attacker
                v_range = config[vessel[0]][1]
                attacker_name = vessel_stats.index(attacker)

                # Enemy target coordinate
                enemy_center = vessel_stats[enemy_player][vessel_name][1]
                coord_enemy_r = enemy_center[0]
                coord_enemy_c = enemy_center[1]

                base_attacked = False
                defend_base = ''

                # Check if the base is attacked
                for base_attacker in vessel_stats[enemy_player]:
                    base = player_estate[player]['base']
                    enemy_coord = base_attacker[1]

                    delta_b_attack = abs(base[0] - enemy_coord[0]) + abs(base[1] - enemy_coord[1])

                    if delta_b_attack <= 10:
                        # Vessel in the secure zone
                        base_attacked = True
                        delta_target = abs(vessel_center[0] - enemy_coord[0]) + abs(vessel_center[1] - enemy_coord[1])

                        if delta_target > v_range:
                            # Vessel in range: attack
                            defend_base = '%s:@%s-%s ' % attacker_name, enemy_coord[0], enemy_coord[0]

                        else:
                            # Vessel out of range: move
                            defend_base = '%s:*%s-%s ' % attacker_name, enemy_coord[0], enemy_coord[1]

                # Check if an excavator is attacked
                excavator_attacked = False
                defend_excavator = ''
                for vessels in vessel_stats[player]:

                    # For each excavator
                    if vessels[0] in ('excavator-S', 'excavator-M', 'excavator-L'):
                        vessels_coord = vessels[1]

                        # Get the distance between an enemy and excavator to defend them
                        for enemy_vessel in vessel_stats[enemy_player]:
                            enemy_center = enemy_vessel[1]

                            _delta = abs(vessels_coord[0] - enemy_center[0]) + abs(vessels_coord[1] - enemy_center[1])

                            if _delta <= 5:
                                # Excavator can be attacked
                                excavator_attacked = True

                                if _delta <= v_range:
                                    # Enemy in range of the vessel
                                    defend_excavator = '%s:*%s-%s ' % attacker_name, enemy_center[0], enemy_center[1]

                                else:
                                    # Enemy out of range move to the enemy
                                    defend_excavator = '%s:@%s-%s ' % attacker_name, enemy_center[0], enemy_center[1]

                # Chose the right order
                if delta_base >= v_range:
                    # Attack the base in range
                    order_attack_ia = '%s:*%s-%s ' % attacker_name, enemy_base[0], enemy_base[1]

                elif base_attacked:
                    # Move or attack the vessel near the base
                    order_attack_ia = defend_base

                elif excavator_attacked:
                    # Move to the excavator or defend it
                    order_attack_ia = defend_excavator

                elif v_range >= closest:
                    # Attack the closest enemy
                    order_attack_ia = '%s:*%s-%s ' % attacker_name, coord_enemy_r, coord_enemy_c

                else:
                    # Move to the enemy base or random move(1/10)
                    random = randint(1, 10)

                    if random == 1:
                        # Move random
                        direction_row = randint(1, 2)
                        direction_column = randint(1, 2)
                        case = config['general'][0]

                        # Random direction
                        if direction_row == 1:
                            vessel_center[0] += case
                        else:
                            vessel_center[0] -= case

                        if direction_column == 1:
                            vessel_center[1] += case
                        else:
                            vessel_center[1] -= case

                        order_attack_ia = '%s:@%s-%s ' % attacker_name, vessel_center[0], vessel_center[1]

                    else:
                        order_attack_ia = '%s:@%s-%s ' % attacker_name, enemy_base[0], enemy_base[1]

                orders += order_attack_ia

            # if len(excavator) != 0:
            for excavators in excavator:
                order_excavator_ia = ''
                vessel_type = excavators[0]
                max_ore = config[vessel_type][2]
                ore = excavators[3]

                if max_ore == ore:
                    excavator_name = vessel_stats[player].index(excavators)
                    base = player_estate['base']

                    if excavators[4] == 'lock':
                        # Release
                        order_excavator_ia += '%s:release' % excavator_name

                        # Check if the vessel is already trying to move
                        if excavator_name in final_coordinate[player]:

                            # Check if the target isn't the base
                            target_coordinate = final_coordinate[player][excavator_name]
                            if target_coordinate == base:
                                # Already going to base
                                order_excavator_ia += ''

                            else:
                                # Go to base
                                order_excavator_ia += '%s:@%s-%s' % excavator_name, base[0], base[1]
                elif ore == 0:
                    for asteroid in environment_stats['asteriod']:


                orders += order_excavator_ia

    return orders
