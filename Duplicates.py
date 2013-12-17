'''
Find Duplicates

Input: list of Size N, integers from 1 to n
Output: print out if there are duplicates
'''

def find_duplicates(lista):
    d = {}
    for item in lista:
        if d.get(item) == None:
            d[item] = 1
        else:
            d[item] = d[item] + 1 
    print d
    for key, val in d.iteritems():
        if val > 1:
            print key



print find_duplicates([1,3,4,4,5,6,7,8,8,8,9])