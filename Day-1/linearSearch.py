# export
"""linearSearch.py"""
import export


#creating function
@export
def linear_locate_card(cards,query):
    no_loop_ran = 0
    locations = []
    for i in range(len(cards)):
        if(query==cards[i]):
            locations.append(i)
            no_loop_ran = i+1
            break
        else:
            no_loop_ran = i+1
    if(locations):
        return locations[0],no_loop_ran
    else:
        return -1,no_loop_ran
    pass







