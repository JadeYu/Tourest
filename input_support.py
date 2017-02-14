def str2nlist(string):
    i = 0
    result = []
    sn = ''
    while i < len(string):
        if string[i] != ',':
            sn += string[i]
        else:
            result.append(int(sn))
            sn = ''
        i += 1
    result.append(int(sn))
    return result

def add_num(names):
    nnames = []
    for i in range(len(names)):
        nnames.append('{}. {}'.format(str(i+1), names[i]))
    return nnames
