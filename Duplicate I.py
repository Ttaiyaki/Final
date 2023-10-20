'''Duplicate I'''
def duplicate(group_m, group_n):
    '''Duplicate I'''
    list_m = []
    list_imposter = []

    for _ in range(group_m):
        list_m.append(input())

    for _ in range(group_n):
        member = input()
        if member in list_m:
            list_imposter.append(member)

    if len(list_imposter) == 0:
        print("Nope")
    else:
        list_imposter.sort(reverse=True)
        for member in list_imposter:
            print(member)
duplicate(int(input()), int(input()))
