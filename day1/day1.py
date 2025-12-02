with open('input.txt', 'r') as f:
    lines = f.readlines()

# lines='''L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82'''.splitlines()

def left(v, i):
    zeros=0
    if v==0:
        zeros -= 1
    out = v-i
    while out<0:
        zeros+=1
        out += 100
    assert zeros>=0
    if out==0:
        zeros += 1
    return out, zeros

def right(v, i):
    zeros=0
    out = v+i
    while out>99:
        out -= 100
        zeros+=1
    return out,zeros

pos=50
password=0
pass2=0
for line in lines:
    turn, amt = line[0], int(line[1:])
    if turn == 'L':
        pos, increment = left(pos, amt)
    else:
        pos, increment = right(pos, amt)
    if pos==0:
        password+=1
    pass2+=increment
    assert increment >= amt//100
print(password, pass2)