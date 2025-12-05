input=open('Input.txt','r')
lines = input.readlines()

ranges=[]

for line in lines:
    line=line.strip("\n")
    if '-' in line:
        parts=line.split('-')
        parts[0]=int(parts[0])
        parts[1]=int(parts[1])
        ranges.append((parts[0],parts[1]))

ranges.sort()
print(ranges)

for i in range(len(ranges)-1):
    if ranges[i+1][0]<=ranges[i][1]:
        if ranges[i][1]<=ranges[i+1][1]:
            ranges[i+1]=(ranges[i][0],ranges[i+1][1])
            ranges[i]=(-1,-1)
        if ranges[i+1][1]<=ranges[i][1] and ranges[i][0]<=ranges[i+1][0]:
            ranges[i+1]=(ranges[i][0],ranges[i][1])
            ranges[i]=(-1,-1)

while (-1,-1) in ranges:
    ranges.remove((-1,-1))

print(ranges)

total=0

for range in ranges:
    total+=range[1]+1-range[0]



print(total)