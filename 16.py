with open('16.in') as f:
    movies = f.readline().strip().split(',')
#letters = list('abcde')
letters = list('abcdefghijklmnop')

# todo: not optimized
def dance(letters, counter=1):
    for _ in range(counter):
        if _ % 1000 == 0:
            print(_)
        for move in movies:
            if move[0] == 's':
                n = int(move[1:]) % len(letters)
                letters = letters[-n:] + letters[:-n]
            if move[0] == 'x':
                slash = move.index('/')
                i = int(move[1:slash])
                j = int(move[slash+1:])
                letters[i], letters[j] = letters[j], letters[i]
            if move[0] == 'p':
                slash = move.index('/')
                i = letters.index(move[1:slash])
                j = letters.index(move[slash+1:])
                letters[i], letters[j] = letters[j], letters[i]
    return ''.join(letters)

print(dance(letters))
print(dance(letters, counter=1000000))