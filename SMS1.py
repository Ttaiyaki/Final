'''SMS'''
def check(time, numlen):
    '''check'''
    if numlen == 3:
        if time%3 == 1:
            return 0
        if time%3 == 2:
            return 1
        if time%3 == 0:
            return 2
    if numlen == 4:
        if time%4 == 1:
            return 0
        if time%4 == 2:
            return 1
        if time%4 == 3:
            return 2
        if time%4 == 0:
            return 3
def tel_sms(num):
    '''SMS'''
    num2 = ['A', 'B', 'C']
    num3 = ['D', 'E', 'F']
    num4 = ['G', 'H', 'I']
    num5 = ['J', 'K', 'L']
    num6 = ['M', 'N', 'O']
    num7 = ['P', 'Q', 'R', 'S']
    num8 = ['T', 'U', 'V']
    num9 = ['W', 'X', 'Y', 'Z']
    text = ''
    for _ in range(num):
        button = int(input())
        if button == 1:
            if text == '':
                continue
            text = text[:len(text)-1]
            continue
        time = int(input())
        if button == 7 or button == 9:
            numlen = 4
        else:
            numlen = 3
        time = check(time, numlen)

        if button == 2:
            text += num2[time]
        if button == 3:
            text += num3[time]
        if button == 4:
            text += num4[time]
        if button == 5:
            text += num5[time]
        if button == 6:
            text += num6[time]
        if button == 7:
            text += num7[time]
        if button == 8:
            text += num8[time]
        if button == 9:
            text += num9[time]
    if not text:
        return print("null")
    print(text)
tel_sms(int(input()))
