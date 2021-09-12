import months_in_order

convert_shortened = {
	'Jan.':'January',
	'Feb.':'February',
	'March':'March',
	'April':'April',
	'May':'May',
	'June':'June',
	'July':'July',
	'Aug.':'August',
	'Sept.':'September',
	'Oct.':'October',
	'Nov.':'November',
	'Dec.':'December',
}

def get_days_after_age(birthday, date2_date) :
	if birthday == date2_date :
		return 0
	month, date, year = birthday.split(' ')
	date = date[:-1]
	try :
		month = convert_shortened[month]
	except :
		pass
	
	month2, date2, year2 = date2_date.split(' ')
	date2 = date2[:-1]
	try :
		month2 = convert_shortened[month2]
	except :
		pass
	
	
	date2_month_index = months_in_order.get_month_number(month2)
	birthday_month_index = months_in_order.get_month_number(month)
	
	counting_index = birthday_month_index
	total_months_passed = []
	while True :
		if counting_index == date2_month_index :
			break
		else :
			total_months_passed.append(months_in_order.get_number_month(counting_index))
			counting_index += 1
			if counting_index == 12 :
				counting_index = 0
	total_days = sum([months_in_order.get_days_in_a_month(month_passed) for month_passed in total_months_passed])
	difference_between_date_numbers = abs(int(date2)-int(date))
	if total_days == 0 :
		if int(date) >= int(date2) :
			total_days += difference_between_date_numbers
		else :
			total_days -= difference_between_date_numbers
	else :
		if int(date) >= int(date2) :
			total_days -= difference_between_date_numbers
		else :
			total_days += difference_between_date_numbers
	
	
	return 365-total_days

#birthday = 'June 18, 1989'
#date2_date = 'September 30, 2020'

#print(get_days_after_age(birthday, date2_date))

#print()
#print()
#print()
#date2_date = 'October 1, 2020'

#print(get_days_after_age(birthday, date2_date))

#quit()

age_factors = {
	16:1.5,
	17:1.4,
	18:1.3,
	19:1.2,
	20:1.1,
	21:1,
	22:0.9,
	23:0.8,
	24:0.7,
	25:0.6,
	26:0.5,
	27:0.4,
	28:0.3,
	29:0.2,
	30:0.1,
	31:0,
	32:0,
	33:0,
	34:0,
	35:0,
	36:0,
	37:0,
	38:0,
	39:0,
	40:0
}

def get_multiplying_factor(age, between_days) :
	base = age_factors[age]
	base2 = age_factors[age+1]
	difference_bases = -0.1
	if between_days == 0 :
		return base
	return base+(difference_bases*(between_days/365))
		
def demonstrate_rating_value_change(age, rating, potential, days_after_age, rating_value_change) :
	days_until_next_age = 365-days_after_age
	rating_value_total = 0
	peak = rating
	peak_age = None
	while True :
		if days_until_next_age == 0 :
			days_until_next_age = 365
			age += 1
			if age == 40 :
				break
		between_days = 365-days_until_next_age
		multiplying_factor = get_multiplying_factor(age, between_days)
		if not age > 30 :
			rating_value_total += (rating_value_change*multiplying_factor)
		days_until_next_age -= 1
		if rating_value_total > 1 :
			rating_value_total = rating_value_total-1
			rating += 1
			print(age, rating)
			peak = rating
			if peak > potential :
				break
		elif rating_value_total < 0 :
			rating_value_total = rating_value_total+1
			rating -= 1
			print(age, rating)
	if peak == potential :
		return True

def test_rating_value_change(age, rating, potential, days_after_age, rating_value_change, starting_total) :
	days_until_next_age = 365-days_after_age
	rating_value_total = starting_total
	peak = rating
	peak_age = age
	current_counting_days = 0
	counting_days_array = []
	if rating == potential :
		return True, counting_days_array
	while True :
		if days_until_next_age == 0 :
			days_until_next_age = 365
			age += 1
			if age == 40 :
				break
		between_days = 365-days_until_next_age
		multiplying_factor = get_multiplying_factor(age, between_days)
		if not age > 30 :
			rating_value_total += (rating_value_change*multiplying_factor)
		days_until_next_age -= 1
		if rating_value_total > 1 :
			rating_value_total = rating_value_total-1
			rating += 1
			peak = rating
			peak_age = age
			counting_days_array.append(current_counting_days)
			current_counting_days = 0
			if peak > potential :
				break
		elif rating_value_total < 0 :
			rating_value_total = rating_value_total+1
			rating -= 1
		current_counting_days += 1
	if peak == potential and peak_age >= 27 :
		return True, counting_days_array
	return False, counting_days_array

def determine_rating_value_change(age, rating, potential, birthday, next_to_one) :
	rating_value_change = 0
	days_after_age = get_days_after_age(birthday, 'Sept. 1, 2020')
	#test_rating_value_change(age, rating, potential, days_after_age, rating_value_change)
	#quit()
	first_loop = True
	while True :
		if first_loop :
			starting_total = next_to_one
		else :
			starting_total = 0
		confirm, counting_days_array = test_rating_value_change(age, rating, potential, days_after_age, rating_value_change, starting_total)
		if confirm :
			#demonstrate_rating_value_change(age, rating, potential, days_after_age, rating_value_change)
			return rating_value_change, counting_days_array
		else :
			rating_value_change = round(rating_value_change+0.0001, 5)
			if rating_value_change < 0 :
				break
			#print(rating_value_change)
		first_loop = False

def build_thirty_age_factors() :
	thirty_age_factors = {}
	change_gain = 1
	change = 5
	current_tgf = -20
	for age_b in range(27, 50) :
		thirty_age_factors[age_b] = current_tgf
		current_tgf += change
		change += change_gain
	return thirty_age_factors

thirty_age_factors = build_thirty_age_factors()
	
def get_rating_at_thirty(rating, age) :
	return int((rating/2)-thirty_age_factors[age])

#print(get_rating_at_thirty(92, 36))
#quit()

def player_decay(age, birth_date, rating, added_days) :
	days_after_age = get_days_after_age(birth_date, 'Sept. 1, 2020')
	days_after_age += added_days 
	if days_after_age > 365 :
		age += 1
		days_after_age = days_after_age-365
	rating_at_thirty = get_rating_at_thirty(rating, age)
	rvc, cda = determine_rating_value_change(16, rating_at_thirty, rating, birth_date, 0)
	cda = [int(cda_element*1.1) for cda_element in list(reversed(cda))]
	"""
	current_c = 0
	current_i = 0
	while True :
		days_after_age += 1
		if days_after_age == 365 :
			age += 1
			days_after_age = 0
		current_c += 1
		try :
			if current_c == cda[current_i] :
				current_i += 1
				current_c = 0
				rating -= 1
				print(age, rating)
		except :
			break
	"""
	return cda, days_after_age

#print(player_decay(age, birth_date, rating, added_days)

#player_decay()

"""
age, rating, potential, birthday = 25, 73, 73, 'April 6, 1996'
found = determine_rating_value_change(age, rating, potential, birthday)

days_after_age = get_days_after_age(birthday, 'Sept. 1, 2020')

demonstrate_rating_value_change(age, rating, potential, days_after_age, found)

#'73|21': 79,
#age = 21
#rating = 73
#potential = 79

#found = determine_rating_value_change(age, rating, potential)
#demonstrate(age, rating, potential, found)
"""

#print(determine_rating_value_change(age, rating, potential, birthday, next_to_one))

