T = int(input())

for i in range(T) :
    n = int(input())
    L = list(map(int,input().split()))
    L.sort()
    L_sort=L
    L_reverse = list(reversed(L))
    x=[]
    for j in range(len(L)):
        if(L_sort[j]==L_reverse[j] ):
            x.append(L_sort[j])
            break
        elif( len(x)==len(L) ):
            break
        else:
            x.append(L_reverse[j])
            x.append(L_sort[j])
    print("#" + str(i + 1), end=" ")
    if(len(x)>10):
        for k in range(10) :
            print(x[k], end=" ")
    else:
        for k in x :
            print(k,end=" ")
    print()



