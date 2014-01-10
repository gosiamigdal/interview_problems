# Count mode - value, which appears the most frequently in the array


def count_mode(alist):
    d = {}
    for item in alist:
        if d.get(item) == None:
            d[item] = 1
        else:
            d[item] = d[item] + 1 
    tuple_pairs = []
    for key, val in d.iteritems():
        tuple_pairs.append((val, key))
    tuple_pairs = sorted(tuple_pairs)
    return tuple_pairs[len(tuple_pairs) - 1][1]


print count_mode([1,2,2,2,2,8,8,8,8,8,8,8])