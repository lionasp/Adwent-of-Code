with open('19.in') as f:
    field = f.readlines()

field = [k.rstrip() for k in field]
letters = []

x, y = 0, field[0].index('|')
to = 'b'
empty = ('', ' ')
steps = 0

while True:
    steps +=1
    if field[x][y] not in '|+-':
        letters.append(field[x][y])
    elif field[x][y] == '+':
        try:
            if field[x + 1][y] not in empty and to != 't':
                x += 1
                to = 'b'
                continue
        except IndexError:
            pass
        try:
            if field[x - 1][y] not in empty and to != 'b':
                x -= 1
                to = 't'
                continue
        except IndexError:
            pass
        try:
            if field[x][y + 1] not in empty and to != 'l':
                y += 1
                to = 'r'
                continue
        except IndexError:
            pass
        try:
            if field[x][y - 1] not in empty and to != 'r':
                y -= 1
                to = 'l'
                continue
        except IndexError:
            pass
    if to == 'r' and field[x][y + 1] not in empty:
        y += 1
    elif to == 'l' and field[x][y - 1] not in empty:
        y -= 1
    elif to == 't' and field[x - 1][y] not in empty:
        x -= 1
    elif to == 'b' and field[x + 1][y] not in empty:
        x += 1
    else:
        break

print(''.join(letters))
print(steps)
