T = int(input())

for i in range(T) :
    n = int(input())
    num = input()
    cnt=[0,0,0,0,0,0,0,0,0,0]
    for j in range(n):
        cnt[int(num[j])]+=1
    x=max(cnt)
    y=0
    for k in range(len(cnt)) :
        if(cnt[k]==x):
            y=k
    print("#" + str(i + 1), y,x)
