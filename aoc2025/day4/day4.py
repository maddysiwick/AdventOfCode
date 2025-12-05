input=open('Input.txt','r')
lines = input.readlines()

grid=[]
dirs=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

for line in lines:
    grid.append(list(line.strip("\n")))

for row in grid:
    print(row)  

total=0
possible=True
while possible:
    removedThisRound=False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]=='@':
                paperCount=0
                for dir in dirs:
                    adjy, adjx = y + dir[0], x + dir[1]
                    if 0 <= adjy < len(grid) and 0 <= adjx < len(grid[0]):
                        if grid[adjy][adjx] == '@':
                            paperCount += 1
                if paperCount<4:
                    grid[y][x]='x'
                    removedThisRound=True
                    total+=1
    if not removedThisRound:
        possible=False

print(total)