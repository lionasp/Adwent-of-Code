puzzle = 386
buffer = [0]
pos = 0
for i in range(1, 2018):
    pos = (pos + puzzle) % len(buffer) + 1
    buffer = buffer[:pos] + [i] + buffer[pos:]
print(buffer[buffer.index(2017) + 1])


pos = 0
result = 0
for i in range(1, 50000001):
    pos = (pos + puzzle) % i
    if pos == 0:
        result = i
    pos += 1
print(result)
