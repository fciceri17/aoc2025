from math import sqrt

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

conn=1000

# data, conn='''162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689'''.split('\n'), 10


def make_box(coords):
    return map(int, coords.split(','))

boxes = [tuple(make_box(x)) for x in data]
distances = {}
for i, box in enumerate(boxes):
    for j in range(i+1, len(boxes)):
        target =  boxes[j]
        distances[(i,j)] = sum(abs(box[n]-target[n])**2 for n in range(3))

links = sorted(distances.keys(), key=lambda x: distances[x])[:conn]

graph = {i:set() for i in range(len(boxes))}
for link in links:
    graph[link[0]].add(link[1])
    graph[link[1]].add(link[0])

def visit_graph(start):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        for adj in graph[node]:
            if adj not in visited:
                queue.append(adj)
    return visited

complete_sets = {i: visit_graph(i) for i in graph}
tot=1
for _ in range(3):
    max_size = max(complete_sets.keys(), key=lambda x: len(complete_sets[x]))
    tot*=len(complete_sets[max_size])
    for node in complete_sets[max_size]:
        del complete_sets[node]
print(tot)