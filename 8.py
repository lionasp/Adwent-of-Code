with open('8.in') as f:
    lines = [l.strip() for l in f.readlines()]

indexes = set()
for line in lines:
    after_split = line.split()
    try:
        globals()[after_split[0]] = 0
        indexes.add(after_split[0])
    except TypeError:
        print(line)

maximum_ever = int(-100500)
for line in lines:
    code = line + ' else 0'
    if 'inc' in code:
        code = code.split(' inc ')
        globals()[code[0]] += eval(code[1])
    else:
        code = code.split(' dec ')
        globals()[code[0]] -= eval(code[1])
    maximum_ever = max(globals()[code[0]], maximum_ever)

values = [globals()[i] for i in indexes]

print(max(values))
print(maximum_ever)