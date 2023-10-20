'''Inverter'''
def invert(binum):
    '''Inverter'''
    binum_invert = ""
    for num in binum:
        if num == "0":
            binum_invert += "1"
        else:
            binum_invert += "0"

    count = 0
    for num in binum_invert:
        if num == "1":
            break
        count += 1
    print(binum_invert[count:])
invert(input())
