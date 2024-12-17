def decoder(data):
    # data = sys.stdin.read()
    # data = '.....'
    if not isinstance(data, str):
        raise ValueError
    res = []
    dot_count = 0
    sub_str = ''
    for i in range(len(data)):
        if data[i] == '.':
            if sub_str:
                res.append(sub_str)
                sub_str = ''
            dot_count += 0.5
        else:
            if dot_count:
                res.append(dot_count)
                dot_count = 0
            sub_str += data[i]
    if sub_str:
        res.append(sub_str)
    elif dot_count:
        res.append(dot_count)
    for uid, ent in enumerate(res):
        if isinstance(ent, float):

            if ent % 1 != 0:
                whole_part = ent - 0.5
            else:
                whole_part = ent
            if uid != 0:
                if whole_part >= len(res[uid - 1]):
                    res[uid - 1] = ''
                    res[uid] = ''
                else:
                    res[uid - 1] = res[uid - 1][:len(res[uid - 1]) - int(whole_part)]
                    res[uid] = ''
            else:
                res[uid] = ''
    # print(res)
    # print(''.join(res))
    return ''.join(res)


if __name__ == '__main__':
    decoder(input("Введите строку: "))