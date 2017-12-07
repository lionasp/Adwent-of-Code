inp = '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5'

blocks = list(map(int, inp.split()))
l = len(blocks)
loop_counter = 0
exists_blocks = [str(blocks)]
while True:
    loop_counter += 1
    max_index = blocks.index(max(blocks))
    distribution = blocks[max_index] // (l - 1) if blocks[max_index] > l else 1
    distrib_counter = blocks[max_index]
    blocks[max_index] = 0
    index = max_index + 1

    while distrib_counter > 0:
        index = index % l
        blocks[index] += distribution
        index += 1
        distrib_counter -= distribution
        if distrib_counter < 0:
            blocks[index - 1] += distrib_counter
    current_state = str(blocks)
    if current_state in exists_blocks:
        break
    exists_blocks.append(current_state)

print(loop_counter)

# part 2
blocks = list(map(int, inp.split()))
l = len(blocks)
loop_counter = 0
exists_blocks = [str(blocks)]
fixed_state = ''
while True:
    loop_counter += 1
    max_index = blocks.index(max(blocks))
    distribution = blocks[max_index] // (l - 1) if blocks[max_index] > l else 1
    distrib_counter = blocks[max_index]
    blocks[max_index] = 0
    index = max_index + 1

    while distrib_counter > 0:
        index = index % l
        blocks[index] += distribution
        index += 1
        distrib_counter -= distribution
        if distrib_counter < 0:
            blocks[index - 1] += distrib_counter
    current_state = str(blocks)
    if current_state in exists_blocks:
        if current_state == fixed_state:
            break
        if not fixed_state:
            fixed_state = current_state
            loop_counter = 0
    exists_blocks.append(current_state)

print(loop_counter)
