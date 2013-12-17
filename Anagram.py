
"""
Anagram 
(A word, phrase, or name formed by rearranging the letters of anothe)

Give a list of strings, return a list of anagram sets just from the original input.

Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]
    """

def sort_word(world):
    result = []
    for letter in world:
        result.append(letter)
    result = sorted(result)
    return ''.join(result)



def return_anagrams(lista):
    d = {}
    for word in lista:
        sorted_w = sort_word(word)
        if d.get(sorted_w) == None:
            d[sorted_w] = [word]
        else:
            d[sorted_w].append(word)
    result = []
    for key, val in d.iteritems():
        if len(val) > 1:
            result.append(val)
    return result 



print return_anagrams(['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food'])
