n = int(input())

for i in range(n+1,1000000):
    if(i%2==0):
        continue
    num=str(i)
    if(num[int(len(num)/2):len(num)]==num[int(len(num)/2)-((len(num)+1)%2)::-1]) :
        for j in range(1,i//2):
            if(i%j==0):
                break
        print(i)
        break
