T = int(input())
# x=시작점
def next_stop(stop,k,n,m):
    cnt = 0
    for j in range(stop+k, stop-1, -1):
        if (j in elec):
            stop = j
            cnt +=1
        if(j+k>n):



for i in range(T) :
    k,n,m = map(int,input().split())
    elec = list(map(int,input().split()))
    cnt=0
    stop=0

    print("#" + str(i + 1), cnt)
