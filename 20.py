from copy import deepcopy

commands = {}
with open('20.in') as f:
    n = 0
    for r in f.readlines():
        split = r.strip().split(', ')
        commands[n] = {'p': [int(i) for i in split[0][3:-1].split(',')],
                       'v': [int(i) for i in split[1][3:-1].split(',')],
                       'a': [int(i) for i in split[2][3:-1].split(',')]}
        n += 1

commands2 = deepcopy(commands)

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

print(index)


# part 2
l_commands = len(commands2)
destroy_count = 0
def check_destroy():
    global destroy_count
    cp = commands2.copy()
    for c in cp:
        founded = False
        try:
            p = commands2[c]['p']
        except:
            continue
        for j in cp:
            if j == c:
                continue
            try:
                commands2[j]
            except:
                continue
            jp = commands2[j]['p']
            if p[0] == jp[0] and p[1] == jp[1] and p[2] == jp[2]:
                del commands2[j]
                destroy_count += 1
                founded = True

        if founded and c in commands2:
            del commands2[c]
            destroy_count += 1


check_destroy()
for i in range(100):
    for n in commands2:
        for m in range(3):
            commands2[n]['v'][m] += commands2[n]['a'][m]
            commands2[n]['p'][m] += commands2[n]['v'][m]
    check_destroy()

print(l_commands - destroy_count)
