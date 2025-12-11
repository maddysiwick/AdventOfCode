input=open('exInput.txt','r')
lines = input.readlines()

boxes=[]

for line in lines:
    junction=line.strip("\n").split(",")
    junction=[int(junction[0]),int(junction[1]),int(junction[2])]
    boxes.append(junction)


circuits=[]

def ddp(box1,box2):
    distance=(((box1[0]-box2[0])**2)+((box1[1]-box2[1])**2)+((box1[2]-box2[2])**2))**0.5
    return distance

pairs=[]
for box in boxes:
    minDistance=ddp(box,boxes[boxes.index(box)-1])
    print("stuff:")
    closest=boxes[boxes.index(box)-1]
    for otherBox in boxes:
        if box!=otherBox:
            distance=ddp(box,otherBox)
            if distance<=minDistance:
                minDistance=distance
                closest=otherBox
    if (minDistance,closest,box) not in pairs:
        pairs.append((minDistance,box,closest))

pairs.sort()
pars=pairs[:10]

circuits=[]

for pair1 in pairs:
    createCircuit=False
    for i in range(len(circuits)):
        if pair1[1] in circuits[i] or pair1[2] in circuits[i]:
            circuits[i]=list(set(circuits[i]+pair1[1:]))
            break
    for pair2 in pairs:
        if list(set(pair1)&set(pair2))!=[]:
            foundCircuit=False
            for i in range(len(circuits)):
                if pair1[1] in circuits[i] or pair1[2] in circuits[i]:
                    circuits[i]=list(set(circuits[i]+pair1[1:]+pair2[1:]))
                    foundCircuit=True
            if not foundCircuit:
                circuits.append(list(set(pair1[1:]+pair2[1:])))

for circuit in circuits:
    print(circuit)