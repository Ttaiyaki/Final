'''Password'''
import math
def password(text):
    '''Password'''
    pool = 0
    for i in text:
        if i.isupper():
            pool += 26
            break
    for i in text:
        if i.islower():
            pool += 26
            break
    for i in text:
        if i.isnumeric():
            pool += 10
            break
    for i in text:
        if not i.isalnum():
            pool += 32
            break

    entropy = int(math.log2(pool**len(text)))
    print(entropy)
    status(entropy)

def status(entropy):
    '''status'''
    if entropy < 28:
        return print("Very Weak")
    if entropy <= 35:
        return print("Weak")
    if entropy <= 59:
        return print("Reasonable")
    if entropy <= 127:
        return print("Strong")
    else:
        return print("Very Strong")

password(input())
