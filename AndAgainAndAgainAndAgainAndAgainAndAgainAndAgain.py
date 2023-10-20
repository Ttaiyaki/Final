'''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
def again(text):
    '''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
    text_list = text.split(' ')
    word_list = []
    for txt in text_list:
        word = ''
        for i in txt:
            if i.isalnum():
                word += i
        word_list.append(word)

    newlist = []
    for txt in word_list:
        counting = 0
        for char in txt:
            if char in 'aeiouAEIOU':
                counting += 1

        if counting > 1:
            newlist.append(txt)

    if not newlist:
        return print("Nope")

    newlist.sort()
    for i in newlist:
        print(i)

again(input())
