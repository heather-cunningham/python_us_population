# Heather Cunningham
# Python 3.6 MCC Online
# 4/2/17
# Ch's 13 - 18 Cumulative - Analysis_population.py

##The file, USPopulation.txt, lists the population, in thousands, of the United States
##during the years 1950 - 1990 (inclusive).  The first line of the file is the
##population in year 1950, the second line the population in the year 1951 etc.
##
##You are to write a program that reads the contents of the file above
##into a list, and calculate and display:
##
##    --The average annual change in population during the time period
#        1950 - 1990 (inclusive)
##    --The year with the greatest increase in population during the time period
#        1950 - 1990 (inclusive)
##    --The year with the the smallest increase in population during the time
#        period 1950 - 1990 (inclusive)

from census import Census

def find_avg_annual_change(population_list):
    tot_change = 0
    for i in range( (len(population_list) - 1) ):
        j = i + 1
        pop_change = population_list[i].find_change_in_pop(population_list[j].pop)
        tot_change += pop_change
    return tot_change/(len(population_list) - 1)#because 1950 doesn't count because have no data w/ which to compare

def list_changes_in_pop(population_list):
    changes_in_pop = []
    for i in range( (len(population_list) - 1) ):
        j = i + 1
        pop_change = population_list[i].find_change_in_pop(population_list[j].pop)
        changes_in_pop.append( [population_list[j].year, pop_change] )
    return changes_in_pop

def find_max(changes_in_pop_list):
    largest = None
    first_time = True
    for element in changes_in_pop_list:
        if type(element) == type([]):
            max_change = find_max(element)
        else:
            max_change = element
        if first_time or max_change > largest:
            largest = max_change
            first_time = False
    return largest

def find_min(changes_in_pop_list):
    smallest = None
    first_time = True
    for element in changes_in_pop_list:
        if type(element) == type([]):
            min_change = find_min(element)
        else:
            min_change = element
        if first_time or min_change < smallest:
            smallest = min_change
            first_time = False
    return smallest

def match_yr_to_change(population_list, amt_of_change):
    for i in range(len(population_list)):
        j = i + 1
        if population_list[i].find_change_in_pop(population_list[j].pop) == amt_of_change:
            return population_list[j].get_yr()
    
    
pop_file = open("USPopulation.txt", "r")
pop_list = []
start_yr = 1950
end_yr = 1990
while start_yr <= end_yr:
    pop = pop_file.readline()
    census_data = Census(start_yr, int(pop))
    pop_list.append(census_data)
    start_yr +=1

print("The average annual change in US population for the 40 years")
print("from 1950-1990, not counting any change from 1949-1950, was:\n")
print( str(find_avg_annual_change(pop_list)) + "\n" )

max_changes_in_pop = list_changes_in_pop(pop_list)
max_change = find_max(max_changes_in_pop)
print("\nMax increase in population was year: " + str(match_yr_to_change(pop_list, max_change)))
print("With an increase of: " + str(max_change) + "\n" )
#print(max_change)

min_changes_in_pop = list_changes_in_pop(pop_list)
min_change = find_min(min_changes_in_pop)
print("Min increase in population was year: " + str(match_yr_to_change(pop_list, min_change)))
print("With an increase of: " + str(min_change) )
#print(min_change)

pop_file.close()


