i=[13,2,4,1,5,6,9,7,33,12,21,8,17,3,27,11]
print (" input=",i)
o=[]
def meso(inp):
    c=[]
    le=len(inp)
    if le == 2:
        if inp[0] > inp[1]:
            return([inp[1],inp[0]])
        else:
            return(inp)
    a=inp[0:int(le/2)]
    b=inp[int(le/2):le]
    aout=meso(a)
    aout.append(10000)
    bout=meso(b)
    bout.append(10000)
    i=0
    j=0
    for k in range(0,le):
        if aout[i] < bout[j]:
            c.append(aout[i])
            i=i+1
        else:
            c.append(bout[j])
            j=j+1
    return(c)

iout= meso(i)
print ("output=",iout)
