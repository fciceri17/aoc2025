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
last=False
op=0
for i in range(len(data[0])):
    num = [v[i] for v in data[:-1]]
    if not all(x==' ' for x in num):
        cols[op].append(int(''.join(num).strip()))
    else:
        op+=1

tot=0
for i,op in enumerate(data[-1].split()):
    if op=='+':
        tot+=sum(cols[i])
    else:
        tot+=prod(cols[i])

print(tot)