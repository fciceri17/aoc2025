import re
from math import prod
with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# data='''123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  '''.split('\n')


ops = len(data[0].split())
cols = [[] for _ in range(ops)]
tot=0
for entry in data:
        for i,num in enumerate(entry.strip().split()):
            if re.match(r'\d+', num):
                cols[i].append(int(num))
            else:
                if num=='+':
                    tot+=sum(cols[i])
                else:
                    tot+=prod(cols[i])

print(tot)

