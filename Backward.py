'''Backward'''
def backward():
    '''Backward'''
    listed = []
    while True:
        listed.append(input())
        if "NULL" in listed:
            listed.remove("NULL")
            break
    for text in listed[::-1]:
        print(text)
backward()
