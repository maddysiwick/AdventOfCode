input=open('Input.txt','r')
lines = input.readlines()

banks=[]

for line in lines:
    print(line)
    banks.append(list(line.strip("\n")))

total=0

for bank in banks:
    spot=0
    batteriesLeft=12
    joltage=''
    while batteriesLeft>0:
        highest=0
        for i in range(spot,len(bank)-batteriesLeft+1):
            if int(bank[i])>int(highest):
                highest=bank[i]
                spot=i
        spot+=1
        batteriesLeft-=1
        joltage+=highest
    print(joltage)
    total+=int(joltage)

print(total)