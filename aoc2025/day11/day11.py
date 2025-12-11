import functools
input=open('Input.txt','r')
lines = input.readlines()

keys=[]
values=[]

for line in lines:
    line=line.strip("\n").split(":")
    keys.append(line[0])
    values.append(line[1].strip().split())

tree=dict(zip(keys,values))

print(tree)

@functools.cache
def goDownNodes(node,fft,dac):
    global tree
    if node=="fft":
        fft=True
    elif node=="dac":
        dac=True
    if node=="out" and dac and fft:
        return 1
    elif node=="out":
        return 0
    options=tree[node]
    routes=0
    for option in options:
        routes+=goDownNodes(option,fft,dac)
    return routes

total=goDownNodes("svr",False,False)

print(total)