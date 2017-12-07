with open('7.in') as f:
    raw_items = [x.strip() for x in f.readlines()]
all_names = []
childs = []
for i in raw_items:
    i_split = i.split(' -> ')
    main = i_split[0].split()
    all_names.append(main[0])
    childs.extend(i_split[1].split(', ') if len(i_split) == 2 else [])
print(set(all_names) - set(childs))
