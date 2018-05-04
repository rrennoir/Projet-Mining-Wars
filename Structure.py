player_estate = [{'ore_amount': 'ore', 'vessel': ['vessel_name'], 'base': ['x', 'y'], 'base_hp': 'life'},
                 {'ore_amount': 'ore', 'vessel': ['vessel_name'], 'base': ['x', 'y'], 'base_hp': 'life'}]

# Board = [('x', 'y'), ('x', 'y'), ('x', 'y'), ('x', 'y'), ('x', 'y'), ('x', 'y')]

vessel_position = [{'vessel 1': [['x', 'y'], ['x', 'y']],
                    'vessel 2': [['x', 'y'], ['x', 'y']]},
                   {'vessel 3': [['x', 'y'], ['x', 'y']],
                    'vessel 4': [['x', 'y'], ['x', 'y']]}]

environment_stats = {'board_size': ('x', 'y'),
                     'asteroid': [[('x', 'y'), 'ore', 'ore/round'], [('x', 'y'), 'ore', 'ore/round']]}

asteroid_position = [['x', 'y'], ['x', 'y']]

game_config = {'general': ['case per move', 'nb_AI', 'starting_ore', 'base_hp'],
               'scout': ['life', 'range', 'max ore', 'lock', 'attack', 'cost'],
               'warship': ['life', 'range', 'max ore', 'lock', 'attack', 'cost'],
               'excavator_s': ['life', 'range', 'max ore', 'lock', 'attack', 'cost'],
               'excavator_m': ['life', 'range', 'max ore', 'lock', 'attack', 'cost'],
               'excavator_l': ['life', 'range', 'max ore', 'lock', 'attack', 'cost']}

vessel_stats = [{'vessel_name 1': ['type', 'center coordinate', 'life', 'ore', 'lock'],
                 'vessel_name 2': ['type', 'center coordinate', 'life', 'ore', 'lock']},
                {'vessel_name 3': ['type', 'center coordinate', 'life', 'ore', 'lock'],
                 'vessel_name 4': ['type', 'center coordinate', 'life', 'ore', 'lock']}]

create_vessel_position = [{'type 1': [['coordinate 1'], ['coordinate 2']],
                           'type 2': [['coordinate 1'], ['coordinate 2']]},
                          {'type 1': [['coordinate 1'], ['coordinate 2']],
                           'type 2': [['coordinate 1'], ['coordinate 2']]}]

final_coordinate = [{'vessel_1': ['x', 'y']}, {'vessel_1': ['x', 'y']}]

vessel_start_position = [[], []]
base_position = [[], []]

data = [vessel_stats, player_estate, environment_stats, vessel_position, asteroid_position, vessel_start_position,
        base_position, final_coordinate]
