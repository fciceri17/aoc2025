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

start = next(i for i, x in enumerate(data[0]) if x =='S')
spots = defaultdict(list)
for i, row in enumerate(data[1:]):
    for j, v in enumerate(row):
        if v=='^':
            spots[j].append(i)
splits=set()

@cache
def explore_from_node(node):
    row, column = node
    for x in spots[column]:
        if x>row:
            splits.add((x,column))
            return explore_from_node((x, column+1))+explore_from_node((x, column-1))
    else:
        return 1

print(explore_from_node((0,start)), len(splits))