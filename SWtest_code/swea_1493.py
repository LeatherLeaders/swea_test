T = int(input())
L=[]
for j in range(1,201):
     for x in range(1,j+1):
         y=-x+j+1
         z=int(j*(j-1)/2+x)
         l=[x,y,z]
         L.append(l)
for i in range(T) :
    m,n = map(int,input().split())
    x_1,y_1,x_2,y_2 = 0,0,0,0
    for j in L :
        if(j[2]==m):
            x_1,y_1=j[0],j[1]
        elif(j[2]==n):
            x_2,y_2=j[0],j[1]
    x=x_1+x_2
    y=y_1+y_2

    for j in L :
        if(j[0]==x and j[1]==y):
            print("#" + str(i + 1), j[2])
            break
