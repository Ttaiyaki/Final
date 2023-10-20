'''Cokw v.2'''
def coke2(price, cap, new_price, want):
    '''Coke v.2'''
    discount = price - new_price
    pay = price*want
    if cap > 0 and want > 0:
        pay -= discount*((want-1)//cap)

    print(int(pay))

coke2(float(input()), float(input()), float(input()), float(input()))
