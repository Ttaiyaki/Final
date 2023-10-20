'''RemoveTag'''
import re
def removetag(string):
    '''RemoveTag'''
    new = (re.sub('<.*?>', ' ', string)).split(' ')

    if not new:
        return print(string.split(' '))
    listed = [word for word in new if not word == '']
    print(listed)
removetag(input())
