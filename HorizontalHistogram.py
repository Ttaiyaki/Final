'''HorizontalHistogram'''
def check(dicted):
    '''check'''
    for key in dicted:
        if key.isupper():
            return ord(key) + 1000
        else:
            return ord(key)

def horixontal(message):
    '''HorizontalHistogram'''
    chardicted = {}
    for key in message:
        if not key in chardicted.keys():
            chardicted.update({key: 1})
        else:
            chardicted[key] += 1

    chardicted_sorting = dict(sorted(chardicted.items(), key=check))
    for key in chardicted_sorting:
        print(key, ": ", end="")
        hyphen = "-"*chardicted_sorting[key]
        hyphennum = len(hyphen)
        while hyphennum > 5:
            print("{}|".format("-"*5), end='')
            hyphennum -= 5
        print("-"*hyphennum)
horixontal(input())
