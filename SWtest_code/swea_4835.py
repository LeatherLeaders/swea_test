T = int(input())

for i in range(T) :
    n,m = map(int,input().split())
    L = list(map(int,input().split()))
    sum=[]
    for j in range(n-m+1):
        tmp=0
        for k in range(m):
            tmp+=L[j+k]
        sum.append(tmp)
    max_sum = max(sum)
    min_sum = min(sum)
    print("#" + str(i + 1), max_sum-min_sum)
