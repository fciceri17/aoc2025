from functools import cache
from itertools import accumulate

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# data='''aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out'''.split('\n')

# data='''svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out'''.split('\n')


edges = {}
for row in data:
    node = row.split(': ')[0]
    for dest in row.split(': ')[1].split(' '):
        if node not in edges:
            edges[node] = []
        edges[node].append(dest)

@cache
def recurse_reach(start='you', end='out'):
    if start==end:
        return 1
    return sum(recurse_reach(n, end) for n in edges.get(start, []))

print(recurse_reach())

#determine loop direction
f_d = recurse_reach('fft', 'dac')
d_f = recurse_reach('dac', 'fft')
if d_f==0:
    s_f = recurse_reach('svr', 'fft')
    d_o = recurse_reach('dac','out')
    print(s_f*f_d*d_o)
else:
    s_d = recurse_reach('svr', 'dac')
    f_o = recurse_reach('fft','out')
    print(s_d*d_f*f_o)