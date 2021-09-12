#Web Scraper

import requests, re, pickle, html
from bs4 import BeautifulSoup
from scrape_player_page import main
from file_path_converter import convert_path
from get_rate_of_progression import determine_rating_value_change, get_days_after_age, player_decay
from calculate_player_rating import calculate_player_rating

pi = True

def scrape(link) :
    page = requests.get(link)
    
    soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
    return soup

til_arrays = [['AFC Bournemouth', 'Barnsley', 'Birmingham City', 'Blackburn Rovers', 'Brentford', 'Bristol City', 'Cardiff City', 'Coventry City', 'Derby County', 'Huddersfield Town', 'Luton Town', 'Middlesbrough', 'Millwall', 'Norwich City', 'Nottingham Forest', 'Preston North End', 'Queens Park Rangers', 'Reading', 'Rotherham United', 'Sheffield Wednesday', 'Stoke City', 'Swansea City', 'Watford', 'Wycombe Wanderers'], ['Arsenal','Aston Villa','Brighton & Hove Albion','Burnley','Chelsea','Crystal Palace','Everton','Fulham','Leeds United','Leicester City','Liverpool','Manchester City','Manchester United','Newcastle United','Sheffield United','Southampton','Tottenham Hotspur','West Bromwich Albion','West Ham United','Wolverhampton Wanderers']]
tfi_dictionaries = [{'AFC Bournemouth': '1943', 'Barnsley': '1932', 'Birmingham City': '88', 'Blackburn Rovers': '3', 'Brentford': '1925', 'Bristol City': '1919', 'Cardiff City': '1961', 'Coventry City': '1800', 'Derby County': '91', 'Huddersfield Town': '1939', 'Luton Town': '1923', 'Middlesbrough': '12', 'Millwall': '97', 'Norwich City': '1792', 'Nottingham Forest': '14', 'Preston North End': '1801', 'Queens Park Rangers': '15', 'Reading': '1793', 'Rotherham United': '1797', 'Sheffield Wednesday': '1807', 'Stoke City': '1806', 'Swansea City': '1960', 'Watford': '1795', 'Wycombe Wanderers': '1933'}, {'Arsenal': '1', 'Aston Villa': '2', 'Brighton & Hove Albion': '1808', 'Burnley': '1796', 'Chelsea': '5', 'Crystal Palace': '1799', 'Everton': '7', 'Fulham': '144', 'Leeds United': '8', 'Leicester City': '95', 'Liverpool': '9', 'Manchester City': '10', 'Manchester United': '11', 'Newcastle United': '13', 'Sheffield United': '1794', 'Southampton': '17', 'Tottenham Hotspur': '18', 'West Bromwich Albion': '109', 'West Ham United': '19', 'Wolverhampton Wanderers': '110'}]
league_indxes = ['13', '14']


file_path1 = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Database.dat'])
if pi :
    file_path1 = convert_path(file_path1)

database = pickle.load(open(file_path1, 'rb'))

file_path2 = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\PotentialCombinations.dat'])
if pi :
    file_path2 = convert_path(file_path2)

potential_combinations = pickle.load(open(file_path2, 'rb'))

current_days_until_next_update = 0

for operation_index in range(2) :
    teams_in_league = til_arrays[operation_index]
    league_page = scrape('https://www.fifaindex.com/teams/?league='+league_indxes[operation_index])
    team_fifaindex_indexes = tfi_dictionaries[operation_index ]
    
    for team_in_league in teams_in_league :
        link = 'https://www.fifaindex.com/team/'+team_fifaindex_indexes[team_in_league]+'/'
        soup = scrape(link)
        
        player_links = ['https://www.fifaindex.com'+li[6:]+'/' for li in list(set(re.findall('href=\"/player/[0-9]+', soup)))]
        final_dict = {}
        for player_link in player_links :
            player_data = main(player_link)
            age, rating = int(player_data['Age']), int(player_data['Rating'])
            player_pot = potential_combinations[str(rating)+'|'+str(age)]
            print(player_data['Name'], age, rating, player_pot, player_data['Date of Birth'])
            
            
            rating_value_change, counting_days_array = determine_rating_value_change(age, rating, player_pot, player_data['Date of Birth'], player_data['NextToOne'])
            
            player_stats_trying, player_pos_trying = player_data['Player Stats'], player_data['Position']
            
            final_development_plan = {stat_name:[] for stat_name in player_stats_trying}
            
            for i, counted_days in enumerate(counting_days_array) :
                rating, important_percentages, next_to_one = calculate_player_rating(player_stats_trying, player_pos_trying, player_pos_trying, real_position_rating=None)
                total_stats_testing = sum([player_stats_trying[total_stats_key] for total_stats_key in player_stats_trying])
                add_to_total_stats = 1
                while True :
                    trying_rating = int(player_data['Rating'])+i+1
                    total_trying = total_stats_testing + add_to_total_stats
                    trying_stats = {ip_key:important_percentages[ip_key]*total_trying for ip_key in important_percentages}
                    trying_calculate = calculate_player_rating(trying_stats, player_pos_trying, player_pos_trying, real_position_rating=None)[0]
                    if trying_calculate == trying_rating :
                        break
                    add_to_total_stats += 1
                
                for key_trying_stats in trying_stats :
                    final_development_plan[key_trying_stats].append((trying_stats[key_trying_stats]-player_stats_trying[key_trying_stats])/counted_days)
                player_stats_trying = trying_stats
            
            #print('This is the player_stats_trying after this loop')
            #print(player_stats_trying)
            #print()
            #print()
            
            player_data['DevelopmentPlan1'] = final_development_plan
            player_data['DevelopmentPlanIndex1'] = 0
            player_data['DevelopmentPlanCountedDaysArray1'] = counting_days_array
            player_data['DevelopmentPlanCountedDays1'] = 0
    
            empty_cda = counting_days_array == []
            
            age_spitting_in_total = sum(counting_days_array)
            mod = age_spitting_in_total % 365 
            age_spitting_in = age+int((age_spitting_in_total-mod)/365)
            
            counting_days_array, days_after_age = player_decay(age_spitting_in, player_data['Date of Birth'], player_pot, mod)
            
            player_data['DaysAfterAge'] = days_after_age
            
            final_development_plan = {stat_name:[] for stat_name in player_stats_trying}
            
            broke = False
            
            for i, counted_days in enumerate(counting_days_array) :
                try :
                    rating_reeee, important_percentages, next_to_one_reee = calculate_player_rating(player_stats_trying, player_pos_trying, player_pos_trying, real_position_rating=None)
                except :
                    broke = True
                    break
                total_stats_testing = sum([player_stats_trying[total_stats_key] for total_stats_key in player_stats_trying])
                add_to_total_stats = 1
                while True :
                    trying_rating = int(player_data['Rating'])-i-1
                    total_trying = total_stats_testing - add_to_total_stats
                    trying_stats = {ip_key:important_percentages[ip_key]*total_trying for ip_key in important_percentages}
                    try :
                        trying_calculate = calculate_player_rating(trying_stats, player_pos_trying, player_pos_trying, real_position_rating=None)[0]
                    except :
                        broke = True
                        break
                    if trying_calculate == trying_rating :
                        break
                    add_to_total_stats += 1
                
                for key_trying_stats in trying_stats :
                    if i == 0 :
                        final_development_plan[key_trying_stats].append(0)
                    else :
                        final_development_plan[key_trying_stats].append((trying_stats[key_trying_stats]-player_stats_trying[key_trying_stats])/counted_days)
                player_stats_trying = trying_stats
            
            if broke :
                for key_fdp in final_development_plan :
                    still_to_do = len(counting_days_array)-len(final_development_plan[key_fdp])
                    for std in range(still_to_do) :
                        final_development_plan[key_fdp].append(None)
            
            if empty_cda :
                for key_fdp in final_development_plan :
                    final_development_plan[key_fdp] = final_development_plan[key_fdp][1:]
                counting_days_array = counting_days_array[1:]
            
            days_until_thirty = 10950-((age_spitting_in*365))
            if days_until_thirty > 0 :
                for key_dev2 in final_development_plan :
                    final_development_plan[key_dev2].insert(0, 0)
                counting_days_array.insert(0, days_until_thirty)
            
            player_data['DevelopmentPlan2'] = final_development_plan
            player_data['DevelopmentPlanIndex2'] = 0
            player_data['DevelopmentPlanCountedDaysArray2'] = counting_days_array
            player_data['DevelopmentPlanCountedDays2'] = 0
            
            player_data['DevelopmentPlanNumber'] = '1'
            
            player_data['DaysUntilNextUpdate'] = current_days_until_next_update
            current_days_until_next_update += 1
            if current_days_until_next_update == 8 :
                current_days_until_next_update = 0
            
            if player_data['Team'] == team_in_league :
                final_dict[player_data['Name']] = player_data
        
        starting_lineup_findings = [finding[7:][:-9] for finding in re.findall('title=\"[^""]+\"', soup) if finding[-8:] == 'FIFA 21\"']
        starting_lineup = []
        for starting_lineup_finding in starting_lineup_findings :
            if starting_lineup_finding in final_dict and not starting_lineup_finding in starting_lineup :
                starting_lineup.append(starting_lineup_finding)
            if len(starting_lineup) == 11 :
                break 
        print("\'"+team_in_league+"_Lineup\':", starting_lineup)
        database[team_in_league] = final_dict
    
output_file = open(file_path1, 'wb')
pickle.dump(database, output_file)

"""
final_dict = main()
for team in final_dict :
    file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\', team, '.dat'])
    if pi :
        file_path = convert_path(file_path)
    output_file = open(file_path, 'wb')
    pickle.dump(final_dict[team], output_file)
    print(team)
    for player in final_dict[team] :
        print(final_dict[team][player])
    print()
    print()
    print()



file_path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Team Database', '\\ThrowawayFile.dat'])
if pi :
    file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump({}, output_file)

print('Done')
"""

    
    
    
