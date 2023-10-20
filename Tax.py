'''Tax'''
def sizetax(size):
    '''calculate tax by moter size'''
    if size <= 600:
        return size*0.5
    if size <= 1800:
        return 600*0.5 + (1800-600)*1.50
    else:
        return 600*0.5 + (1800-600)*1.50 + (size-1800)*4

def pay(size, discount_percent):
    '''pay'''
    price = sizetax(size) - sizetax(size)*discount_percent
    return print('{:.2f}'.format(price))

def tax(year, size):
    '''Tax - main func'''
    if year == 6:
        return pay(size, 0.1)
    if year == 7:
        return pay(size, 0.2)
    if year == 8:
        return pay(size, 0.3)
    if year == 9:
        return pay(size, 0.4)
    if year == 10:
        return pay(size, 0.5)
    else:
        return pay(size, 0)
tax(int(input()), int(input()))
