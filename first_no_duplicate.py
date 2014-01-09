# Given a list of integeres, find and return firs one, which has no duplicates in this list

def no_dup(some_list):
    d = {}
    for item in some_list:
        if d.get(item) == None:
            d[item] = 1
        else:
            d[item] = d[item] + 1 
    for item in some_list:
        if d[item] == 1:
            return item
    return "Just duplicates here"




print no_dup([1,1,5,5,5,5])