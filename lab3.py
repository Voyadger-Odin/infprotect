


def hash(text):
    result = 0

    for i in range(len(text) - 1):
        result += ( (ord(text[i]) - ord(text[i + 1])) * ord(text[i]) + ord(text[i + 1]) ) ** 2
    return result

def hashCrypt(text):

    l = 64

    result = ''
    resultInt = 0

    start = 97
    end = 122
    abc = ''
    for i in range(10):
        abc += str(i)
    for c in range(start, end + 1):
        abc += chr(c)



    for i in range(len(text)):
        resultInt += (ord(text[i]) + len(str(resultInt))) ** 2
        if i < len(text) - 1:
            #resultInt *= len(str(resultInt))
            resultInt += ((ord(text[i + 1]) * ord(text[i])) + len(str(resultInt))) ** 3
            ...


    resultInt *= len(text)
    resultInt **= 11

    larg = len(abc) ** l - 1

    # Уменьшаем
    while (larg < resultInt):
        #print(resultInt)
        resultInt = int(resultInt / (len(abc) * 2)) * (resultInt % len(abc) + 1)

    # Уселичиваем
    while (larg > resultInt):
        resultInt *= 11
        resultInt **= 2

    while resultInt > 0 and len(result) < l:
        ost = resultInt % (len(abc))
        result += abc[ost]
        resultInt = int(resultInt / len(abc))

    #print(len(result), result)
    return result



def collisionTest(itter, lensim, func):
    countCollisions = 0
    collisions = []

    data = 1 * (10 ** (lensim - 1))
    for i in range(itter):
        h = func(str(data))
        #print('TEST', i, 'hash', h, 'data', data, end=' ')
        if (h in collisions):
            countCollisions += 1
            #print('OK', end='')
        else:
            collisions.append(h)

        #print()


        data += 1

    print('COLLISIONS:', countCollisions, '=', f'{countCollisions / itter * 100}%')


def main():

    text = '1235'
    result = hash(text)
    print(result)


    #collisionTest(200, 2, hash)
    #collisionTest(1500, 300, hashCrypt)



    #hashCrypt('1000000005')
    #hashCrypt('1000000050')
    #print(hashCrypt('100000000000000000000000000000001'))
    #print(hashCrypt('100000000000000000000000000000002'))
    #hashCrypt('hello world jsbajg bksabgk bsakgbas')



if __name__ == '__main__':
    main()