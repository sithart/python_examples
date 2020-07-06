alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# word = 'hello'
# word_1 = 'ebiil'
# word_1 = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
word_1 = 'xuo'
offset = 10

# Encode the message


def encode(word, offset):
    arr = []
    word = word.lower()
    for elt in word:
        ind = alphabet.index(elt)
        arr.append(alphabet[ind-offset])
    return ''.join(arr)


# print(encode(word, offset))


# Decode the message

def decode(word_1, offset):
    if len(word_1.split()) < 2:
        arr = []
        for elt in word_1:
            ind = alphabet.index(elt)
            arr.append(alphabet[ind+offset])
        return ''.join(arr)

    else:
        word_spliting = word_1.split()
        arr = []
        for data in word_spliting:
            for elt in data[0]:
                ind = alphabet.index(elt)
                arr.append(alphabet[ind - offset])
        return ''.join(arr)


print(decode(word_1, offset))
