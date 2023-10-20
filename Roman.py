'''Roman'''
def roman(romannum):
    '''Roman'''
    year = 0
    for i in romannum:
        if i == 'I':
            year += 1
        if i == 'V':
            year += 5
        if i == 'X':
            year += 10
        if i == 'L':
            year += 50
        if i == 'C':
            year += 100
        if i == 'D':
            year += 500
        if i == 'M':
            year += 1000
    print(year)
roman(input())