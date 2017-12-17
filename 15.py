a = 883
b = 879

judge = 0
to = 40000000
for i in range(to):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if str(bin(a))[-16:] == str(bin(b))[-16:]:
        judge += 1
print(judge)

# part 2
a = 883
b = 879

judge = 0
to = 5000000
for i in range(to):
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            break
    if str(bin(a))[-16:] == str(bin(b))[-16:]:
        judge += 1
print(judge)
