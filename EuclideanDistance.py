'''EuclideanDistance'''
def euclideandistance(num):
    '''EuclideanDistance'''
    all_distance = 0
    for i in range(0, num, 2):
        positon1 = list(input().split(" "))
        postion2 = list(input().split(" "))
        all_distance += distance(positon1, postion2)

    print(all_distance)

def distance(position1,position2):
    '''find diatance'''
    return ((int(position2[0]) - int(position1[0]))**2 + (int(position2[1]) - int(position1[1])))**0.5
euclideandistance(int(input()))