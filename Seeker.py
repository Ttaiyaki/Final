'''Seeker'''
def seeker(text):
    '''Seeker'''
    num_list = []
    num = ''
    for i in text+' ':
        if i.isnumeric():
            num += i
        else:
            if not num:
                continue
            num_list.append(int(num))
            num = ''
    print(sum(num_list))
seeker(input())
