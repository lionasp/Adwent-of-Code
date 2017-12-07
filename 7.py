with open('7.in') as f:
    raw_items = [x.strip() for x in f.readlines()]
items = {}
all_names = []
childs = []
for i in raw_items:
    i_split = i.split(' -> ')
    main = i_split[0].split()

    all_names.append(main[0])
    childs.extend(i_split[1].split(', ') if len(i_split) == 2 else [])

    items[main[0]] = {
        'weight': int(main[1][1:-1]),
        'childs': i_split[1].split(', ') if len(i_split) == 2 else []
    }

root = list(set(all_names) - set(childs))[0]
print(root)

# recursive calculation weight sum for subtrees
def calculate(name):
    s = items[name]['weight']
    if items[name]['childs']:
        s += sum([calculate(n) for n in items[name]['childs']])
    return s


while True:
    calcs = {}
    for child in items[root]['childs']:
        calcs.setdefault(calculate(child), []).append(child)
    if len(calcs.items()) == 1:
        print('{} is needed key, subtract difference from it'.format(root))
        break
    key = [a[0] for a in calcs.values() if len(a) == 1]
    root = key[0]
    print(calcs)
