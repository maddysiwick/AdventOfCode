input=open('Input.txt','r')
lines = input.readlines()

ranges=[[],[]]
ids=[]

for line in lines:
    line=line.strip("\n")
    if '-' in line:
        parts=line.split('-')
        ranges[0].append(int(parts[0]))
        ranges[1].append(int(parts[1]))
    elif line!='':
        ids.append(int(line))

total=0

for id in ids:
    fresh=False
    for i in range(len(ranges[0])):
        if ranges[0][i]<=id<=ranges[1][i]:
            fresh=True
            break
    if fresh:
        total+=1
print(total)