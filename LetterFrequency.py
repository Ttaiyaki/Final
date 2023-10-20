'''LetterFrequency'''
def letter(sentence):
    '''LetterFrequency'''
    dict_char = {}
    for char in sentence:
        if not char.isalpha():
            continue
        if char.lower() and not char in dict_char:
            dict_char.update({char: 1})
        else:
            dict_char[char] += 1
    most = max(dict_char, key=dict_char.get)
    print(most)
letter(input())
