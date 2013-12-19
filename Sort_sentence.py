"""
Input: sentence
Output: sort a sentence by length of words


 Input:  This is a fun cat interview
 Output: a is fun this interview
 """


def sort_sentence(string):
    words = string.split()
    d = {}
    for word in words:
        length = len(word)
        if d.get(length) == None:
            d[length] = [word]
        else:
            d[length].append(word)
    lista = []
    for key, val in d.iteritems():
        lista.append((key, val))
    lista = sorted(lista)
    result = []
    for i in lista:
        result.append(i[1])
   

print sort_sentence("This is a fun cat interview")