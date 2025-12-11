input=open('exInput.txt','r')
lines = input.readlines()

lights=[]
buttons=[]

for line in lines:
    lineButtons=[]
    lStart=line.index('[')+1
    lEnd=line.index(']')
    light=list(line[lStart:lEnd])
    lights.append(light)
    for i in range(len(line)):
        if line[i]=='(':
            end=line[i:].index(')')+i
            button=line[i+1:end].split(',')
            lineButtons.append(button)
    buttons.append(lineButtons)

for i in range(len(lights)):
    newLight=[]
    for light in lights[i]:
        if light=='.':
            newLight.append(False)
        else:
            newLight.append(True)
    lights[i]=newLight


for i in range(len(buttons)):
    newLine=[]
    for button in buttons[i]:
        base=[False for i in range(len(lights[i]))]
        for point in button:
            base[int(point)]=True
        newLine.append(base)
    buttons[i]=newLine

stop=False

def nightMareFunc(intendedLights,currentLights,buttons,pressed):
    global stop
    if intendedLights==currentLights:
        stop=True
        print("FOUND")
        print(pressed)
        return [pressed]
    elif stop or pressed==100:
        return [-1]
    else:
        options=[]
        for button in buttons:
            mutable=currentLights
            for i in range(len(button)):
                if button[i]:
                    #print("changed state")
                    mutable[i]= not mutable[i]
            print("PRESSES")
            print(pressed)
            print("PREV STATE")
            print(currentLights)
            print("BUTTON")
            print(button)
            print("NEW STATE")
            print(mutable)
            options+=nightMareFunc(intendedLights,mutable,buttons,pressed+1)
        return options

total=0

for i in range(len(lights)):
    stop=False
    base=[False for _ in range(len(lights[i]))]
    print(buttons[i])
    times=nightMareFunc(lights[i],base,buttons[i],0)
    for time in times:
        if time!=-1:
            total+=time
    break

print(total)

