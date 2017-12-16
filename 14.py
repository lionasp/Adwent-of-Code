from i10 import get_hash
table = {
    'f': '1111',
    'e': '1110',
    'd': '1101',
    'c': '1100',
    'b': '1011',
    'a': '1010',
    '9': '1001',
    '8': '1000',
    '7': '0111',
    '6': '0110',
    '5': '0101',
    '4': '0100',
    '3': '0011',
    '2': '0010',
    '1': '0001',
    '0': '0000'
}


def to_bin(hash):
    return ''.join(table[i] for i in hash)


inp = 'flqrgnkx'
s = ['%s-%s' % (inp, i) for i in range(128)]
print(s[0])
h = get_hash(s[0])
print(h)
print(to_bin(h))
counter = 0
for i in s:
    bn = to_bin(get_hash(i))
    for j in bn:
        counter += int(j)
print(counter)
