commands = {}
with open('20.in') as f:
    n = 0
    for r in f.readlines():
        split = r.strip().split(', ')
        commands[n] = {'p': [int(i) for i in split[0][3:-1].split(',')],
                       'v': [int(i) for i in split[1][3:-1].split(',')],
                       'a': [int(i) for i in split[2][3:-1].split(',')]}
        n += 1


for i in range(10 ** 3):
    for n in commands:
        for m in range(3):
            commands[n]['v'][m] += commands[n]['a'][m]
            commands[n]['p'][m] += commands[n]['v'][m]

min_distance = abs(sum([abs(i) for i in commands[0]['p']]))
index = 0
for n in commands:
    check = abs(sum([abs(i) for i in commands[n]['p']]))
    if check < min_distance:
        min_distance = check
        index = n

print(min_distance)
print(index)
