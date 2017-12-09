with open('9.in') as f:
    line = f.readline().strip()

stack = []
scores = 0
previous = ''
prev_was_canceled = False
inside_garbage = False
garbages_counter = 0
removed = 0
for i in line:
    if previous == '!' and not prev_was_canceled:
        previous = i
        prev_was_canceled = True
        continue
    if not inside_garbage:
        if i == '{':
            stack.append(i)
        if i == '}':
            if stack.pop() == '{':
                scores += len(stack) + 1
            else:
                print('error in data')
    if i == '<':
        if not inside_garbage:
            garbages_counter += 1
            inside_garbage = True
    if i == '>':
        inside_garbage = False
    previous = i
    prev_was_canceled = False
    if inside_garbage and i != '!':
        removed += 1
print(scores)
print(removed - garbages_counter)
