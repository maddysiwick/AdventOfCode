import functools
input=open('Input.txt','r')
lines = input.readlines()

grid=[]

for line in lines:
    grid.append(list(line.strip("\n")))

@functools.cache
def followBeam(x,y,paths):
    global grid
    if y==len(grid)-1:
        return 1
    elif grid[y+1][x]=='^':
        paths+=followBeam(x-1,y+1,0)
        paths+=followBeam(x+1,y+1,0)
        return paths
    else:
        return followBeam(x,y+1,paths)


start=grid[0].index('S')
splits=followBeam(start,0,0)

print(splits)


