## Paul Kiripolsky
## CS 125
## Quiz 4
## Problem 4

def check_input(user_input):
    res = False
    #converting string to list makes it easier to work with
    string2List = list(user_input)
    # checking to see if the string is even; if not, don't bother going further
    if len(string2List)%2 != 0:
        return res
    else:
        # mid point: if the string is even, find the mid point to compare...this is equivalent to just one 'w'
        mid = int((len(string2List)/2))
        # compare the ith and mid+ith positions to see if they are the same
        res=[False if string2List[i]!=string2List[mid+i] else True for i in range(0,mid)]
        return res[0] #res becomes a list of boolean values so return the first one
##=====================================================
print("Given the following rules {ww | w ∈ Σ*}")
keep_going = True
while keep_going:
    user_input = input("Please enter a string to test: ")
    res = check_input(user_input)
    if res: #If res returns True
        print("That input string -IS- accepted")
    else:
        print("That input string is -NOT- accepted")
    in_res = (input("Would you like to keep going? (y/n)")).lower()
    if in_res == "n":
        keep_going = False

