class Node:
    def __init__(self, value, relations=None):
        self.value = value
        self.relations = [int(r) for r in relations if int(r) != value] if relations else []

    def __repr__(self):
        return '{} <-> {}'.format(self.value, self.relations)


nodes = {}
not_founded = []
with open('12.in') as f:
    for line in f.readlines():
        split = line.strip().split(' <-> ')
        value = int(split[0])
        nodes[value] = Node(value, split[1].split(', '))
        not_founded.append(value)


def find(k):
    if k.value == needed:
        return True

    visited[k.value] = True
    for relation in k.relations:
        if not visited[relation]:
            if find(nodes[relation]):
                return True
    return False


result1 = []
groups_counter = 0
not_founded = list(reversed(not_founded))
while not_founded:
    needed = not_founded.pop()
    for node in nodes.values():
        if node.value not in not_founded and node.value != needed:
            continue
        visited = {n: False for n in nodes}
        if find(node):
            if needed == 0:
                result1.append(node.value)
            if node.value in not_founded:
                not_founded.remove(node.value)

    groups_counter += 1

print(len(result1))
print(groups_counter)


