with open('18.in') as f:
    commands = [l.strip() for l in f.readlines()]

registers = {}
last = 0
biggest = -100000001
index = 0
while True:
    split = commands[index].split()
    registers.setdefault(split[1], 0)

    try:
        sp = int(split[2])
    except ValueError:
        registers.setdefault(split[2], 0)
        sp = registers[split[2]]
    except IndexError:
        sp = None

    if split[0] == 'set':
        registers[split[1]] = sp
    elif split[0] == 'add':
        registers[split[1]] += sp
    elif split[0] == 'mul':
        registers[split[1]] *= sp
    elif split[0] == 'mod':
        registers[split[1]] %= sp
    elif split[0] == 'rcv' and registers[split[1]]:
        print(last)
        break
    elif split[0] == 'snd':
        last = registers[split[1]]
        if last != 0:
            biggest = last
    elif split[0] == 'jgz' and registers[split[1]]:
        index += (sp - 1) if sp > 0 else sp
        continue
    index += 1


