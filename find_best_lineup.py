from starting_team_formations import get_positions_from_formation
from outside_positions_converter import convert_outside_position_to_center

import random

all_formations = [
	'4-2-3-1 (Wide)',
	'5-3-2 (Attacking)',
	'4-4-2 (Flat)',
	'5-2-3 (Flat)',
	'4-3-3 (Defensive)',
	'4-5-1 (Defensive)',
	'4-3-3 (False 9)',
	'5-3-2 (Flat)',
	'4-3-3 (Flat)',
	'4-3-3 (Attacking)',
	'4-2-3-1 (Narrow)',
	'4-1-2-1-2 (Narrow)',
]

same_positions = {
    'LCB':['RCB', 'CB'],
    'RCB':['LCB', 'CB'],
    'RDM':['LDM', 'CDM'],
    'LDM':['RDM', 'CDM'],
    'RCM':['LCM', 'CM'],
    'LCM':['RCM', 'CM'],
    'RS':['LS', 'ST'],
    'LS':['RS', 'ST'],
    'LAM':['CAM', 'RAM'],
    'RAM':['CAM', 'LAM'],
    'RM':['LM'],
    'LM':['RM'],
    'RB':['LB'],
    'LB':['RB'],
    'RWB':['LWB'],
    'LWB':['RWB'],
    'RW':['LW'],
    'LW':['RW'],
    'CB':['RCB', 'LCB'],
    'CDM':['RDM', 'LDM'],
    'CM':['RCM', 'LCM'],
    'ST':['RS', 'LS'],
    'CAM':['RAM', 'LAM'],
    'CF':['CF']
}

"""
similar_positions = {
	'GK':['GK'],
	'CB':['CB'],
	'CDM':['CDM', 'CM'],
	'LCB':['CB'],
    'RCB':['LCB', 'CB'],
    'RDM':['LDM', 'CDM'],
    'LDM':['RDM', 'CDM'],
    'RCM':['LCM', 'CM'],
    'LCM':['RCM', 'CM'],
    'RS':['LS', 'ST'],
    'LS':['RS', 'ST'],
    'LAM':['CAM', 'RAM'],
    'RAM':['CAM', 'LAM'],
    'RM':['LM'],
    'LM':['RM'],
    'RB':['LB'],
    'LB':['RB'],
    'RWB':['LWB'],
    'LWB':['RWB'],
    'RW':['LW'],
    'LW':['RW'],
    'CB':['RCB', 'LCB'],
    'CDM':['RDM', 'LDM'],
    'CM':['RCM', 'LCM'],
    'ST':['RS', 'LS'],
    'CAM':['RAM', 'LAM'],
    'CF':['CF']
}
"""



def filter_valid_moves(players_position_ratings, position_in_question, has_to_beat) :
	return [player_name for player_name in players_position_ratings if players_position_ratings[player_name][position_in_question] > has_to_beat]

def find_best_fit(players_position_ratings, position, taken_players) :
	best_name, best_value = '', 0
	for player_name in players_position_ratings :
		if players_position_ratings[player_name][position] > best_value and not (player_name in taken_players):
			best_name, best_value = player_name, players_position_ratings[player_name][position]
	return best_name, best_value

def get_first_combination(players_position_ratings, positions_in_formation) :
	taken_players = []
	final = [] 
	for position_in_formation in positions_in_formation :
		best_fit = find_best_fit(players_position_ratings, convert_outside_position_to_center(position_in_formation), taken_players)[0]
		taken_players.append(best_fit)
		final.append(best_fit) 
	return final

def get_sum_of_combo(combo, pif) :
	return sum([players_position_ratings[combo[i]][convert_outside_position_to_center(pif_element)] for i, pif_element in enumerate(pif)])

def find_best_lineup(players_position_ratings, players_main_positions) :
	for formation in all_formations :
		positions_in_formation = get_positions_from_formation(formation)
		all_players = list(players_main_positions.keys())
		combinations = [get_first_combination(players_position_ratings, positions_in_formation)]
		combinations_sums = [get_sum_of_combo(combinations[0], positions_in_formation)]
		print()
		print()
		print(combinations[0])
		print(positions_in_formation)
		print()
		print()
		while True :
			length_to_beat = len(combinations)
			current_combo = [element for element in combinations[-1]]
			for pif_index, p in enumerate(positions_in_formation) :
				p = convert_outside_position_to_center(p)
				filtered = filter_valid_moves(players_position_ratings, p, players_position_ratings[combinations[-1][pif_index]][p])
				filtered_again = []
				for f in filtered :
					if f in combinations[-1] :
						current_place = positions_in_formation[combinations[-1].index(f)]
						if not p in same_positions[current_place] and p != current_place :
							filtered_again.append(f)
					else :
						filtered_again.append(f)
				
				
				found = False
				for f_a in filtered_again :
					if f_a in combinations[-1] :
						index_in_team = combinations[-1].index(f_a)
						current_combo[pif_index] = f_a
						bf = find_best_fit(players_position_ratings, convert_outside_position_to_center(positions_in_formation[index_in_team]), current_combo)[0]
						current_combo[index_in_team] = bf
					else :
						current_combo[pif_index] = f_a
					if not current_combo in combinations :
						#print(current_combo, 'ADDED')
						combinations.append(current_combo)
						combinations_sums.append(get_sum_of_combo(current_combo, positions_in_formation))
						found = True
						break
					else :
						current_combo[pif_index] = combinations[-1][pif_index]
						current_combo[index_in_team] = combinations[-1][index_in_team]
				if found :
					break
			if len(combinations) == length_to_beat :
				break
			#print()
			#print()
			#print()
			#print()
		index_of_max = combinations_sums.index(max(combinations_sums))
		print('--------------------------------------------')
		print(combinations[index_of_max])
		print('--------------------------------------------')
			
			

players_position_ratings = {'Willian': {'RM': 80, 'CAM': 80, 'CB': 59, 'CDM': 68, 'CF': 79, 'CM': 77, 'GK': 33, 'LB': 67, 'LM': 80, 'LW': 79, 'LWB': 71, 'RB': 67, 'RW': 79, 'RWB': 71, 'ST': 74}, 'Gabriel Martinelli': {'LM': 76, 'CAM': 74, 'CB': 59, 'CDM': 61, 'CF': 75, 'CM': 68, 'GK': 28, 'LB': 64, 'LW': 75, 'LWB': 66, 'RB': 64, 'RM': 76, 'RW': 75, 'RWB': 66, 'ST': 74}, 'Karl Hein': {'GK': 57, 'CAM': 22, 'CB': 23, 'CDM': 23, 'CF': 22, 'CM': 23, 'LB': 23, 'LM': 21, 'LW': 21, 'LWB': 23, 'RB': 23, 'RM': 21, 'RW': 21, 'RWB': 23, 'ST': 23}, 'Miguel Azeez': {'CM': 64, 'CAM': 64, 'CB': 52, 'CDM': 57, 'CF': 64, 'GK': 29, 'LB': 55, 'LM': 64, 'LW': 63, 'LWB': 57, 'RB': 55, 'RM': 64, 'RW': 63, 'RWB': 57, 'ST': 62}, 'Nicolas Pépé': {'RM': 82, 'CAM': 79, 'CB': 55, 'CDM': 62, 'CF': 80, 'CM': 74, 'GK': 32, 'LB': 63, 'LM': 82, 'LW': 80, 'LWB': 66, 'RB': 63, 'RW': 80, 'RWB': 66, 'ST': 78}, 'Reiss Nelson': {'RM': 74, 'CAM': 71, 'CB': 49, 'CDM': 57, 'CF': 71, 'CM': 66, 'GK': 30, 'LB': 58, 'LM': 74, 'LW': 72, 'LWB': 61, 'RB': 58, 'RW': 72, 'RWB': 61, 'ST': 68}, 'Ben Cottrell': {'CM': 59, 'CAM': 60, 'CB': 48, 'CDM': 52, 'CF': 59, 'GK': 24, 'LB': 51, 'LM': 60, 'LW': 59, 'LWB': 52, 'RB': 51, 'RM': 60, 'RW': 59, 'RWB': 52, 'ST': 58}, 'Rúnar Alex Rúnarsson': {'GK': 72, 'CAM': 31, 'CB': 28, 'CDM': 29, 'CF': 31, 'CM': 31, 'LB': 29, 'LM': 30, 'LW': 30, 'LWB': 29, 'RB': 29, 'RM': 30, 'RW': 30, 'RWB': 29, 'ST': 31}, 'Eddie Nketiah': {'ST': 74, 'CAM': 71, 'CB': 47, 'CDM': 51, 'CF': 73, 'CM': 63, 'GK': 29, 'LB': 51, 'LM': 70, 'LW': 71, 'LWB': 53, 'RB': 51, 'RM': 70, 'RW': 71, 'RWB': 53}, 'Kieran Tierney': {'LB': 81, 'CAM': 77, 'CB': 78, 'CDM': 79, 'CF': 76, 'CM': 77, 'GK': 35, 'LM': 79, 'LW': 77, 'LWB': 81, 'RB': 81, 'RM': 79, 'RW': 77, 'RWB': 81, 'ST': 73}, 'Folarin Balogun': {'ST': 63, 'CAM': 58, 'CB': 41, 'CDM': 43, 'CF': 61, 'CM': 52, 'GK': 27, 'LB': 45, 'LM': 59, 'LW': 59, 'LWB': 46, 'RB': 45, 'RM': 59, 'RW': 59, 'RWB': 46}, 'Cédric': {'RB': 77, 'CAM': 74, 'CB': 74, 'CDM': 75, 'CF': 74, 'CM': 75, 'GK': 33, 'LB': 77, 'LM': 75, 'LW': 74, 'LWB': 76, 'RM': 75, 'RW': 74, 'RWB': 76, 'ST': 72}, 'Calum Chambers': {'RB': 76, 'CAM': 70, 'CB': 76, 'CDM': 76, 'CF': 69, 'CM': 72, 'GK': 31, 'LB': 76, 'LM': 70, 'LW': 69, 'LWB': 74, 'RM': 70, 'RW': 69, 'RWB': 74, 'ST': 68}, 'Bukayo Saka': {'RM': 81, 'CAM': 79, 'CB': 69, 'CDM': 74, 'CF': 78, 'CM': 77, 'GK': 31, 'LB': 75, 'LM': 81, 'LW': 79, 'LWB': 77, 'RB': 75, 'RW': 79, 'RWB': 77, 'ST': 73}, 'Tolaji Bola': {'LB': 58, 'CAM': 49, 'CB': 58, 'CDM': 54, 'CF': 50, 'CM': 49, 'GK': 24, 'LM': 52, 'LW': 51, 'LWB': 57, 'RB': 58, 'RM': 52, 'RW': 51, 'RWB': 57, 'ST': 50}, 'Mathew Ryan': {'GK': 80, 'CAM': 37, 'CB': 33, 'CDM': 36, 'CF': 35, 'CM': 38, 'LB': 33, 'LM': 35, 'LW': 34, 'LWB': 33, 'RB': 33, 'RM': 35, 'RW': 34, 'RWB': 33, 'ST': 33}, 'Rob Holding': {'CB': 77, 'CAM': 62, 'CDM': 74, 'CF': 60, 'CM': 66, 'GK': 32, 'LB': 72, 'LM': 61, 'LW': 60, 'LWB': 71, 'RB': 72, 'RM': 61, 'RW': 60, 'RWB': 71, 'ST': 58}, 'Gabriel': {'CB': 79, 'CAM': 62, 'CDM': 75, 'CF': 60, 'CM': 67, 'GK': 29, 'LB': 72, 'LM': 60, 'LW': 58, 'LWB': 69, 'RB': 72, 'RM': 60, 'RW': 58, 'RWB': 69, 'ST': 60}, 'Héctor Bellerín': {'RB': 78, 'CAM': 73, 'CB': 73, 'CDM': 74, 'CF': 72, 'CM': 72, 'GK': 33, 'LB': 78, 'LM': 75, 'LW': 73, 'LWB': 77, 'RM': 75, 'RW': 73, 'RWB': 77, 'ST': 68}, 'Martin Ødegaard': {'CAM': 84, 'CB': 66, 'CDM': 74, 'CF': 81, 'CM': 81, 'GK': 34, 'LB': 72, 'LM': 83, 'LW': 82, 'LWB': 75, 'RB': 72, 'RM': 83, 'RW': 82, 'RWB': 75, 'ST': 77}, 'Cătălin Cîrjan': {'CM': 64, 'CAM': 65, 'CB': 51, 'CDM': 57, 'CF': 63, 'GK': 29, 'LB': 56, 'LM': 64, 'LW': 63, 'LWB': 57, 'RB': 56, 'RM': 64, 'RW': 63, 'RWB': 57, 'ST': 59}, 'Pierre-Emerick Aubameyang': {'ST': 85, 'CAM': 82, 'CB': 59, 'CDM': 64, 'CF': 84, 'CM': 77, 'GK': 32, 'LB': 66, 'LM': 82, 'LW': 83, 'LWB': 69, 'RB': 66, 'RM': 82, 'RW': 83, 'RWB': 69}, 'Thomas Partey': {'CM': 86, 'CAM': 82, 'CB': 83, 'CDM': 85, 'CF': 81, 'GK': 34, 'LB': 82, 'LM': 81, 'LW': 80, 'LWB': 83, 'RB': 82, 'RM': 81, 'RW': 80, 'RWB': 83, 'ST': 79}, 'Emile Smith Rowe': {'CAM': 76, 'CB': 50, 'CDM': 59, 'CF': 74, 'CM': 71, 'GK': 29, 'LB': 58, 'LM': 75, 'LW': 74, 'LWB': 61, 'RB': 58, 'RM': 75, 'RW': 74, 'RWB': 61, 'ST': 69}, 'Pablo Marí': {'CB': 76, 'CAM': 55, 'CDM': 71, 'CF': 55, 'CM': 61, 'GK': 29, 'LB': 68, 'LM': 54, 'LW': 53, 'LWB': 65, 'RB': 68, 'RM': 54, 'RW': 53, 'RWB': 65, 'ST': 57}, 'Granit Xhaka': {'CDM': 79, 'CAM': 73, 'CB': 73, 'CF': 72, 'CM': 78, 'GK': 30, 'LB': 73, 'LM': 71, 'LW': 70, 'LWB': 74, 'RB': 73, 'RM': 71, 'RW': 70, 'RWB': 74, 'ST': 70}, 'Alexandre Lacazette': {'ST': 83, 'CAM': 81, 'CB': 63, 'CDM': 67, 'CF': 82, 'CM': 77, 'GK': 30, 'LB': 64, 'LM': 79, 'LW': 80, 'LWB': 67, 'RB': 64, 'RM': 79, 'RW': 80, 'RWB': 67}, 'Dani Ceballos': {'CM': 79, 'CAM': 78, 'CB': 70, 'CDM': 76, 'CF': 76, 'GK': 33, 'LB': 73, 'LM': 77, 'LW': 76, 'LWB': 75, 'RB': 73, 'RM': 77, 'RW': 76, 'RWB': 75, 'ST': 72}, 'Bernd Leno': {'GK': 85, 'CAM': 39, 'CB': 35, 'CDM': 39, 'CF': 36, 'CM': 41, 'LB': 35, 'LM': 36, 'LW': 35, 'LWB': 36, 'RB': 35, 'RM': 36, 'RW': 35, 'RWB': 36, 'ST': 34}, 'Mohamed Elneny': {'CDM': 78, 'CAM': 72, 'CB': 74, 'CF': 71, 'CM': 76, 'GK': 31, 'LB': 74, 'LM': 71, 'LW': 70, 'LWB': 75, 'RB': 74, 'RM': 71, 'RW': 70, 'RWB': 75, 'ST': 69}, 'Dejan Iliev': {'GK': 63, 'CAM': 27, 'CB': 26, 'CDM': 27, 'CF': 27, 'CM': 27, 'LB': 26, 'LM': 27, 'LW': 27, 'LWB': 27, 'RB': 26, 'RM': 27, 'RW': 27, 'RWB': 27, 'ST': 28}, 'Joel López': {'LB': 60, 'CAM': 52, 'CB': 56, 'CDM': 54, 'CF': 52, 'CM': 51, 'GK': 26, 'LM': 56, 'LW': 54, 'LWB': 58, 'RB': 60, 'RM': 56, 'RW': 54, 'RWB': 58, 'ST': 51}, 'David Luiz': {'CB': 80, 'CAM': 72, 'CDM': 79, 'CF': 71, 'CM': 76, 'GK': 33, 'LB': 76, 'LM': 71, 'LW': 70, 'LWB': 75, 'RB': 76, 'RM': 71, 'RW': 70, 'RWB': 75, 'ST': 71}}
players_main_positions = {'Willian': 'RM', 'Gabriel Martinelli': 'LM', 'Karl Hein': 'GK', 'Miguel Azeez': 'CM', 'Nicolas Pépé': 'RM', 'Reiss Nelson': 'RM', 'Ben Cottrell': 'CM', 'Rúnar Alex Rúnarsson': 'GK', 'Eddie Nketiah': 'ST', 'Kieran Tierney': 'LB', 'Folarin Balogun': 'ST', 'Cédric': 'RB', 'Calum Chambers': 'RB', 'Bukayo Saka': 'RM', 'Tolaji Bola': 'LB', 'Mathew Ryan': 'GK', 'Rob Holding': 'CB', 'Gabriel': 'CB', 'Héctor Bellerín': 'RB', 'Martin Ødegaard': 'CAM', 'Cătălin Cîrjan': 'CM', 'Pierre-Emerick Aubameyang': 'ST', 'Thomas Partey': 'CM', 'Emile Smith Rowe': 'CAM', 'Pablo Marí': 'CB', 'Granit Xhaka': 'CDM', 'Alexandre Lacazette': 'ST', 'Dani Ceballos': 'CM', 'Bernd Leno': 'GK', 'Mohamed Elneny': 'CDM', 'Dejan Iliev': 'GK', 'Joel López': 'LB', 'David Luiz': 'CB'}

print(find_best_lineup(players_position_ratings, players_main_positions))
