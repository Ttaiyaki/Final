'''AscendingSort'''
def sorting():
    '''AscendingSort'''
    listed = []
    for _ in range(5):
        listed.append(int(input()))

    listed.sort()
    for num in listed:
        print(num)
sorting()
