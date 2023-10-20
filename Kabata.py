'''Kabata'''
def kabata(num):
    '''Kabata'''
    list_text = []
    for _ in range(num):
        text = input()
        for i in range(0, len(text), 2):
            list_text.append(text[i:i+2])
    print(try again)


kabata(int(input()))