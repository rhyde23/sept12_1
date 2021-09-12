pi = True

import re, pickle
from file_path_converter import convert_path

file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\potential_combinations_text_file2.txt'
if pi :
	file_path = convert_path(file_path)

text_file = open(file_path,'r').read()

file_path_data = 'C:\\Users\\rhyde23\\Desktop\\Project\\PotentialCombinations.dat'
if pi :
	file_path_data = convert_path(file_path_data)
output_file = open(file_path_data, 'rb')

def get_dictionary(mode) :
	if mode == 0 :
		dictionary = {}
		lines = [line for line in text_file.split('\n') if line != '']
		for line in lines :
			key = re.findall('[0-9]{2}\|[0-9]{2}', line)[0]
			value = int(line.split(':')[1][1:][:-1])
			dictionary[key] = value
		return dictionary
	elif mode == 1:
		return pickle.load(output_file)

potential_combinations = get_dictionary(0)

def save_dictionary() :
	output_file = open(file_path_data, 'wb')
	pickle.dump(potential_combinations, output_file)

save_dictionary()

def build_key_string(rating, age) :
	return str(rating)+'|'+str(age)

def has_potential(rating, age) :
	key_string = build_key_string(rating, age)
	if rating < potential_combinations[key_string] :
		return True
	return False


def find_oldest_potential() :
	for age in reversed(list(range(16, 51))) :
		for rating in range(40, 100) :
			if has_potential(rating, age) :
				return age, rating, potential_combinations[build_key_string(rating, age)]

#oldest_potential = find_oldest_potential()
oldest_potential = 30

def fill_obvious_potentials(oldest_potential) :
	for age in range(oldest_potential, 51) :
		for rating in range(40, 100) :
			key_string = build_key_string(rating, age)
			potential_combinations[build_key_string(rating, age)] = rating
	return potential_combinations

#potential_combinations = fill_obvious_potentials(oldest_potential)

def write_dictionary() :
	text_file_write = open(file_path,'w')
	for key in potential_combinations :
		text_file_write.write(''.join(['\'', key, '\': ', str(potential_combinations[key]), ',\n']))
	text_file_write.close()
		
write_dictionary()
