with open('5.in') as f:
    line = f.readlines()
line = [int(i) for i in line]
cursor = 0
l = len(line)
jumps = 0

while cursor < l:
    next_jump_size = line[cursor]
    line[cursor] += 1
    cursor += next_jump_size
    jumps += 1

print(jumps)
