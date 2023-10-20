'''PrasomSib?'''
def sibsib(num):
    '''PrasomSib'''
    count = 0
    for i in range(1, len(num)):
        if i == 0:
            if int(num[0])+int(num[1]) == 10:
                count += 1
        elif i == len(num)-1:
            if int(num[i-1]) + int(num[i]) == 10:
                count += 1
        elif int(num[i-1])+int(num[i]) == 10 and int(num[i])+int(num[i+1]) == 10:
            count += 2
        elif int(num[i-1])+int(num[i]) == 10 or int(num[i])+int(num[i+1]) == 10:
            count += 1

    print(count)

sibsib(input())
