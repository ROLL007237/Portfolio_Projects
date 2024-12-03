def decodeMessage(key, message):
    k = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_nodupes = ''

    for i in key:
        if (not (i in key_nodupes) and i != ' '):
            key_nodupes += i


    for i, v in enumerate(alphabet):
        k[key_nodupes[i]] = v

    output = ''
    for i in message:
        if i == ' ':
            output+=' '
        else:
            output+= k[i]
    return output


print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb"))