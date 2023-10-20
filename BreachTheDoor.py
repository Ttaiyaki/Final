'''BreachTheDoor'''
def decoding(text):
    '''BreachTheDoor'''
    text_list = text.split(" ")
    massage = []

    for txt in text_list:
        word = ''.join(i for i in txt if i.isalpha())
        if len(word) > 6:
            massage.append(word)
    print(*massage)
decoding(input())
