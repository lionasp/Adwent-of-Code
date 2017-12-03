with open('2.in') as f:
    diffs = []
    for line in f.readlines():
        numbers = [int(i) for i in line.split()]
        diffs.append(max(numbers) - min(numbers))
    print(sum(diffs))
