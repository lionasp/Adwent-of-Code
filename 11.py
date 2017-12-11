with open('11.in') as f:
    moves = f.readline().strip().split(',')

x, y, z = 0, 0, 0
max_distance = 0
for move in moves:
    if move == 'ne':
        x += 1
        z -= 1
    if move == 'se':
        y -= 1
        x += 1
    if move == 's':
        y -= 1
        z += 1
    if move == 'sw':
        x -= 1
        z += 1
    if move == 'nw':
        y += 1
        x -= 1
    if move == 'n':
        y += 1
        z -= 1
    max_distance = max(max_distance, max(abs(x), abs(y), abs(z)))

print(x, y, z)
print(max(abs(x), abs(y), abs(z)))
print(max_distance)