import random

#Passes in two team ratings

max_randomization = 30000

def build_difference_dictionary() :
    add_to_fifty = 1500
    decrease_addtofifty = 0.9
    
    difference_dictionary = {0:int(max_randomization/2)}
    i = 0
    while True :
        i += 1
        difference_dictionary[i] = difference_dictionary[i-1]+add_to_fifty
        add_to_fifty = int(add_to_fifty*decrease_addtofifty)
        if i == 25 :
            break
    return difference_dictionary

difference_dictionary = build_difference_dictionary()


def get_goal_difference(randomization_difference) :
    if randomization_difference > 80 :
        return random.randint(4, 5)
    if randomization_difference > 60 :
        return random.randint(3, 4)
    if randomization_difference > 40 :
        return random.randint(2, 3)
    if randomization_difference > 20 :
        return random.randint(1, 2)
    return random.randint(1, 2)



def build_gd_randomizers() :
    gd_randomizers_better = {}
    gd_randomizers_worse = {}
    better, worse = 100, 100
    for rating_difference in range(1, 26) :
        gd_randomizers_better[rating_difference] = []
        gd_randomizers_worse[rating_difference] = []
        b = better
        start_add = 60
        while True :
            if b >= 200 :
                gd_randomizers_better[rating_difference].append(200)
                break
            gd_randomizers_better[rating_difference].append(b)
            b += start_add
            start_add = int(start_add*0.8)
            if start_add < 10 :
                start_add = 10
        w = worse
        start_add = 60
        while True :
            if w >= 200 :
                gd_randomizers_worse[rating_difference].append(200)
                break
            gd_randomizers_worse[rating_difference].append(w)
            w += start_add
            start_add = int(start_add*0.8)
            if start_add < 10 :
                start_add = 10
        better -= 5
        worse += 5

    return gd_randomizers_better, gd_randomizers_worse

gd_randomizers_better, gd_randomizers_worse = build_gd_randomizers()
#print(gd_randomizers_better)
#print()
#print()
#print()
#print(gd_randomizers_worse)
#quit()


def gd(difference_array) :
    length = len(difference_array)
    if length == 1 :
        return 1
    r = random.randint(1, 200)
    if r <= difference_array[0] :
        return 1
    low, high = 0, length
    while True :
        ind = int((high-low)/2)
        if r > difference_array[ind] and ind <= difference_array[ind+1] :
            return ind+2
        else :
            if r <= difference_array[ind] :
                high = ind
            else :
                low = ind



def match_sim(team1, team2, team1_name, team2_name) :
    if team1 > team2 :
        better_team, better_team_name, worse_team, worse_team_name = team1, team1_name, team2, team2_name
    elif team2 > team1 :
        better_team, better_team_name, worse_team, worse_team_name = team2, team2_name, team1, team1_name
    else :
        randomized = random.randint(1, 100)
        if randomized > 40 and randomized < 60 :
            return 'Draw', 0
        if randomized >= 60 :
            return team2_name, get_goal_difference(100-randomized) 
        else :
            return team1_name, get_goal_difference(randomized)
    try :
        randomized = random.randint(1, max_randomization)
        target = difference_dictionary[better_team-worse_team]
        draw_minimum, draw_maximum = target-int(max_randomization/10), target+int(max_randomization/10)
        if randomized > draw_maximum :
            return worse_team_name, gd(gd_randomizers_worse[better_team-worse_team])
        elif randomized >= draw_minimum and randomized <= draw_maximum :
            return 'Draw', 0
        return better_team_name, gd(gd_randomizers_better[better_team-worse_team])
    except :
        return better_team_name, random.randint(4, 9)
        
        
"""
team1, team2, team1_name, team2_name = 75, 85, 'Burnley', 'Chelsea'
team1, team2, team1_name, team2_name = 78, 74, 'Brighton', 'Sheffield'
team1, team2, team1_name, team2_name = 90, 76, 'Barcelona', 'Newcastle'
n = 0
for i in range(200) :
    r = match_sim(team1, team2, team1_name, team2_name)
    if r[0] == 'Newcastle' :
        n += 1

print(n)
"""
        
