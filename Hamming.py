'''Hamming'''
def hamming(text1, text2):
    '''Hamming'''
    hamming_list = [text1[i] for i in range(len(text1)) if text1[i] != text2[i]]
    print(len(hamming_list))
hamming(list(input()), list(input()))
