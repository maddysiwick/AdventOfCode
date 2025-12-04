import math
input=open('Input.txt','r')
lines = input.readlines()

parsed=[[],[]]
for line in lines:
    parsed[0].append(line[0])
    parsed[1].append(int(line[1:]))

print(parsed)

counter=0
num=50
turnMultiplier=1

for i in range(len(parsed[0])):
    if parsed[0][i]=='L':
        turnMultiplier=-1
    else:
        turnMultiplier=1
    counter+=parsed[1][i]//100
    print("thingy"+str((parsed[1][i]%100)*turnMultiplier))
    if num+(parsed[1][i]%100)*turnMultiplier>99:
        print("around right")
        counter+=1
    if num+(parsed[1][i]%100)*turnMultiplier<=0 and num!=0:
        print("around left")
        counter+=1
    print("counter"+str(counter))
    num+=turnMultiplier*parsed[1][i]
    if num<0:
        num=100-(abs(num)%100)
    if num>99:
        num=(num%100)
        
    
    print(num)
    
print(counter)