T = int(input())
for i in range(T) :
    n = int(input())
    List = list(map(int,input().split()))
    List.sort()
    print("#"+str(i+1),List[-1]-List[0])