T = int(input())
# [[x좌표,y좌표,색칠된 컬러(1,2)]] --> len=4 이면 count한다
for i in range(T) :

    N = int(input())
    R_1=[]
    R_2=[]

    for j in range(N) :
        x1, y1, x2, y2, c1 = map(int, input().split())
        if(c1==1):
            R = [[i, j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)]
            for k in R :
                if(not k in R_1):
                    R_1.append(k)
        else :
            R = [[i, j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)]
            for k in R :
                if(not k in R_2):
                    R_2.append(k)

    cnt = 0
    for x in R_1 :
        if(x in R_2):
            cnt+=1

    print("#" + str(i + 1),cnt)
