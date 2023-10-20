'''Diamond I'''
def diamond1(numm, numn):
    '''Diamond I'''
    diamond_list = [0 for _ in range(numn)]
    for _ in range(numm):
        diamond = input().split(" ")
        for i in range(numn):
            diamond_list[i] += int(diamond[i])

    most = max(diamond_list)
    print(most)
diamond1(int(input()), int(input()))
