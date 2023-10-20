'''Classify unfinished'''
def classify():
    '''Classify'''
    student_list = []
    while True:
        student_id = input()
        if student_id == 'END':
            break
        studentcount = [int(student_id[:2]), int(student_id[2:4]), 1]
        if studentcount in student_list:
            student_list[student_list.index(studentcount)][2] += 1
            continue
        student_list.append(studentcount)

    student_list.sort()

    for i in range(len(student_list)):
        if student_list[i][0] == student_list[(i-1)][0]\
            and student_list[i][1] != student_list[(i-1)][1]:
            print('--', *student_list[i][1:])
            continue
        print(*student_list[i])

classify()
