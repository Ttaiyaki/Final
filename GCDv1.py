'''GCD'''
def gcd(num1, num2):
    '''ห.ร.ม.'''
    for i in range(max(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            final = i
            break
    if not final:
        return print(1)
    print(final)
gcd(int(input()), int(input()))
