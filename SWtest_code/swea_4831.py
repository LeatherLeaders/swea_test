T = int(input())
# x=시작점
def next_stop(stop,cnt):

    for i in range(stop + k, stop, -1):
        if (i in elec):
            stop = i
            cnt += 1
            break
        elif(i==stop+1):
            cnt=-1
    if (cnt == -1):
        print("#" + str(j + 1), 0)
    elif(stop+k>=n) :
        print("#" + str(j + 1), cnt)
    else:
        next_stop(stop,cnt)




for j in range(T) :
    k,n,m = map(int,input().split())
    elec = list(map(int,input().split()))

    next_stop(0,0)
    # print("#" + str(i + 1), count)
