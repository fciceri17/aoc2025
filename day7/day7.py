from functools import cache

from pydantic.fields import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')


# data='''.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............'''.split('\n')

start = -1
spots = defaultdict(list)
for i, row in enumerate(data):
    for j, v in enumerate(row):
        if i==0:
            if v=='S':
                start=j
        else:
            if v=='^':
                spots[j].append(i)

beams = [(0, start)]
depth = 0
splits = set()
while beams:
    row, column = beams.pop()
    for x in spots[column]:
        if x>row:
            splitter = (x, column)
            if splitter in splits:
                break
            splits.add(splitter)
            beams.append((x, column+1))
            beams.append((x, column-1))
            break

print(len(splits))

@cache
def explore_from_node(node):
    row, column = node
    for x in spots[column]:
        if x>row:
            return explore_from_node((x, column+1))+explore_from_node((x, column-1))
    else:
        return 1

print(explore_from_node((0,start)))