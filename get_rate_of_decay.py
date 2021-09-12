import get_rate_of_progression

def calculate_days_old_factor(days_old, day_of_decline) :
	return (0.5+(((days_old-day_of_decline)/100000)*1.2))/15
		
def calculate_rating_factor(rating) :
	return (int(rating)/100)

def get_subtracted_for_this_day(days_old, day_of_decline, rating) :
	return (calculate_days_old_factor(days_old, day_of_decline)*calculate_rating_factor(rating))/2

def test_sftd() :
	dod = 30
	while True :
		starting_date = 'Sept. 1, 2020'
		birthday = 'June 24, 1987'
		age = 34
		days_after_age = 365-get_rate_of_progression.get_days_after_age(birthday, starting_date)
		days_old = (age*365)+days_after_age
		print(days_old)
		day_of_decline = (dod*365)
		rating = 93
		print(age, rating)
		print(days_after_age, 'REEE')
		while True :
			to_subtract = get_subtracted_for_this_day(days_old, day_of_decline, int((rating+1)))
			if to_subtract > 0 :
				rating -= to_subtract
			days_old += 1
			days_after_age += 1
			
			if days_old == 15000 :
				break
			if days_after_age == 365 :
				age += 1
				days_after_age = 0
				print(age, rating)
		print()
		print()
		print()
		dod -= 1
		if dod == 25 :
			break
		
#test_sftd()

