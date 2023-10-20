'''WordSequence II'''
def wordseq2(word1, word2):
    '''WordSequence II'''
    for i in range(max(len(word1), len(word2))+1):
        new = word2[0:i]+word1[i:]
        print(new)
wordseq2(input(), input())
