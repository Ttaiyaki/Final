'''Olympic'''
def olympic(numcountry):
    '''Olympic'''
    country_dict = {}
    for _ in range(numcountry):
        country = input().split()
        country_dict.update({country[0]: [int(i) for i in country[1:]]})

    country_dict = dict(sorted(country_dict.items()))
    country_dict = dict(sorted(country_dict.items()\
                    , key=lambda x: [x[1][0], x[1][1], x[1][2]], reverse=True))

    keylist = list(country_dict.keys())
    valuelist = list(country_dict.values())
    point = ''
    rank_list = [1]
    for i in range(len(keylist)):
        for j in valuelist[i]:
            point += str(j)+' '
        rank = i+1
        if country_dict[keylist[i]] == country_dict[keylist[i-1]]:
            rank_new = rank_list.pop()
            print("{} {} {}{}".format(rank_new, keylist[i], point, sum(country_dict[keylist[i]])))
            rank_list.append(rank_new)
            point = ''
            continue
        print("{} {} {}{}".format(rank, keylist[i], point, sum(country_dict[keylist[i]])))
        rank_list.append(rank)
        point = ''
olympic(int(input()))
