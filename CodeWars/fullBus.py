def enough(cap, on, wait):
    freeSpace=cap-on
    canPick=freeSpace-wait
    
    if freeSpace<0:
        return 0
    elif freeSpace>0 : 
        if canPick<=0:
            canPick=abs(canPick)
            return canPick
        else:
            return 0
    elif freeSpace==0:
        return wait