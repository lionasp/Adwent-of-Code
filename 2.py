with open('2.in') as f:
    diffs = []
    dividers = []
    for line in f.readlines():
        numbers = [int(i) for i in line.split()]
        diffs.append(max(numbers) - min(numbers))
        br = 0
        for i in numbers:
            for j in numbers:
                if i != j and i % j == 0:
                    dividers.append(i // j)
                    br = 1
                    break
            if br:
                break
    print(sum(diffs))
    print(sum(dividers))
