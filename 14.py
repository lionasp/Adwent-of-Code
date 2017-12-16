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


inp = 'ugkiagan'
s = ['%s-%s' % (inp, i) for i in range(128)]
h = get_hash(s[0])
counter = 0
field = []
for i in s:
    bn = to_bin(get_hash(i))
    field.append(bn)
    for j in bn:
        counter += int(j)
print(counter)
size = 128

marker = 0


def mark(i, j):
    field[i] = ''.join(field[i][:j]) + '*' + ''.join(field[i][j + 1:])
    if (i + 1) < size and field[i + 1][j] == '1':
        mark(i + 1, j)
    if i and field[i - 1][j] == '1':
        mark(i - 1, j)
    if j and field[i][j - 1] == '1':
        mark(i, j - 1)
    if (j + 1) < size and field[i][j + 1] == '1':
        mark(i, j + 1)


for i in range(size):
    for j in range(size):
        try:
            if field[i][j] == '1':
                mark(i, j)
                marker += 1
        except IndexError:
            print(i,j)

print(marker)