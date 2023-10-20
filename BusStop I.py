'''BusStop I'''
def busstop(contain, numstation):
    '''BusStop I'''
    peoplelist = []
    end = []
    for station in range(1, numstation+1):
        print('station', station)
        list1 = peoplelist.copy()
        for i in list1:
            if i == str(station):
                end.append(i)
                peoplelist.remove(i)
                print('left', peoplelist)
                print('end', end)

        people = input().split(' ')
        for i in people[1:]:
            if len(peoplelist) >= contain or i == '':
                break
            if int(i) <= station:
                continue
            peoplelist.append(i)
            print('add', peoplelist)

    print(len(end))
busstop(int(input()), int(input()))
