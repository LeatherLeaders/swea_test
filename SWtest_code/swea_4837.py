T = int(input())

for i in range(T) :
    n,k  = map(int,input().split())
    print(k)
    L=[i for i in range(1,13)]
    p = len(L)
    cnt_ = 0
    for a in range(1<<p) :
        x=[]
        for b in range(p):
            if a & (1<<b) :
                x.append(L[b])
        if(len(x)==n):
            tmp=0
            for j in x :
                tmp+=j
            if(tmp==k):
                cnt_+=1

    print("#" + str(i + 1),cnt_)


# 3
# 3 6
# 5 15
# 5 10