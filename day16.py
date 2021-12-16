def biToDec(bi):
    dec = 0
    twoPow = 2 ** (len(bi) - 1)
    for i in bi:
        #print(twoPow)
        dec += int(i) * twoPow
        twoPow /= 2
    return dec

def decode(packet):
    version = biToDec(packet[0:3])
    typeID = biToDec(packet[3:6])
    if typeID == 4:
        print('number')
    count = 0
    buff = ''
    num = ''
    for i in range(6, len(packet), 1):
        count += 1
        buff += packet[i]
        if count % 5 == 0:
            ##if buff[0] == '0':
              #  break
            print(buff[1:])
            num += buff[1:]
            print(buff)
            buff = ''
    #print(version, typeID)
    print()
    print(num,biToDec(num))

        

file = open("input-2021-16.txt")

hexBuff = [i for i in file.readline().strip()]

#print(hexBuff)

bi = ''

for i in hexBuff:
    if i == '0':
        bi += '0000'
    elif i == '1':
        bi += '0001'
    elif i == '2':
        bi += '0010'
    elif i == '3':
        bi += '0011'
    elif i == '4':
        bi += '0100'
    elif i == '5':
        bi += '0101'
    elif i == '6':
        bi += '0110'
    elif i == '7':
        bi += '0111'
    elif i == '8':
        bi += '1000'
    elif i == '9':
        bi += '1001'
    elif i == 'A':
        bi += '1010'
    elif i == 'B':
        bi += '1011'
    elif i == 'C':
        bi += '1100'
    elif i == 'D':
        bi += '1101'
    elif i == 'E':
        bi += '1110'
    elif i == 'F':
        bi += '1111'




#print(bi)
decode(bi)
