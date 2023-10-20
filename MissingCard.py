'''MissingCard (No Set)'''
def missingcard():
    '''MissingCard (No Set)'''
    cardset = set()
    rank = ["S", "H", "D", "C"]
    num = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in range(len(num)):
        for j in range(len(rank)):
            cardset.add(num[i]+rank[j])

    cardset2 = set()
    for i in range(51):
        card = input()
        cardset2.add(card)
    differ = cardset.difference(cardset2)
    print(*differ)
missingcard()
