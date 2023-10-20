'''AlmostMean'''
def almostmean(num):
    '''AlmostMean'''
    student_dict = {}
    sumscore = 0
    for _ in range(num):
        member = input().split("\t")
        student_dict.update({member[0]: float(member[1])})

    for key in student_dict:
        sumscore += student_dict[key]
    mean = sumscore/num

    almost_list = []
    for key in student_dict.keys():
        if student_dict[key] <= mean:
            almost_list.append([key, student_dict[key]])

    almost_list.sort(key=lambda x: x[1])

    print(*almost_list[len(almost_list)-1], sep='\t')

almostmean(int(input()))
