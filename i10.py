def cycle(inp, lengths, count=1):
    result = inp.copy()
    pos = 0
    skip_size = 0
    l = len(inp)
    for c in range(count):
        for i in lengths:
            term = (i + pos)
            if i > 2:
                if term > l:
                    temp = result.copy()
                    for j in range(term // l):
                        temp += result.copy()
                    temp2 = list(reversed(temp[pos:term]))
                    pos2 = pos
                    for t2 in temp2:
                        result[pos2] = t2
                        pos2 = (pos2 + 1) % l
                else:
                    result = result[:pos] + list(reversed(result[pos:term])) + result[term:]
            pos = (pos + i + skip_size) % l
            skip_size += 1
    return result


def get_hash(text):
    lengths = [ord(a) for a in text] + [17, 31, 73, 47, 23]
    second = cycle(circ_list, lengths, 64)

#    print('sparse hash', second)
    dense = []
    counter = 0
    l = len(second)
    while counter < l:
        part = second[counter:counter + 16]
        part_xor = part[0]
        for p in range(1, 16):
            part_xor ^= part[p]
        dense.append(part_xor)
        counter += 16
#    print('dense', dense)
    res = []
    for i in dense:
        pre = '0' if i <= 15 else ''
        res.append(pre + str(hex(i))[2:])
    return ''.join(i for i in res)


# first part
circ_list = list(range(0, 256))
with open('10.in') as f:
    lengths = [int(a) for a in f.readline().strip().split(',')]

first = cycle(circ_list, lengths)
print(first[0] * first[1])

# second part
with open('10.in') as f:
    st = f.readline().strip()
print('hash', get_hash(st))

