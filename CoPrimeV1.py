'''CoPrimeV1'''
def coprimev1(num1, num2):
    '''CoPrimeV1'''
    for i in range(2, min(num1, num2)+1):
        if num1%i == 0 and num2%i == 0:
            return print('{}\n{}'.format("NO", i))
    print('{}\n{}'.format("YES", 1))
coprimev1(int(input()), int(input()))
