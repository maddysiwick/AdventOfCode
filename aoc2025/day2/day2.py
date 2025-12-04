input=open('Input.txt','r')
text = input.readlines()[0]
ranges = text.split(',')

parsed=[[],[]]
print(ranges)

for r in ranges:
    rrange=r.split('-')
    parsed[0].append(rrange[0])
    parsed[1].append(int(rrange[1]))
print(parsed)

total=0

for i in range(len(parsed[0])):
    lenOptions=[]
    dups=[]
    for l in range(len(parsed[0][i]),len(str(parsed[1][i]))+1):
        lenOptions.append(l)
    print("invalid ids")
    startValue='0'
    
    
    while(len(startValue)<=len(str(parsed[1][i]))//2):
        mults=[]
        for o in lenOptions:
            if o%len(startValue)==0 and o//len(startValue)>1:
                mults.append(o//len(startValue))
        for mult in mults:
            if parsed[1][i]>=(int(startValue*mult))>=int(parsed[0][i]) and dups.__contains__(startValue*mult)==False:
                total+=int(startValue*mult)
                dups.append(startValue*mult)
                print(startValue*mult)
        startValue=str(int(startValue)+1)

print(total)