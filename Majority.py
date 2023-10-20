'''Majority'''
def voting(candidate, people):
    '''Majority'''
    result = {}
    for i in range(1, candidate+1):
        result.update({i: 0})
    for _ in range(people):
        vote = int(input())
        result[vote] += 1
    most_value = max(result.values())
    key = list(result.keys())
    value = list(result.values())

    if most_value < people/2:
        return print(0, most_value)
    print(key[value.index(most_value)], most_value)

voting(int(input()), int(input()))
