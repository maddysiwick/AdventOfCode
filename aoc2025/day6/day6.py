input=open('Input.txt','r')
lines = input.readlines()

columns=[]
places=[]

for place in range(len(lines[-1])):
    if lines[-1][place]=='+' or lines[-1][place]=='*':
        places.append(place)

print(places)

for i in range(len(places)):
    column=[]
    for line in lines[0:-1]:
        if i<len(places)-1:
            column.append(line[places[i]:places[i+1]].strip("\n"))
        else:
            column.append(line[places[i]:].strip("\n"))
    column.append(lines[-1][places[i]])
    columns.append(column)

print(columns)

total=0

for col in columns:
    placeExists=True
    index=0
    nums=[]
    while placeExists:
        num=''
        for term in col[:-1]:
            if index<len(term):
                if term[index].isdigit():
                    num+=term[index]
        if num=='':
            placeExists=False
        else:
            nums.append(int(num))
            index+=1
    nums.reverse()
    if col[-1]=='+':
        total+=sum(nums)
    elif col[-1]=='*':
        result=1
        for num in nums:
            result*=num
        total+=result
print(total)