'''SMS'''
def telsms(num):
    '''SMS'''
    buttontel = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
                 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
                 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
    text = ''
    for _ in range(num):
        button = int(input())
        if button == 1:
            if not text:
                continue
            text = text[:len(text)-1]
            continue

        time = int(input())
        if time == 0:
            continue

        if button == 7 or button == 9:
            time = (time%4)-1
            text += buttontel[button][time]
        else:
            time = (time%3)-1
            text += buttontel[button][time]

    if not text:
        return print("null")
    print(text)

telsms(int(input()))
