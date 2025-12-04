with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# data='''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''.split('\n')

all_removed = set()
def in_bounds(map_, i, j):
    max_i = len(map_)
    max_j = len(map_[0])
    if i < 0 or i >= max_i or j < 0 or j >= max_j:
        return False
    return True

def find_neighbors(location, map_):
    neighbors = set()
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1,-1), (-1,1), (1,1), (1,-1)]:
        if (location[0] + i, location[1] + j) not in all_removed and in_bounds(map_, location[0] + i, location[1] + j) and map_[location[0] + i][location[1] + j] == '@':
            neighbors.add((location[0] + i, location[1] + j))
    return neighbors

def movable(location, map_):
    if map_[location[0]][location[1]] == '@':
        neighbors = find_neighbors(location, map_)
        return len(neighbors) <4
    return False

print(sum(movable((i, j), data) for j in range(len(data)) for i in range(len(data[j]))))

curr_removed = set((i,j) for j in range(len(data)) for i in range(len(data[j])) if movable((i,j), data))
while curr_removed:
    all_removed.update(curr_removed)
    curr_removed = set((i, j) for j in range(len(data)) for i in range(len(data[j])) if movable((i, j), data) and (i,j) not in all_removed)
print(len(all_removed))