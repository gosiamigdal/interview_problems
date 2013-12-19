# Given a list of integers, return first integers from the lis, which has no duplicates 

def return_first_no_duplicate(some_list):
    d = {}
    for i in some_list:
        if d.get(i) == None:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for j in some_list:
        if d[j] == 1:
            return j
        else:
            return "Just duplicates in this list..."



print return_first_no_duplicate([3,4,5,5,7,8,9,7,8,0,2])
print return_first_no_duplicate([3,3])