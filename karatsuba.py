a=3141592653589793238462643383279502884197169399375105820974944592
b=2718281828459045235360287471352662497757247093699959574966967627

def kara(x,y):
    xstr=str(x)
    if len(xstr) == 1:
        #print('bas:',x*y)
        return x*y
    
    a=int(xstr[0:int(len(xstr)/2)])
    b=int(xstr[int(len(xstr)/2):len(xstr)])
        
    ystr=str(y)
    len_y=len(ystr)
    lyp2=int(len_y/2)
    c=int(ystr[0:lyp2])
    d=int(ystr[lyp2:len_y])
    ac=kara(a,c)
    ad=kara(a,d)
    bc=kara(b,c)
    bd=kara(b,d)
    
    r=10**len_y*ac+10**lyp2*(ad+bc)+bd
    #print('ret:',r)
    return (r)
        
c = kara(a,b)
print(c)
print(a*b)
