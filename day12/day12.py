with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')

blocks = []
for d in data[:-1]:
    block = ''.join(d.split('\n')[1:])
    blocks.append(block.count('#'))

filled = 0
for space in data[-1].split('\n'):
    grid, needs = space.split(': ')
    size = eval(grid.replace('x', '*'))
    needs = [int(x) for x in needs.split(' ')]
    req_area = sum(needed * blocks[i] for i, needed in enumerate(needs))
    if req_area <= size:
        filled += 1
print(filled)
