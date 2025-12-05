with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')

# data = '''3-5
# 10-14
# 16-20
# 12-18
# 5-21
#
# 1
# 5
# 8
# 11
# 17
# 32'''.split('\n\n')

ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in  data[0].strip().split('\n')]
ingredients = [int(x) for x in data[1].strip().split('\n')]

fresh = set()
for ingredient in ingredients:
    for range_ in ranges:
        if range_[0] <= ingredient <= range_[1]:
            fresh.add(ingredient)
            break
print(len(fresh))

computed_ranges = set()
for _ in (0,1):
    for range_ in ranges:
        new_range = range_
        for computed_range in list(computed_ranges):
            # new range is entirely contained, ignore
            if new_range[0] >= computed_range[0] and new_range[1] <= computed_range[1]:
                break
            if new_range[0] <= computed_range[0] and new_range[1] >= computed_range[1]:
                # computed range is inside new range, let's remove it
                computed_ranges.remove(computed_range)
            if new_range[0] <= computed_range[0] <= new_range[1] and new_range[1] < computed_range[1]:
                # prepend
                computed_ranges.remove(computed_range)
                new_range = (new_range[0], computed_range[1])
            if computed_range[0] <= new_range[0] <= computed_range[1] and new_range[1] > computed_range[1]:
                # chain
                if computed_range in computed_ranges:
                    computed_ranges.remove(computed_range)
                new_range = (computed_range[0], new_range[1])
        else: # range is not entirely contained since we did not hit break
            computed_ranges.add(new_range)
print(sum(y-x+1 for x,y in computed_ranges))