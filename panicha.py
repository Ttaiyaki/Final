binary_num = bin(int(input()))[2:]
if len(binary_num) < 11:
    binary_num = '1'*(11-len(binary_num)) + binary_num

binarylist = [int(num) for num in binary_num]

#check 11 pos
if (binarylist[2] + binarylist[4] + binarylist[6] + binarylist[8] + binarylist[10])%2 == 0:
    binarylist[0] = 0
else:
    binarylist[0] = 1

if (binarylist[2] + binarylist[5] + binarylist[6] + binarylist[9] + binarylist[10])%2 == 0:
    binarylist[1] = 0
else:
    binarylist[1] = 1

if (binarylist[4] + binarylist[5] + binarylist[6])%2 == 0:
    binarylist[3] = 0
else:
    binarylist[3] = 1

if (binarylist[8] + binarylist[9] + binarylist[10])%2 == 0:
    binarylist[7] = 0
else:
    binarylist[7] = 1


#check hamming code
errornum = ''
if (binarylist[0] + binarylist[2] + binarylist[4] + binarylist[6] + binarylist[8] + binarylist[10])%2 == 0:
    errornum += '1'
else:
    errornum += '0'

if (binarylist[1] + binarylist[3] + binarylist[5] + binarylist[7] + binarylist[9])%2 == 0:
    errornum += '1'
else:
    errornum += '0'

if (binarylist[3] + binarylist[4] + binarylist[5] + binarylist[6])%2 == 0:
    errornum += '1'
else:
    errornum += '0'

if (binarylist[7] + binarylist[8] + binarylist[9] + binarylist[10])%2 == 0:
    errornum += '1'
else:
    errornum += '0'

print(errornum)

binarylist[binarylist.index(int(errornum, 2))] = abs(int(binarylist.index(int(errornum, 2)))-1)


print(*binarylist)
