import re

with open('input.txt', 'r') as f:
    data = f.read().split(',')

# data='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''.split(',')

to_match=re.compile(r'^(\d+)\1+$')
detected=[]
detected2=[]
for ranges in data:
    start, end = [int(x) for x in ranges.split('-')]
    for a in range(start, end+1):
        # bad split attempt
        reading = str(a)
        if len(reading)%2==0:
            start,end = reading[len(reading)//2:],reading[:len(reading)-len(reading)//2]
            if start==end:
                detected.append(a)
        if to_match.match(reading):
            detected2.append(a)



print(sum(detected), sum(detected2))