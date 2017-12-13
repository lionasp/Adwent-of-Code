def tick(firewall):
    for i in firewall:
        if not i['len']:
            continue
        i['pos'] += i['direction']
        if i['pos'] == 1:
            i['direction'] = 1
        if i['pos'] == i['len']:
            i['direction'] = -1


firewall = []
with open('13.in') as f:
    for line in f.readlines():
        index, val = line.strip().split(': ')
        while len(firewall) < int(index):
            firewall.append({'len': 0, 'pos': None})
        firewall.append({'len': int(val), 'pos': 1, 'direction': 1})

result = 0
for pointer in range(len(firewall)):
    if firewall[pointer]['pos'] == 1:
        result += firewall[pointer]['len'] * pointer
    tick(firewall)
print(result)
