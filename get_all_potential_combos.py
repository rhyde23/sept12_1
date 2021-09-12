"""import requests, re, html, pickle
from bs4 import BeautifulSoup
from file_path_converter import convert_path

pi = True

def scrape(link) :
	page = requests.get(link)
	soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
	return soup

def find_divs(soup) :
	start = [finding for finding in re.findall('div class=\"[^"]+\">[^<>]+<', soup) if finding[:18] == 'div class=\"player-']
	finish = []
	for element in start :
		for indicators in ['-age', 'potential', 'overall'] :
			if indicators in element :
				finish.append(element)
				break
	return finish

def get_values_from_small(small_array) :
	return [int(element.split('>')[1][1:][:-2]) for element in small_array]
	
def split_large_array_into_smalls(findings) :
	length_of_findings = len(findings)
	final_array = []
	for starting_index in range(0, length_of_findings, 3) :
		small_array = [findings[starting_index], findings[starting_index+1], findings[starting_index+2]]
		final_array.append(get_values_from_small(small_array))
	return final_array

def build_key_string(rating, age) :
	return str(rating)+'|'+str(age)

potential_combinations = {}
for rating in range(40, 100) :
	for age in range(16, 51) :
		key_string = build_key_string(rating, age)
		potential_combinations[key_string] = [0, 0]
		
for page in range(1, 634) :
	page_string = str(page)
	link = 'https://www.fifacm.com/players?page='+page_string
	soup = scrape(link)
	divs = find_divs(soup)
	for player_stats in split_large_array_into_smalls(divs) :
		try :
			key_string = build_key_string(player_stats[0], player_stats[2])
			if potential_combinations[key_string] == [0, 0] :
				potential_combinations[key_string] = [player_stats[1], 1]
			else :
				total_sum, divider = (potential_combinations[key_string][0]*potential_combinations[key_string][1])+player_stats[1], potential_combinations[key_string][1]+1
				potential_combinations[key_string] = [int(total_sum/divider), divider]
		except :
			print('FAILED', player_stats)
	print(page_string, 'DONE')

for key in potential_combinations :
	potential_combinations[key] = potential_combinations[key][0]


file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\PotentialCombinations.dat'
if pi :
	file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump(potential_combinations, output_file)


"""
#print(potential_combinations)

import pickle
from file_path_converter import convert_path

pi = True

def build_key_string(rating, age) :
	return str(rating)+'|'+str(age)

age_percentages = {
	16:0.17,
	17:0.15,
	18:0.13,
	19:0.11,
	20:0.09,
	21:0.08,
	22:0.07,
	23:0.06,
	24:0.05,
	25:0.04,
	26:0.03,
	27:0.02,
	28:0.01,
	29:0,
	30:0,
	31:0,
	32:0,
	33:0,
	34:0,
	35:0,
	36:0,
	37:0,
	38:0,
	39:0,
	40:0,
	40:0,
	41:0,
	42:0,
	43:0,
	44:0,
	45:0,
	46:0,
	47:0,
	48:0,
	49:0,
	50:0,
}

potential_combinations = {}
rate = 0.7
for rating in list(reversed(list(range(40, 100)))) :
	print(rating)
	for age in range(16, 51) :
		key_string = build_key_string(rating, age)
		ap = age_percentages[age]
		if ap != 0 :
			ap = ap*rate
		pot = int(rating*(1+ap))
		if pot > 99 :
			pot = 99
		potential_combinations[key_string] = pot
	rate += 0.035

file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\PotentialCombinations.dat'
if pi :
	file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump(potential_combinations, output_file)
