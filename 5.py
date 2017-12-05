with open('5.in') as f:
    raw_line = f.readlines()
line = [int(i) for i in raw_line]
cursor = 0
l = len(line)
jumps = 0

while cursor < l:
    next_jump_size = line[cursor]
    line[cursor] += 1
    cursor += next_jump_size
    jumps += 1

print(jumps)

line = [int(i) for i in raw_line]
cursor = 0
jumps = 0
# second part
while cursor < l:
    next_jump_size = line[cursor]
    line[cursor] += 1 if next_jump_size < 3 else -1
    cursor += next_jump_size
    jumps += 1

print(jumps)