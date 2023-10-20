'''Point Sorting'''
def point_sorting(num):
    '''Point Sorting'''
    point_set = []
    for _ in range(num):
        n_set = int(input())
        for _ in range(n_set):
            point = tuple(input().split(" "))
            point_set.append(point)
        point_set.sort(key=lambda y: y[1], reverse=True)
        point_set.sort(key=lambda x: float(x[0])+float(x[1]))
        for i in point_set:
            print(*i)
        point_set.clear()

point_sorting(int(input()))
