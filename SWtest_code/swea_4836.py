T = int(input())
# [[x좌표,y좌표,색칠된 컬러(1,2)]] --> len=4 이면 count한다
for i in range(T) :
    N = int(input())
    L=[[i,j] for i in range(10) for j in range(10)]
    for j in range(N) :
        x1, y1, x2, y2, c1 = map(int, input().split())
        R=[[i,j] for i in range(x1,x2+1) for j in range(y1,y2+1)]
        for x in L:
            for y in R:
                if (x[:2] == y):
                    x.append(c1)
    cnt = 0
    for x in L :
        for y in R :
            if(x[:2]==y and len(x)==4):
                cnt+=1


    print("#" + str(i + 1),cnt)
