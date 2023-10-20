'''FibonacciRecursionV1'''
def fibonacciv1(num):
    '''FibonacciRecursionV1'''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacciv1(num-1) + fibonacciv1(num-2)
print(fibonacciv1(int(input())))
