input=open('exInput.txt','r')
lines = input.readlines()

tiles=[]
width=0
length=0

for line in lines:
    coords=line.strip("\n").split(",")
    c1=int(coords[0])
    c2=int(coords[1])
    tiles.append((c1,c2))

horizontal=True
fuckass=[tiles[0]]

for i in range(len(tiles)-1):
    rule=tiles[i][1] if horizontal else tiles[i][0]
    fuckass.append(rule)
    fuckass.append(tiles[i+1])
    horizontal=not horizontal

print(fuckass)

p1=tiles[0]

qPoints=[(p1[0]-1,p1[1]-1),(p1[0]+1,p1[1]-1),(p1[0]-1,p1[1]+1),(p1[0]+1,p1[1]+1)]
sPoints=[(p1[0]-1,0),(p1[0]+1,0),(p1[0]-1,0),(p1[0]+1,0)]

quads=[]

for i in range(len(qPoints)):
    q=qPoints[i]
    s=sPoints[i]
    crosses=0
    for j in range(1,len(fuckass),2):
        bound1=fuckass[j-1] if fuckass[j-1][0]<fuckass[j+1][0] else fuckass[j+1]
        bound2=fuckass[j-1] if fuckass[j-1][0]>fuckass[j+1][0] else fuckass[j+1]
        if(bound1[0]<q[0]<bound2[0]) and (q[1]<fuckass[j]<s[1]):
            crosses+=1
    if crosses%2==0:
        quadrant=True
    else:
        quadrant=False
    quads.append(quadrant)

corners={}
corners.update({p1:quads})

print(corners)