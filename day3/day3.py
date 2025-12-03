with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# data='''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111'''.split('\n')


joltages=[]
for row in data:
    highest_i = max(range(len(row)-1), key=row.__getitem__)
    second_highest = max(range(highest_i+1, len(row)), key=row.__getitem__)
    joltage = int(row[highest_i]+row[second_highest])
    joltages.append(joltage)
print(sum(joltages))

joltages2=[]
for row in data:
    idx=11
    idxs=[]
    curr_offset=0
    while idx >= 0:
        highest_i = max(range(curr_offset, len(row)-idx), key=row.__getitem__)
        curr_offset = highest_i+1
        idx-=1
        idxs.append(highest_i)
    joltages2.append(int(''.join(row[idx] for idx in idxs)))
print(sum(joltages2))
