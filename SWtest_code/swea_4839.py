T = int(input())


def binary(l,r,x,cnt):

    c=int((l+r)/2)
    if(c==x):
        cnt+=1
        return cnt
    elif(c<x):
        cnt+=1
        return binary(c,r,x,cnt)
    else :
        cnt+=1
        return binary(l,c,x,cnt)


for i in range(T) :
    r,a,b  = map(int,input().split())
    cnt_a = binary(1,r,a,0)
    cnt_b = binary(1,r,b,0)
    if (cnt_a==cnt_b):
        print("#" + str(i + 1), 0)
    elif (cnt_a < cnt_b):
        print("#" + str(i + 1), "A")
    else:
        print("#" + str(i + 1), "B")

3
400 300 350
1000 299 578
1000 222 888