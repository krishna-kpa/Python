# export
"""binarySearch.py"""
import export

#creating a function for testing the position 

def test_position(cards,query,mid):
    if(cards[mid]==query):
        if(mid!=0):
            if(cards[mid-1]==query):
                return "left"
            else:
                return "found"
        else:
            return "found"
        
    elif(cards[mid]<query):
        return "left"
    elif(cards[mid]>query):
        return "right"

#creating function for binary search
@export
def binary_locate_card(cards,query):
    no_loop_ran = 0
    high,low=len(cards)-1,0
    while(low<=high):
        no_loop_ran = no_loop_ran+1
        mid = (high+low)//2
        result = test_position(cards,query,mid)
        if(result == "found"):
            return mid,no_loop_ran
        elif(result=="right"):
            low = mid+1
        elif(result=="left"):
            high=mid-1
    return -1,no_loop_ran
    pass


