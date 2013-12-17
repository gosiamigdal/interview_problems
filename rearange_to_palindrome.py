'''
Palindrome Part 2 

Input: List of words
Output: Rearrange each word if can be a palindrome, otherwise replace with -1 and return the list

'''


def rearrange_to_palindrome_word(string):
    sort = []
    for letter in string:
        sort.append(letter)
    sort = sorted(sort)
    if len(sort) % 2 == 0:
        i = 0
        half = []
        while i < len(sort) - 1:
            if sort[i] != sort[i + 1]:
                return -1
            half.append(sort[i])
            i += 2
        return "".join(half) + "".join(half[::-1])
    else:
        d = {}
        for letter in sort:
            if d.get(letter) == None:
                d[letter] = 1
            else:
                d[letter] = d[letter] + 1 
        result = []
        half = []
        for key, val in d.iteritems():
            for i in range(val / 2):
                half.append(key)
            if val % 2 != 0:
                result.append(key)
        if len(result) == 1:
            return "".join(half) + result[0] + "".join(half[::-1])
        else:
            return -1


def rearrange_to_palindrome_word_2(string):
    if len(string) % 2 == 0:
        sort = sorted([letter for letter in string])
        half = []
        for i in range(0, len(sort), 2):
            if sort[i] != sort[i + 1]:
                return -1
            half.append(sort[i])
        return "".join(half) + "".join(half[::-1])
    else:
        d = {}
        for letter in string:
            d[letter] = d.get(letter, 0) + 1
        result = []
        half = []
        for key, val in d.iteritems():
            for i in range(val / 2):
                half.append(key)
            if val % 2 != 0:
                result.append(key)
        if len(result) == 1:
            return "".join(half) + result[0] + "".join(half[::-1])
        else:
            return -1
    

def rearrange_to_palindrome(lista):
    final = []
    for item in lista:
        final.append(rearrange_to_palindrome_word_2(item))
    return final

print rearrange_to_palindrome(["kkaa", "string","aaa", "aaaab"])



