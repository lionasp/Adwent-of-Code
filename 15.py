a = 883
b = 879

judge = 0
to = 40000000
for i in range(to):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if i % 100000 == 0:
        print(i)
    # print(str(bin(a))[-16:])
    # print(str(bin(b))[-16:])
    if str(bin(a))[-16:] == str(bin(b))[-16:]:
        judge += 1
print(judge)
