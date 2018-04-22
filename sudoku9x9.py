
import os
clauses = []
satlines = []


def ooo(a,b,c,d,e,f,g,h,i):
    sa=str(a)
    sb=str(b)
    sc=str(c)
    sd=str(d)
    se=str(e)
    sf=str(f)
    sg=str(g)
    sh=str(h)
    si=str(i)
    clauses.append(sa+" "+sb+" "+sc+" "+sd+" "+se+" "+sf+" "+sg+" "+sh+" "+si+" 0")
    clauses.append("-"+sa+" -"+sb+" 0")
    clauses.append("-"+sa+" -"+sc+" 0")
    clauses.append("-"+sa+" -"+sd+" 0")
    clauses.append("-"+sa+" -"+se+" 0")
    clauses.append("-"+sa+" -"+sf+" 0")
    clauses.append("-"+sa+" -"+sg+" 0")
    clauses.append("-"+sa+" -"+sh+" 0")
    clauses.append("-"+sa+" -"+si+" 0")
    clauses.append("-"+sb+" -"+sc+" 0")
    clauses.append("-"+sb+" -"+sd+" 0")
    clauses.append("-"+sb+" -"+se+" 0")
    clauses.append("-"+sb+" -"+sf+" 0")
    clauses.append("-"+sb+" -"+sg+" 0")
    clauses.append("-"+sb+" -"+sh+" 0")
    clauses.append("-"+sb+" -"+si+" 0")
    
    clauses.append("-"+sc+" -"+sd+" 0")
    clauses.append("-"+sc+" -"+se+" 0")
    clauses.append("-"+sc+" -"+sf+" 0")
    clauses.append("-"+sc+" -"+sg+" 0")
    clauses.append("-"+sc+" -"+sh+" 0")
    clauses.append("-"+sc+" -"+si+" 0")
    
    clauses.append("-"+sd+" -"+se+" 0")
    clauses.append("-"+sd+" -"+sf+" 0")
    clauses.append("-"+sd+" -"+sg+" 0")
    clauses.append("-"+sd+" -"+sh+" 0")
    clauses.append("-"+sd+" -"+si+" 0")
    
    clauses.append("-"+se+" -"+sf+" 0")
    clauses.append("-"+se+" -"+sg+" 0")
    clauses.append("-"+se+" -"+sh+" 0")
    clauses.append("-"+se+" -"+si+" 0")
    
    clauses.append("-"+sf+" -"+sg+" 0")
    clauses.append("-"+sf+" -"+sh+" 0")
    clauses.append("-"+sf+" -"+si+" 0")

    clauses.append("-"+sg+" -"+sh+" 0")
    clauses.append("-"+sg+" -"+si+" 0")

    clauses.append("-"+sh+" -"+si+" 0")


#===    puzzle input   =========
print("paste a sudoku puzzle here:")
items = [ input().split() for i in range(9) ]


j=1
for item in items:
    i=1
    for i in range(9):
        c=str(item)[i+2:i+3]
        if c != ".":
            #print (100*j+10*(i+1)+int(c),0)
            clauses.append(str(100*j+10*(i+1)+int(c))+" 0")
        i=i+1
    j=j+1
    
#exeptions
#clauses.append('-112 -127 -136 -141 -153 -165 -178 -184 -199 -218 -223 -235 -242 -254 -269 -271 -287 -296 -311 -324 -339 -347 -358 -366 -372 -383 -395 -415 -426 -433 -444 -451 -462 -477 -489 -498 -514 -521 -532 -549 -557 -568 -575 -586 -593 -617 -629 -638 -645 -656 -663 -674 -681 -692 -716 -725 -734 -743 -752 -761 -779 -788 -797 -813 -822 -831 -848 -859 -867 -876 -885 -894 -919 -928 -937 -946 -955 -964 -973 -982 -991 0')
        
#============== general sudoku clauses  ==== 


for i in range(1,10):
    for j in range(1,10):
        ij=100*i+10*j
        ooo(ij+1,ij+2,ij+3,ij+4,ij+5,ij+6,ij+7,ij+8,ij+9)

# rows
for i in range(1,10):
    for k in range(1,10):
        ij = 100*i
        ooo(ij+10+k,ij+20+k,ij+30+k,ij+40+k,ij+50+k,ij+60+k,ij+70+k,ij+80+k,ij+90+k)

#colums
for j in range(1,10):
    for k in range(1,10):
        jj=j*10
        ooo(100+jj+k,200+jj+k,300+jj+k,400+jj+k,500+jj+k,600+jj+k,700+jj+k,800+jj+k,900+jj+k)
        
for k in range(1,10):
    ooo(110+k,120+k,130+k,210+k,220+k,230+k,310+k,320+k,330+k)
    ooo(140+k,150+k,160+k,240+k,250+k,260+k,340+k,350+k,360+k)
    ooo(170+k,180+k,190+k,270+k,280+k,290+k,370+k,380+k,390+k)

    ooo(410+k,420+k,430+k,510+k,520+k,530+k,610+k,620+k,630+k)
    ooo(440+k,450+k,460+k,540+k,550+k,560+k,640+k,650+k,660+k)
    ooo(470+k,480+k,490+k,570+k,580+k,590+k,670+k,680+k,690+k)
    
    ooo(710+k,720+k,730+k,810+k,820+k,830+k,910+k,920+k,930+k)
    ooo(740+k,750+k,760+k,840+k,850+k,860+k,940+k,950+k,960+k)
    ooo(770+k,780+k,790+k,870+k,880+k,890+k,970+k,980+k,990+k)

# write CNF clauses to file
with open ("sudoku.cnf","w") as f:
    for c in clauses:
        f.write(''.join(map(str,c))+"\n")

for i in range(3):        
    
    # calling minisat solver
    os.system("minisat sudoku.cnf tmp.sat")

    with open ("tmp.sat","r") as satfile:
        for line in satfile:
            satlines.append(line)
        

    # striping the solution from tmp.sat
    bf=''
    res=''
    exct=''
    print(str(satlines[0:1]))
    inp = satlines[1:2]
    inp = str(inp)
    inp=inp[2:]

    for c in inp:
        bf=bf+c
        if c == " ":
            if int(bf) > 0:
                res=res+bf[2]+' '
                exct=exct+"-"+bf
            bf=''

    print (exct)
    #print (res[0:18])
    #print (res[18:36])
    #print (res[36:54])
    #print (res[54:72])
    #print (res[72:90])
    #print (res[90:108])
    #print (res[108:126])
    #print (res[126:144])
    #print (res[144:162])

    with open ("sudoku.cnf","a") as f:
        c = exct + " 0"
        f.write(''.join(map(str,c))+"\n")
        f.close


