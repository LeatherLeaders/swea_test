#자료 [[x,y],[생성시간,생명력,상태]] 상태 = 0(죽음),1(살아있음)

# 1
# 2 2 10
# 1 1
# 0 2
class plants :
    def __init__(self,x,y,T,H):
        self.x = x
        self.y = y
        self.T =T
        self.H = H
        self.S = 1

#nexttime은 다음 시기로 넘어간다
def nextTime(info,time) :
    add_P = []
    for i in info :
        if(time == i.T+i.H+1):
            P1 = plants(i.x+1,i.y,time+1,i.H)
            P2 = plants(i.x-1,i.y,time+1,i.H)
            P3 = plants(i.x,i.y+1,time+1,i.H)
            P4 = plants(i.x,i.y-1,time+1,i.H)
            add_P.append(P1,P2,P3,P4)
    for j in add_P:

T = int(input())
for i in range(T) :
    n,m,k = map(int,input().split())
    info = []
    for j in range(n) :
        x = list(map(int,input().split()))
        for k in range(m) :
            P=plants(j,k,0,x[k])
            info.append(P)


